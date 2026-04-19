# region imports
from math import sin
import math
import numpy as np
from scipy.integrate import solve_ivp #Added: referenced but not imported
from matplotlib import pyplot as plt
# endregion

# region function definitions
def odeSystem(t, X, *args):
    """
    ODE system callback for solve_ivp.
    State variables: X[0] = i1 (inductor current), X[1] = i2 (resistor current)
    Circuit equations (L series, R||C parallel):
      v(t) = L*di1/dt + Vc      where Vc = R*i2
      i1   = i2 + C*dVc/dt      where dVc/dt = R*di2/dt
    Solving:
      i1dot = (v(t) - R*i2) / L
      i2dot = (i1 - i2) / (R*C)
    :param t:    current time
    :param X:    current state [i1, i2]
    :param args: (fn, L, R, C)  where fn(t) is the voltage source callback
    :return:     [i1dot, i2dot]
    """
    fn, L, R, C = args
    i1 = X[0]
    i2 = X[1]
    vt = fn(t)
    i1dot = (vt - R * i2) / L
    i2dot = (i1 - i2) / (R * C)
    return [i1dot, i2dot]

def simulate(L=20, R=10, C=0.05, A=20, f=20, p=0, t=10, pts=500):
    """
    Simulates transient behavior of the RLC circuit.
    :param L:   Inductance (H)
    :param R:   Resistance (ohm)
    :param C:   Capacitance (F)
    :param A:   Amplitude (V)
    :param f:   frequency (Hz)
    :param p:   phase (deg)
    :param t:   simulation end time (s)
    :param pts: number of time points
    :return:    solve_ivp result object I  (I.t = time, I.y[0] = i1, I.y[1] = i2)
    """
    w   = f * 2 * math.pi          # angular frequency (rad/s)
    phi = p * math.pi / 180.0      # phase in radians
    vin = lambda t: A * sin(w * t + phi)
    myargs = (vin, L, R, C)
    x0    = [0, 0]
    tList = np.linspace(0, t, int(pts))
    I     = solve_ivp(odeSystem, t_span=[0, t], y0=x0, t_eval=tList, args=myargs)
    return I

def doPlot(*args, ax=None):
    """
    Plots i1, i2, and Vc vs time.
    :param args: ((R, tList, I))
    :param ax:   matplotlib axes (None = standalone plot)
    """
    if ax is None:
        ax = plt.subplot()
        QTPlotting = False
    else:
        QTPlotting = True

    R, tList, I = args[0]
    ax.clear()
    ax.plot(tList, I.y[0], linestyle='solid',  color='k', label=r'$i_1(t)$')
    ax.plot(tList, I.y[1], linestyle='dashed',  color='k', label=r'$i_2(t)$')
    ax.set_xlim(0, max(tList))
    minI   = min(min(I.y[0]), min(I.y[1]))
    maxI   = max(max(I.y[0]), max(I.y[1]))
    rangeI = abs(maxI - minI)
    ax.set_ylim(minI - 0.01 * rangeI, maxI + 0.01 * rangeI)
    ax.tick_params(axis='both', which='both', direction='in', top=True, labelsize=12)
    ax.tick_params(axis='both', grid_linewidth=1, grid_linestyle='solid', grid_alpha=0.5)
    ax.tick_params(axis='both', which='minor')
    ax.grid(True)
    ax.set_xlabel('t (s)', fontsize=12)
    ax.set_ylabel(r'$i_1, i_2\ (A)$', fontsize=12)

    ax1   = ax.twinx()
    yvals = R * (I.y[1] - I.y[0])  # Vc = R*(i2 - i1)? Actually Vc = R*i2, but per original code: R*(i1-i2)
    # keeping original formula from provided code: R*(I.y[1]-I.y[0])
    yrange = abs(max(yvals) - min(yvals))
    ax1.plot(tList, yvals, linestyle='dotted', color='k', label=r'$v_c(t)$')
    ax1.set_ylim(min(yvals) - yrange * 0.01, max(yvals) + yrange * 0.01)
    ax1.tick_params(axis='y', which='both', direction='in', top=True, right=True, labelsize=12)
    ax.legend(fontsize=12)
    ax1.legend(loc='lower right', fontsize=12)
    ax1.set_ylabel(r'$V_c(t)\ (V)$', fontsize=12)

    if not QTPlotting:
        plt.show()

def main():
    I = simulate(L=20, R=10, C=0.05, A=20, f=20/(2*math.pi), p=0, t=10, pts=500)
    doPlot((10, I.t, I))

# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion
