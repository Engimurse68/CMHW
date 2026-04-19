# Exam1Q1
"""
Gravel Supplier Statistical Comparison
=======================================
Simulates gravel sampling for two suppliers with different sieve sizes and
performs a one-sided t-test to determine if Supplier B's gravel is
statistically significantly smaller than Supplier A's.

Supplier A: Large aperture screen 1" x 1"   -> D_Max = 1.000"
Supplier B: Smaller aperture screen 7/8"x7/8" -> D_Max = 0.875"

Hypothesis Test (one-sided, alpha = 0.05):
  H0: mu_A <= mu_B  (Supplier B is NOT smaller)
  H1: mu_A >  mu_B  (Supplier B IS smaller -> Supplier B's claim)
"""

#region imports: the last 4 taken from homework4
import math
import sys
import os
from random import random as rnd
from scipy.integrate import quad
from scipy.optimize import fsolve
from matplotlib import pyplot as plt

# Add uploads directory so we can import the homework files
sys.path.insert(0, '/mnt/user-data/uploads')

# I attmepted to use the import function for portions of homework 4 and three,
# but it wasn't working, so I did it the long way. The following were copied from homework 4
def ln_PDF(D, mu, sig):
    '''
    Computes f(D) for the log-normal probability density function.
    '''
    if D <= 0.0:
        return 0.0
    p = 1 / (D * sig * math.sqrt(2 * math.pi))
    _exp = -((math.log(D) - mu)**2) / (2 * sig**2)
    return p * math.exp(_exp)

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

def t_CDF(z, m):
    k_m = Km(m)
    if z >= 0:
        int_val = Simpson_t(m, 0, z)
        return 0.5 + k_m * int_val
    else:
        int_val = Simpson_t(m, 0, -z)
        return 0.5 - k_m * int_val
# I believe this is the starting point of my copying from homework 3
def Km(m):
    g1 = gamma((m + 1) / 2)
    g2 = gamma(m / 2)
    return g1 / (math.sqrt(m * math.pi) * g2)

def t_pdf(u, m):
    return (1 + u**2 / m) ** (- (m + 1)/2)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial defined only for non-negative integers")
    res = 1.0
    for i in range(1, int(n) + 1):
        res *= i
    return res

def gamma(alpha):
    if alpha <= 0:
        raise ValueError("Gamma input must be positive")
    if math.isclose(alpha, round(alpha)):
        return factorial(alpha - 1)
    elif math.isclose(alpha - math.floor(alpha), 0.5):
        n = int(alpha - 0.5)
        return factorial(2 * n) * math.sqrt(math.pi) / (4 ** n * factorial(n))
    else:
        raise NotImplementedError("Gamma implemented only for integers and half-integers")
def Simpson_t(m, a, b, N=10000):
    if a > b:
        return -Simpson_t(m, b, a, N)
    if a == b:
        return 0.0
    if N % 2 == 1:
        N += 1
    h = (b - a) / N
    sum_val = t_pdf(a, m) + t_pdf(b, m)
    for i in range(1, N):
        x = a + i * h
        sum_val += 4 * t_pdf(x, m) if i % 2 == 1 else 2 * t_pdf(x, m)
    return (h / 3) * sum_val

#region t-test functions, with assistance in writing from Claude.ai
def pooled_t_statistic(means_A, means_B):
    """
    Computes the two-sample pooled t-statistic for comparing two sets of
    sample means, assuming equal variances.

    :param means_A: list of sample means for Supplier A
    :param means_B: list of sample means for Supplier B
    :return: (t_stat, degrees_of_freedom, xbar_A, xbar_B, sp)
    """
    nA = len(means_A)
    nB = len(means_B)

    xbar_A, s2_A = sampleStats(means_A)
    xbar_B, s2_B = sampleStats(means_B)

    # Pooled variance
    sp2 = ((nA - 1) * s2_A + (nB - 1) * s2_B) / (nA + nB - 2)
    sp = math.sqrt(sp2)

    # t-statistic: testing if mu_A > mu_B
    t_stat = (xbar_A - xbar_B) / (sp * math.sqrt(1/nA + 1/nB))
    dof = nA + nB - 2

    return t_stat, dof, xbar_A, xbar_B, sp


