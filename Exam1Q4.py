# prob4.py
"""
Problem 4: Improved Euler and Runge-Kutta for a 2nd Order ODE
==============================================================
Solves the IVP:  y'' - y = x,  y(0) = 1,  y'(0) = -2

Converted to first order system:
  y1' = y2
  y2' = y1 + x

Exact solution:
  y  = -x + cosh(x) - sinh(x)
  y' = -1 + sinh(x) - cosh(x)
"""

#region imports
import math
#endregion

#region exact solution
def exact_y(x):
    """
    Computes the exact solution y(x) = -x + cosh(x) - sinh(x)
    :param x: x value
    :return: y
    """
    return -x + math.cosh(x) - math.sinh(x)

def exact_yprime(x):
    """
    Computes the exact derivative y'(x) = -1 + sinh(x) - cosh(x)
    :param x: x value
    :return: y'
    """
    return -1 + math.sinh(x) - math.cosh(x)
#endregion

#region ODE system
def ode_system(x, y1, y2):
    """
    Defines the first order ODE system for y'' - y = x
      y1' = y2
      y2' = y1 + x
    :param x:  current x value
    :param y1: current y value
    :param y2: current y' value
    :return: derivatives
    """
    dy1 = y2
    dy2 = y1 + x
    return dy1, dy2
#endregion

#region Improved Euler
def improved_euler_step(x, y1, y2, h):
    """
    Performs a single Improved Euler (Heun's) step for the 2nd order ODE system.
    :param x:  current x value
    :param y1: current y value
    :param y2: current y' value
    :param h:  step size
    :return: (y1_new, y2_new) at x + h
    """
    dy1, dy2 = ode_system(x, y1, y2)
    y1_pred = y1 + h * dy1
    y2_pred = y2 + h * dy2
    dy1_pred, dy2_pred = ode_system(x + h, y1_pred, y2_pred)
    y1_new = y1 + (h/2) * (dy1 + dy1_pred)
    y2_new = y2 + (h/2) * (dy2 + dy2_pred)
    return y1_new, y2_new

def improved_euler_solve(x0, y1_0, y2_0, x_target, h):
    """
    Solves the ODE system using Improved Euler from x0 to x_target.
    :param x0:       initial x
    :param y1_0:     initial y
    :param y2_0:     initial y'
    :param x_target: target x value
    :param h:        step size
    :return: (y1, y2) at x_target
    """
    x  = x0
    y1 = y1_0
    y2 = y2_0
    while x < x_target - 1e-10:
        y1, y2 = improved_euler_step(x, y1, y2, h)
        x = round(x + h, 10)
    return y1, y2
#endregion

#region RK4
def rk4_step(x, y1, y2, h):
    """
    Performs a single RK4 step for the 2nd order ODE system. Recycled from problem 2...or was it 1?
    :param x:  current x value
    :param y1: current y value
    :param y2: current y' value
    :param h:  step size
    :return: (y1_new, y2_new) at x + h
    """
    k1_y1, k1_y2 = ode_system(x,       y1,              y2)
    k2_y1, k2_y2 = ode_system(x + h/2, y1 + h/2*k1_y1, y2 + h/2*k1_y2)
    k3_y1, k3_y2 = ode_system(x + h/2, y1 + h/2*k2_y1, y2 + h/2*k2_y2)
    k4_y1, k4_y2 = ode_system(x + h,   y1 + h*k3_y1,   y2 + h*k3_y2)
    y1_new = y1 + (h/6) * (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1)
    y2_new = y2 + (h/6) * (k1_y2 + 2*k2_y2 + 2*k3_y2 + k4_y2)
    return y1_new, y2_new

def rk4_solve(x0, y1_0, y2_0, x_target, h):
    """
    Solves the ODE system using RK4 from x0 to x_target.
    :param x0:       initial x
    :param y1_0:     initial y
    :param y2_0:     initial y'
    :param x_target: target x value
    :param h:        step size
    :return: (y1, y2) at x_target
    """
    x  = x0
    y1 = y1_0
    y2 = y2_0
    while x < x_target - 1e-10:
        y1, y2 = rk4_step(x, y1, y2, h)
        x = round(x + h, 10)
    return y1, y2
#endregion

#region CLI
def get_inputs():
    """
    Prompts the user for initial conditions, step size, and target x.
    :return: (y0, yprime0, h, x_target)
    """
    print("\nFor the initial value problem y'' - y = x")
    y0      = float(input("Enter the value of y at x=0: "))
    yprime0 = float(input("Enter the value of y' at x=0: "))
    h       = float(input("Enter the step size for the numerical solution: "))
    x_target = float(input("At what value of x do you want to know y and y'? "))
    return y0, yprime0, h, x_target

def print_results(x_target, y_ie, y2_ie, y_rk4, y2_rk4):
    """
    Prints the results of both numerical methods formatted as #.###
    :param x_target: target x value
    :param y_ie:     y from Improved Euler
    :param y2_ie:    y' from Improved Euler
    :param y_rk4:    y from RK4
    :param y2_rk4:   y' from RK4
    """
    print(f"\nAt x={x_target:#.3f}")
    print(f"For the improved Euler method: y={y_ie:#.3f}, and y'={y2_ie:#.3f}")
    print(f"For the Runge-Kutta method:    y={y_rk4:#.3f}, and y'={y2_rk4:#.3f}")
#endregion

#region main
def main():
    """
    Main function: prompts user for IVP parameters, solves using Improved
    Euler and RK4, reports results, and asks if user wants to compute at
    a different x.

    Steps:
      1. Get initial conditions, step size from user
      2. Get target x from user
      3. Solve with Improved Euler and RK4
      4. Print formatted results
      5. Ask if user wants to compute at a different x
    """
    print("\n" + "="*50)
    print("  Improved Euler and Runge-Kutta ODE Solver")
    print("="*50)

    # Step 1: get initial conditions and step size
    y0, yprime0, h, x_target = get_inputs()

    while True:
        # Step 3: solve with both methods
        y_ie,  y2_ie  = improved_euler_solve(0, y0, yprime0, x_target, h)
        y_rk4, y2_rk4 = rk4_solve(0, y0, yprime0, x_target, h)

        # Step 4: print results
        print_results(x_target, y_ie, y2_ie, y_rk4, y2_rk4)

        # Step 5: ask to compute at a different x
        again = input("\nDo you want to compute at a different x? (Y/N): ").strip().upper()
        if again != 'Y':
            break
        x_target = float(input("At what value of x do you want to know y and y'? "))
#endregion

main()