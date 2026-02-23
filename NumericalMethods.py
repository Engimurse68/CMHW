#region imports
import Gauss_Elim as GE  # this is the module from lecture 2 that has useful matrix manipulation functions
from math import sqrt, pi, exp, cos
#endregion

#region function definitions
def Probability(PDF, args, c, GT=True):
    """
    This is the function to calculate the probability that x is >c or <c depending
    on the GT boolean.
    Step 1:  unpack args into mu and stDev
    Step 2:  compute lhl and rhl for Simpson
    Step 3:  package new tuple args1=(mu, stDev, lhl, rhl) to be passed to Simpson
    Step 4:  call Simpson with GNPDF and args1
    Step 5:  return probability
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean, standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """
    # Step 1: unpack args
    mu, sig = args
    # Step 2: compute lhl and rhl
    lhl = mu - 5 * sig
    rhl = mu + 5 * sig
    # Step 3 & 4: set correct integration limits depending on GT and call Simpson
    if GT:
        # P(x > c) = integral from c to upper limit
        args1 = (mu, sig, c, rhl)
    else:
        # P(x < c) = integral from lower limit to c   ← explicitly required in instructions
        args1 = (mu, sig, lhl, c)

    prob = Simpson(PDF, args1)
    return prob

def GPDF(args):
    """
    Here is where I will define the Gaussian probability density function.
    This requires knowing the population mean and standard deviation.
    To compute the GPDF at any value of x, I just need to compute as stated
    in the homework assignment.
    Step 1:  unpack the args tuple into variables called: x, mu, stDev
    Step 2:  compute GPDF value at x
    Step 3:  return value
    :param args: (x, mean, standard deviation)  tuple in that order
    :return: value of GPDF at the desired x
    """
    # Step 1: unpack args
    x, mu, sig = args
    # step 2: compute GPDF at x
    fx = (1 / (sig * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sig) ** 2)
    # step 3: return value
    return fx

def Simpson(fn, args, N=100):
    mu, sig, a, b = args  # unpack: mean, std dev, lower limit, upper limit

    if a >= b:
        return 0.0  # invalid interval → return zero

    # Make sure number of subintervals is even
    if N % 2 == 1:
        N += 1

    h = (b - a) / N  # step size

    # Evaluate function at the two endpoints
    sum_val = fn((a, mu, sig)) + fn((b, mu, sig))

    # Sum contributions from interior points
    for i in range(1, N):
        x = a + i * h
        if i % 2 == 1:
            sum_val += 4 * fn((x, mu, sig))  # odd indices → weight 4
        else:
            sum_val += 2 * fn((x, mu, sig))  # even indices → weight 2

    # Apply the Simpson 1/3 rule coefficient
    area = (h / 3.0) * sum_val

    return area
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    iter_count = 0  # number of new x values computed

    while iter_count < maxiter:
        f_x0 = fcn(x0)
        f_x1 = fcn(x1)

        # Prevent division by zero
        denominator = f_x1 - f_x0
        if denominator == 0:
            return x1, iter_count  # return current best guess

        # Secant formula
        x_new = x1 - f_x1 * (x1 - x0) / denominator

        iter_count += 1  # we just computed a new x value

        # Check stopping criterion
        if abs(x_new - x1) < xtol:
            return x_new, iter_count

        # Shift values for next iteration
        x0 = x1
        x1 = x_new

        # Max iterations reached → return the last computed value
    return x1, iter_count

def GaussSeidel(Aaug, x, Niter=15):
    """
    Gauss-Seidel method for Ax = b, where Aaug = [A | b]
    """
    # Try to make diagonal dominant – but don't crash if MakeDiagDom fails
    reordered = GE.MakeDiagDom(Aaug)
    if reordered is not None:
        Aaug = reordered
    # else: keep original matrix

    n = len(Aaug)

    for _ in range(Niter):
        for i in range(n):
            rhs = Aaug[i][-1]
            for j in range(n):
                if j != i:
                    rhs -= Aaug[i][j] * x[j]
            x[i] = rhs / Aaug[i][i]

    return x


def main():
    '''
    This is a function I created for testing the numerical methods locally.
    :return: None
    '''
    print("=== Local test results ===")

    # region testing GPDF
    fx = GPDF((0, 0, 1))
    print(f"GPDF(0 | mu=0, sigma=1)   = {fx:0.6f}   expected ~ 0.398942")
    # endregion

    # region testing Simpson
    p = Simpson(GPDF, (0, 1, -5, 0))
    print(f"Simpson from -5 to 0 N(0,1) = {p:0.6f}   expected ~ 0.500000")

    p_full = Simpson(GPDF, (0, 1, -5, 5))
    print(f"Simpson from -5 to 5 N(0,1) = {p_full:0.6f}   expected ~ 1.000000")
    # endregion

    # region testing Probability
    p_less = Probability(GPDF, (0, 1), 0, GT=False)
    p_greater = Probability(GPDF, (0, 1), 0, GT=True)
    print(f"P(X < 0 | N(0,1))    = {p_less:0.6f}   expected ~ 0.500000")
    print(f"P(X > 0 | N(0,1))    = {p_greater:0.6f}   expected ~ 0.500000")

    p_tail = Probability(GPDF, (0, 1), 1.96, GT=True)
    print(f"P(X > 1.96 | N(0,1)) = {p_tail:0.6f}   expected ~ 0.025000")
    # endregion

    print("=========================")


if __name__ == '__main__':
    main()