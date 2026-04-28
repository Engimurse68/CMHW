# region imports
from scipy.optimize import fsolve
import numpy as np
from Fluid import Fluid
from Node import Node
# endregion

# region class definitions
class PipeNetwork():
    # region constructor
    def __init__(self, Pipes=[], Loops=[], Nodes=[], fluid=Fluid()):
        '''
        Pipe network built from pipe, node, loop, and fluid objects.
        Unchanged from HW6
        '''
        self.loops  = Loops
        self.nodes  = Nodes
        self.Fluid  = fluid
        self.pipes  = Pipes
    # endregion

    # region methods
    def findFlowRates(self):
        '''
        Finds flow rates in each pipe using fsolve.
        Constraints: i) no net flow into any node (KCL),
                    ii) no net head loss around any loop (KVL).
        Unchanged from HW6
        '''
        N  = len(self.nodes) + len(self.loops)
        Q0 = np.full(N, 1.0)   # initial guess: 1 cfs in each pipe

        def fn(q):
            for i in range(len(self.pipes)):
                self.pipes[i].Q = q[i]
            L  = self.getNodeFlowRates()
            L += self.getLoopHeadLosses()
            return L

        FR = fsolve(fn, Q0)
        return FR

    def getNodeFlowRates(self):
        return [n.getNetFlowRate() for n in self.nodes]

    def getLoopHeadLosses(self):
        return [l.getLoopHeadLoss() for l in self.loops]

    def getPipe(self, name):
        for p in self.pipes:
            if name == p.Name():
                return p

    def getNodePipes(self, node):
        return [p for p in self.pipes if p.oContainsNode(node)]

    def nodeBuilt(self, node):
        return any(n.name == node for n in self.nodes)

    def getNode(self, name):
        for n in self.nodes:
            if n.name == name:
                return n

    def buildNodes(self):
        for p in self.pipes:
            if not self.nodeBuilt(p.startNode):
                self.nodes.append(Node(p.startNode, self.getNodePipes(p.startNode)))
            if not self.nodeBuilt(p.endNode):
                self.nodes.append(Node(p.endNode, self.getNodePipes(p.endNode)))

    def printPipeFlowRates(self):
        for p in self.pipes:
            p.printPipeFlowRate()

    def printNetNodeFlows(self):
        for n in self.nodes:
            print('net flow into node {} is {:0.2f} (cfs)'.format(
                n.name, n.getNetFlowRate()))

    def printLoopHeadLoss(self):
        for l in self.loops:
            print('head loss for loop {} is {:0.2f} (psi)'.format(
                l.name, l.getLoopHeadLoss() * 62.3 / 144.0))

    def printPipeHeadLosses(self):
        for p in self.pipes:
            print('head loss in pipe {} (L={:.0f} ft, d={:.0f} in) is {:.2f} in of water'.format(
                p.Name(), p.length, p.diam_in, p.frictionHeadLoss() * 12.0))

    def printNodePressures(self, known_node, known_psi, gamma=62.3):
        from collections import deque
        pressures = {known_node: known_psi}
        adj = {}
        for p in self.pipes:
            adj.setdefault(p.startNode, []).append((p.endNode, p, +1))
            adj.setdefault(p.endNode,   []).append((p.startNode, p, -1))
        queue = deque([known_node])
        visited = {known_node}
        while queue:
            node = queue.popleft()
            for neighbor, p, sign in adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    pressures[neighbor] = (pressures[node]
                                           - sign * p.getFlowHeadLoss(node if sign == 1 else neighbor)
                                           * gamma / 144.0)
                    queue.append(neighbor)
        for name in sorted(pressures):
            print('Pressure at node {} = {:.2f} psi'.format(name, pressures[name]))
    # endregion
# endregion