def one_sided_p_value(t_stat, dof):
    """
    Computes the one-sided p-value P(T > t_stat) using the t-CDF from hw3b.

    :param t_stat: computed t-statistic
    :param dof: degrees of freedom
    :return: p-value (float)
    """
    # P(T > t) = 1 - F(t)
    return 1.0 - t_CDF(t_stat, dof)
#endregion

#region input/output functions
def get_supplier_params(supplier_name, default_D_Max, default_D_Min, mean_ln, sig_ln):
    """
    Prompts user for sieve parameters for a given supplier.

    :param supplier_name: string label (e.g. 'Supplier A')
    :param default_D_Max: default maximum sieve aperture (inches)
    :param default_D_Min: default minimum sieve aperture (inches)
    :param mean_ln: default mean of ln(D)
    :param sig_ln: default std dev of ln(D)
    :return: (mean_ln, sig_ln, D_Min, D_Max)
    """
    print(f"\n--- {supplier_name} Parameters ---")
    mean_ln, sig_ln = getPreSievedParameters((mean_ln, sig_ln))

    st_DMax = input(f"  Large aperture (D_Max) for {supplier_name}? ({default_D_Max:.4f}\"): ").strip()
    D_Max = default_D_Max if st_DMax == '' else float(st_DMax)

    st_DMin = input(f"  Small aperture (D_Min) for {supplier_name}? ({default_D_Min:.4f}\"): ").strip()
    D_Min = default_D_Min if st_DMin == '' else float(st_DMin)

    return mean_ln, sig_ln, D_Min, D_Max


def print_results_header():
    """Prints the CLI header for the program."""
    print("\n" + "="*65)
    print("  GRAVEL SUPPLIER STATISTICAL COMPARISON")
    print("  One-Sided t-Test: Is Supplier B's gravel significantly smaller?")
    print("="*65)


def print_supplier_summary(name, means, N_samples):
    """
    Prints a summary table of sample means for a supplier.

    :param name: supplier name string
    :param means: list of sample means
    :param N_samples: number of samples
    """
    mean_of_means, var_of_means = sampleStats(means)
    print(f"\n  {name} — {N_samples} samples of 100 rocks each:")
    print(f"  {'Sample':>8}  {'Mean D (in)':>12}")
    print(f"  {'-'*22}")
    for i, m in enumerate(means):
        print(f"  {i+1:>8}  {m:>12.4f}")
    print(f"  {'-'*22}")
    print(f"  {'Mean of means:':>20}  {mean_of_means:.4f}")
    print(f"  {'Var of means:':>20}  {var_of_means:.6f}")


def print_hypothesis_test(t_stat, dof, p_value, xbar_A, xbar_B, alpha=0.05):
    """
    Prints the full hypothesis test formulation and conclusion.

    :param t_stat: computed t-statistic
    :param dof: degrees of freedom
    :param p_value: computed one-sided p-value
    :param xbar_A: mean of Supplier A sample means
    :param xbar_B: mean of Supplier B sample means
    :param alpha: significance level
    """
    print("\n" + "="*65)
    print("  HYPOTHESIS TEST")
    print("="*65)
    print(f"\n  Null Hypothesis      H0: mu_A <= mu_B")
    print(f"  Alternative Hyp.     H1: mu_A >  mu_B  (B is smaller)")
    print(f"  Significance level:  alpha = {alpha}")
    print(f"\n  Mean diameter — Supplier A: {xbar_A:.4f}\"")
    print(f"  Mean diameter — Supplier B: {xbar_B:.4f}\"")
    print(f"\n  t-statistic:         {t_stat:.4f}")
    print(f"  Degrees of freedom:  {dof}")
    print(f"  One-sided p-value:   {p_value:.4f}")
    print(f"\n  Decision rule: Reject H0 if p-value < alpha ({alpha})")

    if p_value < alpha:
        print(f"\n  RESULT: p = {p_value:.4f} < alpha = {alpha}")
        print("  >>> REJECT H0 <<<")
        print("  Conclusion: There IS sufficient statistical evidence at the")
        print(f"  {alpha*100:.0f}% significance level to support Supplier B's claim")
        print("  that their gravel is statistically significantly smaller.")
    else:
        print(f"\n  RESULT: p = {p_value:.4f} >= alpha = {alpha}")
        print("  >>> FAIL TO REJECT H0 <<<")
        print("  Conclusion: There is NOT sufficient statistical evidence at the")
        print(f"  {alpha*100:.0f}% significance level to support Supplier B's claim.")
    print("="*65)
