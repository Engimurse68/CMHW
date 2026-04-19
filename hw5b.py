# region imports
import hw5a as pta
import random as rnd
from matplotlib import pyplot as plt
import numpy as np
# endregion

# region functions
def ffPoint(Re, rr):
    """
    This function takes Re and rr as parameters and outputs a friction factor according to the following:
    1.  if Re>4000 use Colebrook Equation
    2.  if Re<2000 use f=64/Re
    3.  else calculate a probabilistic friction factor where the distribution has a mean midway between the prediction
        of the f=64/Re and Colebrook Equations and a standard deviation of 20% of this mean
    :param Re:  the Reynolds number
    :param rr:  the relative roughness
    :return:  the friction factor
    """
    if Re>=4000:
        return pta.ff(Re, rr,CBEQN=True)
    if Re<=2000:
        return pta.ff(Re, rr)
    CBff= pta.ff(RE, rr, CBEQN=True)  #prediction of Colebrook Equation in Transition region
    Lamff= pta.ff(Re, rr)  #prediction of Laminar Equation in Transistion region
    mean=Lamff + (CBff - Lamff) * (Re - 2000) / 2000 #I changed this because the directions say that this is the formula for the mean
    sig=0.2*mean
    return rnd.normalvariate(mean, sig)  #use normalvariate to select a number randomly from a normal distribution

def PlotPoint(Re,f):
    pta.plotMoody(plotPoint=True, pt=(Re,f))

def main():
    # region constants
    nu = 1.21e-5        # kinematic viscosity of water in ft^2/s
    g = 32.2            # acceleration of gravity in ft/s^2
    # endregion

    again = True
    while again:
        # get user inputs
        d_in = float(input("Enter pipe diameter (inches): "))
        eps_mics = float(input("Enter pipe roughness (micro-inches): "))
        Q_gpm = float(input("Enter flow rate (gallons/min): "))

        # unit conversions
        d = d_in / 12                    # inches to feet
        eps = eps_mics / (12 * 1e6)      # micro-inches to feet
        Q = Q_gpm * 0.002228             # gallons/min to ft^3/s

        # calculate Re and rr
        A = np.pi / 4 * d**2             # pipe cross sectional area in ft^2
        V = Q / A                        # average velocity in ft/s
        Re = V * d / nu                  # Reynolds number
        rr = eps / d                     # relative roughness

        # calculate friction factor and head loss
        f = ffPoint(Re, rr)
        hfL = f * V**2 / (2 * g * d)    # head loss per foot in ft/ft

        print(f"Re = {Re:.0f}")
        print(f"Relative roughness = {rr:.6f}")
        print(f"Friction factor = {f:.4f}")
        print(f"Head loss per foot = {hfL:.4f} ft/ft")

        # plot the point on the Moody diagram
        PlotPoint(Re, f)

        # ask if user wants to go again
        again = input("Go again? (y/n): ").lower() == 'y'

# region function calls
if __name__=="__main__":
    main()
# endregion