#The end is nigh!#
"""Take-off Distance Calcumalator Thing-a-ma-jig"""

#Importifications#

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import scipy.integrate as integrate
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Making the model, AKA Project Runway

class TakeoffModel:
    """Problems and definitions as listed"""

    #Constants in English units\
    CL_MAX = 2.4
    CD     = 0.0279
    Rho    = 0.002377  # slug/ft^3
    S      = 1000      # ft^2
    GC     = 32.2    # lbft / (lbfs^2)

    def compute_sto(self, thrust, weight):
        v_stall = np.sqrt(weight/(0.5*self.Rho*self.S*self.CL_MAX))
        v_to    = 1.2*v_stall

        A = self.GC*(thrust/weight)
        B = (self.GC/weight)*(0.5*self.Rho*self.S*self.CD)

        integrand = lambda v: v/(A-B*v**2)

        # You're going nowhere
        if A - B*v_to**2 <= 0:
            return "You are grounded, mister!"

        s_to, _ = quad(integrand, 0, v_to)
        return s_to

    def compute_curve(self, weight, thrust_array):
        """Return S_TO array over a range of thrusts for a given weight"""
        result = []
        for t in thrust_array:
            val = self.compute_sto(t, weight)
            result.append(np.inf if val == "You are grounded, mister!" else val)
        return np.array(result)

#Look at that view

class TakeoffView:
    """tkinter management"""

    def __init__(self, root):
        self.root = root
        self.root.title("Takeoff Distance Calcumalator Thing-a-ma-jig")
        self.root.resizable(True, True)
        self._build_input_frame()
        self._build_plot_frame()

    def _build_input_frame(self):
        frame = ttk.LabelFrame(self.root, text="Parameters", padding=10)
        frame.pack(side = tk.TOP, fill=tk.X, padx=10, pady=5)

        # Weight a sec
        ttk.Label(frame, text="Weight (lbf):").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.weight_var = tk.StringVar(value="56000")
        self.weight_entry = ttk.Entry(frame, textvariable=self.weight_var, width=12)
        self.weight_entry.grid(row=0, column=1, padx=5)

        # Thrust
        ttk.Label(frame, text="Thrust (lbf):").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.thrust_var = tk.StringVar(value="13000")
        self.thrust_entry = ttk.Entry(frame, textvariable=self.thrust_var, width=12)
        self.thrust_entry.grid(row=0, column=3, padx=5)

        # Calculate button
        self.calc_button = ttk.Button(frame, text="Calculate")
        self.calc_button.grid(row=0, column=4, padx=15)

    def _build_plot_frame(self):
        frame = ttk.Frame(self.root, padding=5)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(7, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def get_inputs(self):
        """weight, thrust as floats. Raises ValueError if bad."""
        weight = float(self.weight_var.get())
        thrust = float(self.thrust_var.get())
        return weight, thrust

    def update_plot(self, thrust_range, curves, weight, thrust, sto_center):
        """
        Re-draw the plot.
        curves = dict: label -> (thrust_array, sto_array)
        sto_center = S_TO at the specified weight/thrust (for the circle marker)
        """
        self.ax.clear()

        colors = {
            "W - 10,000": "blue",
            "W (specified)": "red",
            "W + 10,000": "green",
        }

        for label, (t_arr, s_arr) in curves.items():
            # Filter out inf values
            mask = np.isfinite(s_arr)
            self.ax.plot(t_arr[mask], s_arr[mask],
                         label=label, color=colors.get(label, "gray"), linewidth=2)

        # Circle marker at specified thrust & weight
        if isinstance(sto_center, (int, float)) and np.isfinite(sto_center):
            self.ax.plot(thrust, sto_center, 'o', markersize=10,
                         color='crimson', zorder=5, label=f"S_TO = {sto_center:.1f} ft")

        self.ax.set_xlabel("Thrust (lbf)", fontsize=11)
        self.ax.set_ylabel("S_TO (ft)", fontsize=11)
        self.ax.set_title("Takeoff Distance vs. Engine Thrust", fontsize=12)
        self.ax.legend(fontsize=9)
        self.ax.grid(True, linestyle='--', alpha=0.5)
        self.fig.tight_layout()
        self.canvas.draw()

    def show_error(self, msg):
        messagebox.showerror("Yeah, that won't work", msg)


#(XBox)CONTROLLER

class TakeoffController:
    "The blessed union of Model and View"

    THRUST_MIN = 5000
    THRUST_MAX = 35000
    N_POINTS = 300

    def __init__(self, root):
        self.model = TakeoffModel()
        self.view = TakeoffView(root)
        self.view.calc_button.config(command=self.on_calculate)

    def on_calculate(self):
        try:
            weight, thrust = self.view.get_inputs()
        except ValueError:
            self.view.show_error("Put some numbers in those boxes.")
            return

        if weight <= 0 or thrust <= 0:
            self.view.show_error("Don't be so negative.")
            return

        thrust_array = np.linspace(self.THRUST_MIN, self.THRUST_MAX, self.N_POINTS)

        curves = {
            "W - 10,000": (thrust_array, self.model.compute_curve(weight - 10000, thrust_array)),
            "W (specified)": (thrust_array, self.model.compute_curve(weight, thrust_array)),
            "W + 10,000": (thrust_array, self.model.compute_curve(weight + 10000, thrust_array)),
        }

        sto_center = self.model.compute_sto(thrust, weight)
        print(f"sto_center = {sto_center}, type = {type(sto_center)}")  # temp debug
        if sto_center == "grounded":
            self.view.show_error("You are grounded! Thrust is too low to achieve takeoff speed.")
            return

        self.view.update_plot(thrust_array, curves, weight, thrust, sto_center)


#The end
if __name__ == "__main__":
    root = tk.Tk()
    app = TakeoffController(root)
    root.mainloop()
