# prob3.py
"""
Problem 3: RLC Circuit Simulation
===================================
Simulates an RLC circuit using solve_ivp and plots the currents i1, i2
and voltage across the capacitor v_c for 10 seconds.

State equations:
  di1/dt  = (v(t) - v_c) / L
  dv_c/dt = (i1 - v_c/R) / C
  i2      = v_c / R

Default values: R=10Ω, L=20H, C=0.05F, v(t)=20·sin(20·t+0)
"""

#region imports
import math
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
#endregion

#region circuit class
class circuit:
    def __init__(self, R=10, L=20, C=0.05, amplitude=20, frequency=20, phase=0):
        """
        Initializes the RLC circuit with given parameters.
        :param R: resistance in ohms (default 10)
        :param L: inductance in henries (default 20)
        :param C: capacitance in farads (default 0.05)
        :param amplitude: amplitude of v(t) in volts (default 20)
        :param frequency: frequency of v(t) in rad/s (default 20)
        :param phase: phase of v(t) in radians (default 0)
        """
        self.R = R
        self.L = L
        self.C = C
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase

    def v(self, t):
        """
        Computes the source voltage at time t.
        v(t) = amplitude * sin(frequency * t + phase)
        :param t: time in seconds
        :return: voltage (float)
        """
        return self.amplitude * math.sin(self.frequency * t + self.phase)

    def ode_system(self, t, y):
        """
        Defines the system of ODEs for the RLC circuit in state form.
        :param t: current time (float)
        :param y: state vector [i1, v_c]
        :return: derivatives [di1/dt, dv_c/dt]
        """
        i1  = y[0]
        v_c = y[1]
        di1_dt = (self.v(t) - v_c) / self.L
        dvc_dt = (i1 - v_c / self.R) / self.C
        return [di1_dt, dvc_dt]

    def simulate(self, t_end=10, t_steps=1000):
        """
        Solves the ODE system using solve_ivp from t=0 to t=t_end.
        Initial conditions: i1(0)=0, v_c(0)=0
        :param t_end: end time in seconds (default 10)
        :param t_steps: number of time points to evaluate (default 1000)
        :return: (t, i1, i2, v_c) as numpy arrays
        """
        t_span = (0, t_end)
        t_eval = np.linspace(0, t_end, t_steps)
        y0 = [0, 0]
        sol = solve_ivp(self.ode_system, t_span, y0, t_eval=t_eval, method='RK45')
        t   = sol.t
        i1  = sol.y[0]
        v_c = sol.y[1]
        i2  = v_c / self.R
        return t, i1, i2, v_c

    def doPlot(self, t, i1, i2, v_c):
        """
        Plots i1 and i2 on the left y-axis and v_c on the right y-axis.
        :param t:   time array (seconds)
        :param i1:  current through inductor (A)
        :param i2:  current through resistor (A)
        :param v_c: voltage across capacitor (V)
        """
        fig, ax1 = plt.subplots()

        # Left y-axis: i1 (solid) and i2 (dashed)
        ax1.plot(t, i1, '-k', linewidth=1.0, label=r'$i_1(t)$')
        ax1.plot(t, i2, '--k', linewidth=1.0, label=r'$i_2(t)$')
        ax1.set_xlabel('t (s)')
        ax1.set_ylabel(r'i_1, i_2 (A)')
        ax1.tick_params(axis='y', direction='in')
        ax1.tick_params(axis='x', direction='in')

        # Right y-axis: v_c (dotted)
        ax2 = ax1.twinx()
        ax2.plot(t, v_c, ':', color='black', linewidth=1.0, label=r'$v_c(t)$')
        ax2.set_ylabel(r'$V_c(t)$ (V)')
        ax2.tick_params(axis='y', direction='in')

        # Combined legend from both axes
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

        plt.title('RLC Circuit Simulation')
        plt.tight_layout()
        plt.show()
#endregion

#region CLI input
def get_parameters(defaults):
    """
    Requests user input for circuit parameters, or user can utilize defaults.
    :param defaults: dict of current parameter values
    :return: dict of updated parameter values
    """
    print("\n--- Circuit Parameters (press Enter to keep default) ---")

    def prompt(label, key, fmt='.2f'):
        val = input(f"  {label} ({defaults[key]:{fmt}}): ").strip()
        return defaults[key] if val == '' else float(val)

    return {
        'R':         prompt('Resistance R (ohms)',       'R'),
        'L':         prompt('Inductance L (henries)',    'L'),
        'C':         prompt('Capacitance C (farads)',    'C'),
        'amplitude': prompt('Amplitude of v(t) (volts)', 'amplitude'),
        'frequency': prompt('Frequency of v(t) (rad/s)', 'frequency'),
        'phase':     prompt('Phase of v(t) (radians)',   'phase'),
    }
#endregion

#region main
def main():
    """
    Main function: prompts user for circuit parameters, simulates the RLC
    circuit, plots the results, and asks if the user wants to run again.

    Steps:
      1. Get circuit parameters from user
      2. Create circuit object and simulate
      3. Plot results
      4. Ask user to run again with new parameters
    """
    print("\n" + "="*50)
    print("  RLC Circuit Simulation")
    print("="*50)

    # Default parameters
    params = {
        'R': 10, 'L': 20, 'C': 0.05,
        'amplitude': 20, 'frequency': 20, 'phase': 0
    }

    go_again = True
    while go_again:
        # Step 1: get parameters from user
        params = get_parameters(params)

        # Step 2: create circuit and simulate
        c = circuit(
            R=params['R'], L=params['L'], C=params['C'],
            amplitude=params['amplitude'],
            frequency=params['frequency'],
            phase=params['phase']
        )
        print("\nSimulating...")
        t, i1, i2, v_c = c.simulate()
        print("Done. Close the plot window to continue.")

        # Step 3: plot
        c.doPlot(t, i1, i2, v_c)

        # Step 4: ask to run again
        go_again = input("\nSimulate with new parameters? (y/N): ").strip().lower() == 'y'
#endregion


main()