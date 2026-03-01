

#region imports
import math
from random import random as rnd
from scipy.integrate import quad
from scipy.optimize import fsolve
from matplotlib import pyplot as plt
#endregion

#region functions
def ln_PDF(D, mu, sig):
    '''
    Computes f(D) for the log-normal probability density function.
    '''
    if D <= 0.0:
        return 0.0
    p = 1 / (D * sig * math.sqrt(2 * math.pi))
    _exp = -((math.log(D) - mu)**2) / (2 * sig**2)
    return p * math.exp(_exp)

def tln_PDF(D, mu, sig, F_DMin, F_DMax):
    """
    compute the value of the truncated log-normal probability density function
    """
    denom = F_DMax - F_DMin
    if denom <= 0.0:
        return 0.0
    return ln_PDF(D, mu, sig) / denom


def F_tlnpdf(args):
    '''
    This integrates the truncated log-normal probability density function from D_Min to D
    '''
    mu, sig, D_Min, D_Max, D, F_DMax, F_DMin = args

    if D >= D_Max:
        return 1.0
    if D <= D_Min:
        return 0.0

    def integrand(x):
        return tln_PDF(x, mu, sig, F_DMin, F_DMax)  # ← no tuple here

    integral, _ = quad(integrand, D_Min, D, limit=100)
    return integral

def makeSample(args, N=100):
    ln_Mean, ln_sig, D_Min, D_Max, F_DMax, F_DMin = args
    probs = [rnd() for _ in range(N)]

    d_s = []
    for p in probs:
        def objective(D):

            d_val = D[0] if hasattr(D, '__len__') else D
            return F_tlnpdf((ln_Mean, ln_sig, D_Min, D_Max, d_val, F_DMax, F_DMin)) - p

        guess = (D_Min + D_Max) / 2
        D_sol = fsolve(objective, guess)[0]

        # Force float and clip very tightly
        D_sol = float(D_sol)
        D_sol = max(D_Min + 1e-10, min(D_Max - 1e-10, D_sol))
        d_s.append(D_sol)

    return d_s

def sampleStats(D, doPrint=False):
    """
    This function computes the mean and variance of the values listed in D
    :param D: a list of values
    :param doPrint: bool,print feedback if True
    :return: (mean, var)
    """
    N=len(D)
    mean = sum(D)/N
    var=0
    for d in D:
        var += (d-mean)**2
    var /= N-1
    if doPrint == True:
        print(f"mean = {mean:0.3f}, var = {var:0.3f}")
    return (mean, var)

def getPreSievedParameters(args):
    """
    Function to prompt user to input the mean and standard deviation for the log-normal probability density function
    :param args: default values (mean_ln, sig_ln)
    :return: (mean_ln, sig_ln)
    """
    mean_ln, sig_ln = args
    st_mean_ln = input(f'Mean of ln(D) for the pre-sieved rocks? (ln({math.exp(mean_ln):0.1f})={mean_ln:0.3f}, where D is in inches):').strip()
    mean_ln = mean_ln if st_mean_ln == '' else float(st_mean_ln)
    st_sig_ln = input(f'Standard deviation of ln(D) for the pre-sieved rocks? ({sig_ln:0.3f}):').strip()
    sig_ln = sig_ln if st_sig_ln == '' else float(st_sig_ln)
    return (mean_ln, sig_ln)

def getSieveParameters(args):
    """
    A function to prompt user for the sieve parameters
    :param args: (D_Min, D_Max)
    :return: (D_Min, D_Max)
    """
    D_Min, D_Max = args
    st_D_Max = input(f'Large aperture size? ({D_Max:0.3f})').strip()
    D_Max = D_Max if st_D_Max == '' else float(st_D_Max)
    st_D_Min = input(f'Small aperture size? ({D_Min:0.3f})').strip()
    D_Min = D_Min if st_D_Min == '' else float(st_D_Min)
    return (D_Min, D_Max)

