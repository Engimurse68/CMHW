# region imports
from Fluid import Fluid
from Pipe  import Pipe
from Loop  import Loop
from PipeNetwork import PipeNetwork
# endregion

# region function definitions
def main():
    '''
    Analyzes flows in the pipe network for Exam 2 using object oriented programming.
    Same Approach as HW 6:
      Step 1: build a PipeNetwork object containing Pipe, Node, Loop, and Fluid objects
      Step 2: calculate flow rates using fsolve (KCL at nodes + KVL around loops)
      Step 3: output results
      Step 4: check results — zero head loss per loop, mass conservation at nodes

    Network notes:
      - 12" and 16" pipes: cast iron, roughness = 0.00085 ft
      - 18" and 24" pipes: concrete,  roughness = 0.003   ft
      - Fluid: room-temperature water, mu=20.50e-6 lb·s/ft², rho=62.3/32.174 slug/ft³
      - External flows: h=+10 cfs (in), d=-2 cfs (out), e=-3 cfs (out), f=-5 cfs (out)
      - Known pressure: node h = 80 psi
    '''
    # define the fluid (imperial units: rho in slug/ft³, mu in lb·s/ft²)
    water = Fluid(mu=20.50e-6, rho=62.3/32.174)

    # roughness values in ft
    r_ci  = 0.00085   # cast iron  (12" and 16" pipes)
    r_con = 0.003     # concrete   (18" and 24" pipes)

    # instantiate a PipeNetwork object
    PN = PipeNetwork()

    # add Pipe objects: Pipe(start, end, length_ft, diam_in, roughness_ft, fluid)
    # top horizontal row
    PN.pipes.append(Pipe('a', 'b', 1000, 18, r_con, water))
    PN.pipes.append(Pipe('b', 'c',  500, 18, r_con, water))
    PN.pipes.append(Pipe('c', 'd',  500, 18, r_con, water))
    # left vertical
    PN.pipes.append(Pipe('a', 'h', 1600, 24, r_con, water))
    # middle verticals
    PN.pipes.append(Pipe('b', 'e',  800, 16, r_ci,  water))
    PN.pipes.append(Pipe('c', 'f',  800, 16, r_ci,  water))
    PN.pipes.append(Pipe('d', 'g',  800, 16, r_ci,  water))
    # middle horizontal row
    PN.pipes.append(Pipe('e', 'f',  500, 12, r_ci,  water))
    PN.pipes.append(Pipe('f', 'g',  500, 12, r_ci,  water))
    # lower verticals
    PN.pipes.append(Pipe('e', 'i',  800, 18, r_con, water))
    PN.pipes.append(Pipe('g', 'j',  800, 18, r_con, water))
    # bottom horizontal row
    PN.pipes.append(Pipe('h', 'i', 1000, 24, r_con, water))
    PN.pipes.append(Pipe('i', 'j', 1000, 24, r_con, water))

    # build Node objects from the pipe endpoints
    PN.buildNodes()

    # set external flows at source/demand nodes (cfs, positive = into network)
    PN.getNode('h').extFlow = +10.0   # 10 cfs source
    PN.getNode('d').extFlow =  -2.0   # 2 cfs demand
    PN.getNode('e').extFlow =  -3.0   # 3 cfs demand
    PN.getNode('f').extFlow =  -5.0   # 5 cfs demand

    # add Loop objects (pipes listed in traversal order, CW)
    # Loop A: a→b→e→i→h→a  (left large loop)
    PN.loops.append(Loop('A', [PN.getPipe('a-b'), PN.getPipe('b-e'),
                                PN.getPipe('e-i'), PN.getPipe('h-i'), PN.getPipe('a-h')]))
    # Loop B: b→c→f→e→b  (top-middle loop)
    PN.loops.append(Loop('B', [PN.getPipe('b-c'), PN.getPipe('c-f'),
                                PN.getPipe('e-f'), PN.getPipe('b-e')]))
    # Loop C: c→d→g→f→c  (top-right loop)
    PN.loops.append(Loop('C', [PN.getPipe('c-d'), PN.getPipe('d-g'),
                                PN.getPipe('f-g'), PN.getPipe('c-f')]))
    # Loop D: e→f→g→j→i→e  (bottom-right loop)
    PN.loops.append(Loop('D', [PN.getPipe('e-f'), PN.getPipe('f-g'),
                                PN.getPipe('g-j'), PN.getPipe('i-j'), PN.getPipe('e-i')]))

    # solve for flow rates using fsolve
    PN.findFlowRates()

    # output results
    PN.printPipeFlowRates()
    print()
    print('Check node flows:')
    PN.printNetNodeFlows()
    print()
    print('Check loop head loss:')
    PN.printLoopHeadLoss()
    print()
    print('Head loss in each pipe (inches of water):')
    PN.printPipeHeadLosses()
    print()
    print('Node pressures (node h = 80.00 psi):')
    PN.printNodePressures('h', 80.0)
# endregion

# region function calls
if __name__ == '__main__':
    main()
# endregion
