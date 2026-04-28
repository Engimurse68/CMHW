# region class definitions
class Loop():
    # region constructor
    def __init__(self, Name='A', Pipes=[]):
        '''
        Defines a loop in a pipe network.  Pipes must be listed in order around
        the loop.  Traversal begins at startNode of Pipes[0].
        :param Name:  name of the loop
        :param Pipes: ordered list of pipe objects in this loop
        '''
        self.name  = Name
        self.pipes = Pipes
    # endregion

    # region methods
    def getLoopHeadLoss(self):
        '''
        Net head loss traversing around the loop in ft of fluid.
        '''
        deltaP    = 0
        startNode = self.pipes[0].startNode
        for p in self.pipes:
            deltaP   += p.getFlowHeadLoss(startNode)
            startNode = p.endNode if startNode != p.endNode else p.startNode
        return deltaP
    # endregion
# endregion