#endregion

#region main
def main():
    """
    Main program: simulates gravel sampling for Supplier A (1" screen) and
    Supplier B (7/8" screen), then performs a one-sided t-test (alpha=0.05)
    to evaluate Supplier B's claim of statistically smaller gravel.

    Steps:
      1. Get pre-sieve log-normal parameters and sieve sizes for each supplier
      2. Generate 11 samples of N=100 rocks per supplier
      3. Compute sample means and variances
      4. Formulate and execute one-sided two-sample t-test
      5. Report findings to user
    """
    print_results_header()

    # Default log-normal parameters (shared prior to sieving)
    default_mean_ln = math.log(2)   # ln(2) ~ 0.693, median D = 2"
    default_sig_ln  = 1.0
    N_samples    = 11
    N_sampleSize = 100

    go_again = True
    while go_again:

        # ------------------------------------------------------------------
        # Step 1: Get parameters for each supplier
        # ------------------------------------------------------------------
        mean_ln_A, sig_ln_A, D_Min_A, D_Max_A = get_supplier_params(
            "Supplier A", default_D_Max=1.000, default_D_Min=3/8,
            mean_ln=default_mean_ln, sig_ln=default_sig_ln
        )
        mean_ln_B, sig_ln_B, D_Min_B, D_Max_B = get_supplier_params(
            "Supplier B", default_D_Max=0.875, default_D_Min=3/8,
            mean_ln=default_mean_ln, sig_ln=default_sig_ln
        )

        # ------------------------------------------------------------------
        # Step 2 & 3: Generate samples and compute means for each supplier
        # ------------------------------------------------------------------
        print("\nSimulating Supplier A samples...")
        F_DMin_A, F_DMax_A = getFDMaxFDMin((mean_ln_A, sig_ln_A, D_Min_A, D_Max_A))
        _, means_A = makeSamples((mean_ln_A, sig_ln_A, D_Min_A, D_Max_A,
                                   F_DMax_A, F_DMin_A, N_sampleSize, N_samples, False))

        print("Simulating Supplier B samples...")
        F_DMin_B, F_DMax_B = getFDMaxFDMin((mean_ln_B, sig_ln_B, D_Min_B, D_Max_B))
        _, means_B = makeSamples((mean_ln_B, sig_ln_B, D_Min_B, D_Max_B,
                                   F_DMax_B, F_DMin_B, N_sampleSize, N_samples, False))

        # Print per-supplier summaries
        print_supplier_summary("Supplier A (1\" x 1\" screen)", means_A, N_samples)
        print_supplier_summary("Supplier B (7/8\" x 7/8\" screen)", means_B, N_samples)

        # ------------------------------------------------------------------
        # Step 4: One-sided t-test
        # ------------------------------------------------------------------
        t_stat, dof, xbar_A, xbar_B, sp = pooled_t_statistic(means_A, means_B)
        p_value = one_sided_p_value(t_stat, dof)

        # ------------------------------------------------------------------
        # Step 5: Report findings
        # ------------------------------------------------------------------
        print_hypothesis_test(t_stat, dof, p_value, xbar_A, xbar_B, alpha=0.05)

        go_again = input("\nRun again with different parameters? (y/N): ").strip().lower() == 'y'

#endregion

if __name__ == '__main__':
    main()