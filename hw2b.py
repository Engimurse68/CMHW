#region imports
from NumericalMethods import Secant
from math import cos, pi
#endregion

#region function definitions
def fn1(x):
    """ Equation 1: x - 3*cos(x) = 0 """
    return x - 3 * cos(x)


def fn2(x):
    """ Equation 2: cos(2x) * x**3 = 0 """
    return cos(2 * x) * x**3


def main():
    """
    fn1:  x - 3*cos(x) = 0; with x0=1, x1=2, maxiter=5, xtol=1e-4
    fn2:  cos(2x)*x**3 = 0; with x0=1, x1=2, maxiter=15, xtol=1e-8
    fn2:  cos(2x)*x**3 = 0; with x0=1, x1=2, maxiter=3, xtol=1e-8

    Note: the second and third calls should converge toward a root near π/4 ≈ 0.7854
    (not π/2 ≈ 1.5708) when starting from [1, 2]
    """
    print("=== Homework 2 Part (b) - Secant Method Results ===\n")

    # Call 1: x - 3*cos(x) = 0
    root1, iter1 = Secant(fn1, 1, 2, maxiter=5, xtol=1e-4)
    print(f"root of fn1 = {root1:0.4f}, after {iter1:0d} iterations")

    # Call 2: cos(2x)*x**3 = 0, maxiter=15
    root2, iter2 = Secant(fn2, 1, 2, maxiter=15, xtol=1e-8)
    print(f"root of fn2 (maxiter=15) = {root2:0.8f}, after {iter2:0d} iterations")

    # Call 3: cos(2x)*x**3 = 0, maxiter=3
    root3, iter3 = Secant(fn2, 1, 2, maxiter=3, xtol=1e-8)
    print(f"root of fn2 (maxiter=3)  = {root3:0.8f}, after {iter3:0d} iterations")

    print("\nNote: expected root for fn2 is approximately π/4 ≈ 0.785398")
    print(f"Distance to π/4 (maxiter=15): {abs(root2 - pi/4):.10f}")
#endregion


if __name__ == "__main__":
    main()