def getSampleParameters(args):
    """
    A function to prompt user for sample parameters
    :param args: (N_samples, N_SampleSize)
    :return: (N_samples, N_SampleSize)
    """
    N_samples, N_sampleSize = args
    st_N_Samples = input(f'How many samples? ({N_samples})').strip()
    N_samples = N_samples if st_N_Samples == '' else int(st_N_Samples)
    st_N_SampleSize = input(f'How many items in each sample? ({N_sampleSize})').strip()
    N_sampleSize = N_sampleSize if st_N_SampleSize == '' else int(st_N_SampleSize)
    return (N_samples, N_sampleSize)

def getFDMaxFDMin(args):
    """
    A function to compute F_DMax, F_DMin using the log-normal distribution
    :param args: (mean_ln, sig_ln, D_Min, D_Max)
    :return: (F_DMin, F_DMax)
    """
    mean_ln, sig_ln, D_Min, D_Max = args
    F_DMax, _ = quad(ln_PDF, 1e-8, D_Max, args=(mean_ln, sig_ln))
    F_DMin, _ = quad(ln_PDF, 1e-8, D_Min, args=(mean_ln, sig_ln))
    return (F_DMin, F_DMax)

def makeSamples(args):
    """
    A function to make samples and compute the sample means
    :param args: (mean_ln, sig_ln, D_Min, D_Max, F_DMax, F_DMin, N_sampleSize, N_samples, doPrint)
    :return: Samples, Means
    """
    mean_ln, sig_ln, D_Min, D_Max, F_DMax, F_DMin, N_sampleSize, N_samples, doPrint = args
    Samples = []
    Means = []
    for n in range(N_samples):
        # Here, I am storing the computed probabilities and corresponding D's in a tuple for each sample
        sample = makeSample((mean_ln, sig_ln, D_Min, D_Max, F_DMax, F_DMin), N=N_sampleSize)
        Samples.append(sample)
        # Step 3:  compute the mean and variance of each sample and report to user
        sample_Stats = sampleStats(sample)
        Means.append(sample_Stats[0])
        if doPrint == True:
            print(f"Sample {n}: mean = {sample_Stats[0]:0.3f}, var = {sample_Stats[1]:0.3f}")
    return Samples, Means

def main():
    '''
    This program simulates a gravel production process where the initial distribution of rock sizes follows a log-normal
    distribution that is sieved between two screens.  It then randomly samples from the truncated distribution to produce
    11 samples of 100 rocks each and computes the mean and variance of each sample as well as the mean and variance of
    the sampling mean.
    Step 1:  use input to get mean of ln(D), stdev of ln(D), Dmax, and Dmin, N_samples, N_sampleSize
    Step 2:  use random to produce uniformly distributed probability values and the truncated log-normal PDF to get values for D
    Step 3:  compute the mean and variance of each sample and report to user
    Step 4:  compute the mean and variance of the sampling mean and report to user
    :return: nothing
    '''
    # setup some default values
    mean_ln = math.log(2)  # units are inches
    sig_ln = 1
    D_Max = 1
    D_Min = 3.0/8.0
    N_samples = 11
    N_sampleSize = 100
    goAgain = True

    while goAgain:
        # Step 1:  use input to get mean of ln(D), stdev of ln(D), Dmax, and Dmin, N_samples, N_sampleSize
        mean_ln, sig_ln = getPreSievedParameters((mean_ln, sig_ln))
        D_Min, D_Max = getSieveParameters((D_Min, D_Max))
        N_samples,N_sampleSize = getSampleParameters((N_samples, N_sampleSize))
        F_DMin, F_DMax = getFDMaxFDMin((mean_ln, sig_ln, D_Min, D_Max))


        Samples, Means = makeSamples((mean_ln, sig_ln, D_Min, D_Max, F_DMax, F_DMin, N_sampleSize, N_samples, True))


        stats_of_Means = sampleStats(Means)
        print(f"Mean of the sampling mean:  {stats_of_Means[0]:0.3f}")
        print(f"Variance of the sampling mean:  {stats_of_Means[1]:0.6f}")
        goAgain = input('Go again? (No)').strip().lower().__contains__('y')

#endregion

if __name__ == '__main__':
    main()