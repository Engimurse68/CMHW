'''
Program to plot the numerical solution vs the exact solution of the IVP: y'=(y-0.01x^2)^2 * sin(x^2) + 0.02x, y(0) = 0.4
Numerical solution uses steps of h=0.2.  As no particular method for solving the IVP was given
RK4 method will be used.'''

#region imports
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import quad


#exact solution
'''Computes S(x)
    :param x: upper limit
    :return: float value of the integral'''
def S(x):
    val, _ = quad(lambda t:math.sin(t**2), 0, x)
    return val

def exact_solution(x, C=2.5):
    '''Computes the exact solution of the IVP
    :param x: x value
    :param C: integration constant
    :return: y value'''
    return 0.01 * x**2 + 1.0/(C-S(x))
#end region

#region ODE and Solve

def ode(x,y):
    return (y-0.01 * x**2)**2 * math.sin(x**2) + 0.02 * x
'''rolls through a single RK$ step'''
def rk4_step(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h * k1/2)
    k3 = f(x + h/2, y + h * k2/2)
    k4 = f(x + h, y + h*k3/2)
    return y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
'''solves the IVP using RK4'''
def rk4_solve(f, x0, y0, x_end, h):
    x_vals = [x0]
    y_vals = [y0]
    x = x0
    y = y0
    while x < x_end - 1e-10:
        y = rk4_step(f, x, y, h)
        x = round(x + h, 10)
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals

#engregion

'''okay, so that whole last portion was 98% written without claude. exceptions include tolerance and rounding'''
'''making the plot'''
def doPlot(x_exact, y_exact, x_num, y_num):
    print("doPlot called")
    fig, ax = plt.subplots()
    ax.plot(x_exact, y_exact, "-k", label="exact")
    ax.plot(x_num, y_num, "^k", label="numerical", markersize=5)

    '''setting limits and labels'''
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0.0,6.0)
    ax.set_ylim(0.0,1.0)

    '''legend and title'''
    ax.legend(loc="upper left")
    ax.set_title("IVP:  y' = (y-0.01x^2)^2 * sin(x^2) + 0.02x, y(0) = 0.4")
    plt.tight_layout()
    plt.savefig(r'C:\Users\jpsim\Documents\GitHub\CMHW\prob2_plot.png')
    plt.show()

#AAAND we put it all together
# region main
import os
print(os.getcwd())

def main():

    """Main function: computes exact and numerical solutions and plots them.
    Steps:
      1. Generate dense x array and compute exact solution for smooth line
      2. Solve numerically with RK4 at h=0.2 increments
      3. Plot both solutions with required formatting
    """
    # Step 1: exact solution on a dense grid for a smooth line.  Claude helped me with line spacing
    print("step 1 - computing exact solution")
    x_exact = np.linspace(0, 6, 300)
    y_exact = [exact_solution(x) for x in x_exact]

    # Step 2: numerical solution at h=0.2
    print("step 2 - computing numerical solution")
    x_num, y_num = rk4_solve(ode, x0=0.0, y0=0.4, x_end=6.0, h=0.2)

    # Step 3: plot
    print("step 3 - plotting")
    doPlot(x_exact, y_exact, x_num, y_num)

main()
# endregion