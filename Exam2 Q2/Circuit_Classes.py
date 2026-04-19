# region imports
#As noted in P1_App.py, I tried to trouble shoot the DLL issues with PyQt5, but it was much easier to just change
#to PySide6
from X2Q2_SP24 import doPlot, simulate
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
# endregion

# region RLC circuit classes (MVC)
class circuitModel():
    def __init__(self):
        self.nodes         = []
        self.resistors     = []
        self.capacitors    = []
        self.inductors     = []
        self.voltageSources = []
        self.wires         = []


class circuitView():
    def __init__(self, dw=None):
        if dw is not None:
            self.setDisplayWidgets(dw)
            self.setupImageLabel()
            self.setupPlot()

    def setDisplayWidgets(self, dw=None):
        if dw is not None:
            # unpacked the three display widgets passed from P1_App.py
            # into named attributes so the rest of the view methods can reference them
            self.layout_VertMain, self.layout_VertInput, self.form = dw

    def setupImageLabel(self):
        """
        Displays picture of circuit from Circuit1.png in a label widget.
        """
        self.pixMap = qtg.QPixmap()          # instantiated a QPixmap object
        self.pixMap.load("Circuit1.png")
        self.image_label = qtw.QLabel()      # instantiated a QLabel object
        self.image_label.setPixmap(self.pixMap)
        self.layout_VertInput.addWidget(self.image_label)

    def setupPlot(self):
        """
        Create figure, canvas, axes, and toolbar and place them on the GUI.
        """
        self.figure  = Figure(figsize=(8, 8), tight_layout=True, frameon=True, facecolor='none')
        self.canvas  = FigureCanvasQTAgg(self.figure)
        self.ax      = self.figure.add_subplot()
        self.toolbar = NavigationToolbar2QT(self.canvas, self.form)
        self.layout_VertMain.addWidget(self.toolbar)
        self.layout_VertMain.addWidget(self.canvas)

    def doPlot(self, args):
        self.canvas.figure.clear()
        self.ax = self.figure.add_subplot()
        doPlot(args, ax=self.ax)
        self.canvas.draw()


class circuitController():
    def __init__(self, args):
        """
        Controller for the RLC circuit MVC.
        :param args: tuple of (inputWidgets, displayWidgets)
        """
        self.inputWidgets, self.displayWidgets = args

        # unpacked input widgets — order matches P1_App.py:
        (self.le_Inductance, self.le_Resistance, self.le_Capacitence,
         self.le_Amplitude,  self.le_Freq,       self.le_Phase,
         self.le_simTime,    self.le_simPts) = self.inputWidgets

        self.Model = circuitModel()
        self.View  = circuitView(dw=self.displayWidgets)

    def calculate(self):
        """
        Reads inputs from GUI, runs simulation, and updates the plot.
        """
        L   = float(self.le_Inductance.text())
        R   = float(self.le_Resistance.text())
        C   = float(self.le_Capacitence.text())
        A   = float(self.le_Amplitude.text())
        f   = float(self.le_Freq.text())
        p   = float(self.le_Phase.text())
        t   = float(self.le_simTime.text())
        pts = float(self.le_simPts.text())
    #Called with keyword arguments matching X2Q2 parameter names
        I = simulate(L=L, R=R, C=C, A=A, f=f, p=p, t=t, pts=pts)
        self.View.doPlot((R, I.t, I))

# endregion
