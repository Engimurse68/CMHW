# hw3a.py
#region imports
from math import sqrt, pi, exp
from NumericalMethods import GPDF, Simpson, Probability
#endregion

def cumulative(c, mu, sig):
    return Probability(GPDF, (mu, sig), c, GT=False)


def main():
    print("Welcome to Normal Probability Calculator")
    mu = float(input("Enter mean (mu): "))
    sig = float(input("Enter standard deviation (sigma): "))
    mode = input("Are you specifying 'c' to find P, or 'P' to find c? (c/p): ").lower()
    type_prob = input("Type of probability: single-less (sl), single-greater (sg), double-inside (di), double-outside (do): ").lower()
    if mode == 'c':
        c = float(input("Enter c: "))
        if type_prob == 'sl':
            p = cumulative(c, mu, sig)
        elif type_prob == 'sg':
            p = 1 - cumulative(c, mu, sig)
        elif type_prob == 'di':
            d = abs(c - mu)
            p = cumulative(mu + d, mu, sig) - cumulative(mu - d, mu, sig)
        elif type_prob == 'do':
            d = abs(c - mu)
            p = 1 - (cumulative(mu + d, mu, sig) - cumulative(mu - d, mu, sig))
        else:
            print("Invalid type")
            return
        print(f"The probability is {p:.6f}")
    elif mode == 'p':
        p_des = float(input("Enter desired probability P (0-1): "))
        if p_des < 0 or p_des > 1:
            print("Invalid P")
            return
        if type_prob == 'sl':
            target = p_des
        elif type_prob == 'sg':
            target = 1 - p_des
        elif type_prob == 'di':
            target = (1 + p_des) / 2
        elif type_prob == 'do':
            target = 1 - p_des / 2
        else:
            print("Invalid")
            return
        def f(c):
            return cumulative(c, mu, sig) - target
        x0 = mu - 5 * sig
        x1 = mu + 5 * sig
        c_found, iters = Secant(f, x0, x1, maxiter=20, xtol=1e-6)
        print(f"The value of c is {c_found:.6f} (after {iters} iterations)")
        if type_prob in ['di', 'do']:
            other = 2 * mu - c_found
            print(f"The symmetric bound is {other:.6f}")
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()