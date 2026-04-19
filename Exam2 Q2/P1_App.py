#region imports
from PySide6.QtWidgets import QApplication, QWidget
from P1_GUI import Ui_MainForm  # I was having DLL issues with PyQt5.  Claude.ai helped me change everything to PySide6.
# This is the fix I used for Homework 7 that I completed and left in my repository, but forgot to submit on Canvas
import sys
from Circuit_Classes import circuitController

#these imports are necessary for drawing a matplot lib graph on my GUI
#no simple widget for this exists in QT Designer, so I have to add the widget in code.
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
#endregion

#region class definitions
class main_window(Ui_MainForm, QWidget):
    def __init__(self):
        """
        Constructor for circuit simulator.
        """
        super().__init__()
        self.setupUi(self)
        # you should modify the window title appropriately

        self.inputWidgets = (self.le_Inductance, self.le_Resistance, self.le_Capacitence, self.le_Amplitude, self.le_Freq, self.le_Phase, self.le_simTime, self.le_simPts)
        self.displayWidgets = (self.layout_VertMain, self.layout_VertInput, self)
        self.controller = circuitController((self.inputWidgets,self.displayWidgets))
        self.setupSignalsAndSlots()
        self.show()


    def setupSignalsAndSlots(self):
        """
        Connect the push button to the calculate function.
        :return:
        """
        self.pb_Calculate.clicked.connect(self.calculate)
        pass

    def calculate(self):
        self.controller.calculate()

#endregion

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec())