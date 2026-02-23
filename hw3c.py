# hw3c.py
import math
from copy import deepcopy

def is_symmetric(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j] - A[j][i]) > 1e-10:
                return False
    return True

def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    try:
        for j in range(n):
            sum_sq = sum(L[j][s] ** 2 for s in range(j))
            temp = A[j][j] - sum_sq
            if temp < 0:
                return None
            L[j][j] = math.sqrt(temp)
            for p in range(j + 1, n):
                sum_prod = sum(L[p][s] * L[j][s] for s in range(j))
                L[p][j] = (A[p][j] - sum_prod) / L[j][j]
        return L
    except:
        return None

def doolittle(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    for j in range(n):
        sum_ = sum(L[j][k] * U[k][j] for k in range(j))
        U[j][j] = A[j][j] - sum_
        if abs(U[j][j]) < 1e-10:
            raise ValueError("Pivot too small")
        L[j][j] = 1.0
        for i in range(j + 1, n):
            sum_ = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = (A[i][j] - sum_) / U[j][j]
        for k in range(j + 1, n):
            sum_ = sum(L[j][m] * U[m][k] for m in range(j))
            U[j][k] = (A[j][k] - sum_)
    return L, U

def forward_solve(L, b):
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        sum_ = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_) / L[i][i]
    return y

def back_solve(U, y):
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_ = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_) / U[i][i]
    return x

def transpose(M):
    n = len(M)
    return [[M[j][i] for j in range(n)] for i in range(n)]

def solve_system(A, b, name):
    print(f"{name}:")
    sym = is_symmetric(A)
    method = ""
    if sym:
        L = cholesky(A)
        if L:
            y = forward_solve(L, b)
            U = transpose(L)
            x = back_solve(U, y)
            method = "Cholesky"
        else:
            L, U = doolittle(A)
            y = forward_solve(L, b)
            x = back_solve(U, y)
            method = "Doolittle (not positive definite)"
    else:
        L, U = doolittle(A)
        y = forward_solve(L, b)
        x = back_solve(U, y)
        method = "Doolittle (not symmetric)"
    print(f"Method used: {method}")
    for i in range(len(x)):
        print(f" x{i+1} = {x[i]:10.6f}")
    print()

def main():
    A1 = [[1, -1, 3, 2],
          [-1, 5, -5, -2],
          [3, -5, 19, 3],
          [2, -2, 3, 21]]
    b1 = [15, -35, 94, 1]
    solve_system(A1, b1, "System 1")

    A2 = [[4, 2, 4, 0],
          [2, 2, 3, 2],
          [4, 3, 6, 3],
          [0, 2, 3, 9]]
    b2 = [20, 36, 60, 122]
    solve_system(A2, b2, "System 2")

if __name__ == "__main__":
    main()