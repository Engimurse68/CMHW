# region imports
import math
import numpy as np
from scipy.optimize import fsolve
from Fluid import Fluid
# endregion

# region class definitions
class Pipe():
    # region constructor
    def __init__(self, Start='A', End='B', L=100, D=18, r=0.003, fluid=Fluid()):
        '''
        Defines a pipe with orientation from lowest letter to highest, alphabetically.
        Adapted from HW6 for imperial units (ft, inches, cfs, lb·s/ft²).
        :param Start:  start node (string)
        :param End:    end node (string)
        :param L:      pipe length in ft (float)
        :param D:      pipe diameter in inches (float)
        :param r:      pipe roughness in ft (float)
        :param fluid:  a Fluid object  (rho in slug/ft³, mu in lb·s/ft²)
        '''
        # region attributes
        self.startNode = min(Start, End)   # alphabetically lower node
        self.endNode   = max(Start, End)   # alphabetically higher node
        self.length    = L                 # ft
        self.r         = r                 # roughness, ft
        self.fluid     = fluid

        self.d         = D / 12.0          # diameter in ft
        self.diam_in   = D                 # diameter in inches (for reporting)
        self.relrough  = self.r / self.d   # relative roughness
        self.A         = math.pi / 4.0 * self.d ** 2  # cross-sectional area, ft²
        self.Q         = 1.0              # initial guess, cfs
        self.vel       = self.V()
        self.reynolds  = self.Re()
        # endregion
    # endregion

    # region methods
    def V(self):
        '''Average velocity in ft/s for current Q (cfs).'''
        self.vel = abs(self.Q) / self.A
        return self.vel

    def Re(self):
        '''Reynolds number: Re = rho * V * d / mu'''
        self.reynolds = self.fluid.rho * self.V() * self.d / self.fluid.mu
        return self.reynolds

    def FrictionFactor(self):
        '''
        Darcy friction factor via Colebrook-White for turbulent flow,
        64/Re for laminar.
        '''
        Re  = self.Re()
        rr  = self.relrough

        def CB():
            cb     = lambda f: 1 / f**0.5 + 2.0 * np.log10(rr / 3.7 + 2.51 / (Re * f**0.5))
            result = fsolve(cb, 0.02)
            return result[0]

        def lam():
            return 64.0 / Re

        if Re >= 4000:
            return CB()
        if Re <= 2000:
            return lam()
        # transitional: linear blend (removed random:  suggestion from Claude.ai)
        CBff  = CB()
        Lamff = lam()
        return Lamff + ((Re - 2000) / (4000 - 2000)) * (CBff - Lamff)

    def frictionHeadLoss(self):
        '''
        Darcy-Weisbach head loss magnitude in ft of fluid.
        h_L = f * (L/d) * V² / (2g)
        '''
        g  = 32.174   # ft/s²
        ff = self.FrictionFactor()
        return ff * (self.length / self.d) * (self.V() ** 2) / (2.0 * g)

    def getFlowHeadLoss(self, s):
        '''
        Signed head loss for loop traversal (mirrors HW6 exactly).
        :param s: the node I'm starting from in the traversal
        :return:  signed head loss in ft of fluid
        '''
        nTraverse = 1 if s == self.startNode else -1
        nFlow     = 1 if self.Q >= 0         else -1
        return nTraverse * nFlow * self.frictionHeadLoss()

    def Name(self):
        return self.startNode + '-' + self.endNode

    def oContainsNode(self, node):
        return self.startNode == node or self.endNode == node

    def printPipeFlowRate(self):
        print('The flow in segment {} is {:0.2f} (cfs) and Re={:,.1f}'.format(
            self.Name(), self.Q, self.Re()))

    def getFlowIntoNode(self, n):
        '''Returns +Q if flow is into node n, -Q if out of node n.'''
        if n == self.startNode:
            return -self.Q
        return self.Q
    # endregion
# endregion
