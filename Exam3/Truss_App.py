#region imports
from Truss_GUI import Ui_TrussStructuralDesign
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from Truss_Classes import TrussController
import sys
#endregion

#region class definitions
class MainWindow(Ui_TrussStructuralDesign, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_Open.clicked.connect(self.OpenFile)
        self.spnd_Zoom.valueChanged.connect(self.setZoom)

        self.controller = TrussController()
        self.controller.setDisplayWidgets((self.te_DesignReport, self.le_LinkName, self.le_Node1Name,
                                           self.le_Node2Name, self.le_LinkLength, self.gv_Main))

        self.gv_Main.setMouseTracking(True)
        self.gv_Main.viewport().setMouseTracking(True)


        self.show()

    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.value())

    def eventFilter(self, obj, event):
        if obj == self.gv_Main.viewport():
            if event.type() == qtc.QEvent.Type.MouseMove:
                pos = event.position().toPoint()
                scenePos = self.gv_Main.mapToScene(pos)
                self.lbl_MousePos.setText("Mouse Position:  x = {}, y = {}".format(
                    round(scenePos.x(), 2), round(-scenePos.y(), 2)))
        return super().eventFilter(obj, event)

    def OpenFile(self):
        filename = qtw.QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:
            return
        self.te_Path.setText(filename)
        file = open(filename, 'r')
        data = file.readlines()
        self.controller.ImportFromFile(data)
#endregion

#region function definitions
def Main():
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
#endregion

#region function calls
if __name__ == "__main__":
    Main()
#endregion