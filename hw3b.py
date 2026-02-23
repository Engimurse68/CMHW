# hw3b.py
import math

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

def Km(m):
    g1 = gamma((m + 1) / 2)
    g2 = gamma(m / 2)
    return g1 / (math.sqrt(m * math.pi) * g2)

def t_pdf(u, m):
    return (1 + u**2 / m) ** (- (m + 1)/2)

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

def F(z, m):
    k_m = Km(m)
    if z >= 0:
        int_val = Simpson_t(m, 0, z)
        return 0.5 + k_m * int_val
    else:
        int_val = Simpson_t(m, 0, -z)
        return 0.5 - k_m * int_val

def main():
    print("t-Distribution CDF Calculator")
    while True:
        inp = input("Enter degrees of freedom m (integer >0, or 'q' to quit): ")
        if inp.lower() == 'q':
            break
        try:
            m = int(inp)
            if m <= 0:
                print("m must be positive integer")
                continue
            z = float(input("Enter z value: "))
            prob = F(z, m)
            print(f"F({z:.2f}) for m={m} = {prob:.3f}")
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()