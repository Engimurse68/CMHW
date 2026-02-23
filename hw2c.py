#region imports
from copy import deepcopy
from NumericalMethods import GaussSeidel
#endregion

def main():
    """
    Uses GaussSeidel to solve two systems of linear equations
    and prints the results with 6 decimal places.

    The assignment requires:
    - Call MakeDiagDom as first step inside GaussSeidel (already handled there)
    - Solve and print the two given systems
    """

    print("HW2 Part (c) – Gauss-Seidel Results\n")

    # ────────────────────────────────────────────────
    # System 1 (3 equations)
    # Expected exact solution: [1, 2, 3]
    # ────────────────────────────────────────────────
    Aaug1 = [
        [ 3,  1, -1,  2],
        [ 1,  4,  1, 12],
        [ 2,  1,  2, 10]
    ]
    x_init1 = [0.0, 0.0, 0.0]

    sol1 = GaussSeidel(deepcopy(Aaug1), x_init1.copy(), Niter=15)

    print("System 1 solution:")
    for i, val in enumerate(sol1, 1):
        print(f"   x{i} = {val:10.6f}")
    print()

    # ────────────────────────────────────────────────
    # System 2 (4 equations)
    # Expected exact solution: [7, -1, -2, 4]
    # ────────────────────────────────────────────────
    Aaug2 = [
        [ 1, -10,  2,  4,  2],
        [ 3,   1,  4, 12, 12],
        [ 9,   2,  3,  4, 21],
        [-1,   2,  7,  3, 37]
    ]
    x_init2 = [0.0] * 4

    sol2 = GaussSeidel(deepcopy(Aaug2), x_init2.copy(), Niter=15)

    print("System 2 solution:")
    for i, val in enumerate(sol2, 1):
        print(f"   x{i} = {val:10.6f}")


if __name__ == "__main__":
    main()