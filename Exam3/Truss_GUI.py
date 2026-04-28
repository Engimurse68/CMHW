# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Truss_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_TrussStructuralDesign(object):
    def setupUi(self, TrussStructuralDesign):
        if not TrussStructuralDesign.objectName():
            TrussStructuralDesign.setObjectName(u"TrussStructuralDesign")
        TrussStructuralDesign.resize(1060, 1161)
        self.verticalLayout = QVBoxLayout(TrussStructuralDesign)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grp_Load = QGroupBox(TrussStructuralDesign)
        self.grp_Load.setObjectName(u"grp_Load")
        self.horizontalLayout = QHBoxLayout(self.grp_Load)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_Open = QPushButton(self.grp_Load)
        self.btn_Open.setObjectName(u"btn_Open")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Open.sizePolicy().hasHeightForWidth())
        self.btn_Open.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_Open, 0, Qt.AlignTop)

        self.te_Path = QTextEdit(self.grp_Load)
        self.te_Path.setObjectName(u"te_Path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_Path.sizePolicy().hasHeightForWidth())
        self.te_Path.setSizePolicy(sizePolicy1)
        self.te_Path.setMinimumSize(QSize(700, 50))
        self.te_Path.setMaximumSize(QSize(1000, 100))
        self.te_Path.setBaseSize(QSize(500, 0))

        self.horizontalLayout.addWidget(self.te_Path)


        self.verticalLayout.addWidget(self.grp_Load)

        self.grp_DesignReport = QGroupBox(TrussStructuralDesign)
        self.grp_DesignReport.setObjectName(u"grp_DesignReport")
        self.horizontalLayout_2 = QHBoxLayout(self.grp_DesignReport)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.te_DesignReport = QTextEdit(self.grp_DesignReport)
        self.te_DesignReport.setObjectName(u"te_DesignReport")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.te_DesignReport.sizePolicy().hasHeightForWidth())
        self.te_DesignReport.setSizePolicy(sizePolicy2)
        self.te_DesignReport.setMinimumSize(QSize(300, 300))
        self.te_DesignReport.setMaximumSize(QSize(1000, 700))

        self.horizontalLayout_2.addWidget(self.te_DesignReport)

        self.grp_LongestLink = QGroupBox(self.grp_DesignReport)
        self.grp_LongestLink.setObjectName(u"grp_LongestLink")
        sizePolicy.setHeightForWidth(self.grp_LongestLink.sizePolicy().hasHeightForWidth())
        self.grp_LongestLink.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.grp_LongestLink)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_Node1Name = QLabel(self.grp_LongestLink)
        self.lbl_Node1Name.setObjectName(u"lbl_Node1Name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_Node1Name.sizePolicy().hasHeightForWidth())
        self.lbl_Node1Name.setSizePolicy(sizePolicy3)
        self.lbl_Node1Name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_Node1Name, 1, 0, 1, 1, Qt.AlignRight)

        self.le_Node1Name = QLineEdit(self.grp_LongestLink)
        self.le_Node1Name.setObjectName(u"le_Node1Name")
        sizePolicy.setHeightForWidth(self.le_Node1Name.sizePolicy().hasHeightForWidth())
        self.le_Node1Name.setSizePolicy(sizePolicy)
        self.le_Node1Name.setMinimumSize(QSize(50, 0))
        self.le_Node1Name.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.le_Node1Name, 1, 1, 1, 1)

        self.lbl_LinkName = QLabel(self.grp_LongestLink)
        self.lbl_LinkName.setObjectName(u"lbl_LinkName")
        sizePolicy3.setHeightForWidth(self.lbl_LinkName.sizePolicy().hasHeightForWidth())
        self.lbl_LinkName.setSizePolicy(sizePolicy3)
        self.lbl_LinkName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_LinkName, 0, 0, 1, 1, Qt.AlignRight)

        self.le_LinkLength = QLineEdit(self.grp_LongestLink)
        self.le_LinkLength.setObjectName(u"le_LinkLength")
        sizePolicy.setHeightForWidth(self.le_LinkLength.sizePolicy().hasHeightForWidth())
        self.le_LinkLength.setSizePolicy(sizePolicy)
        self.le_LinkLength.setMinimumSize(QSize(50, 0))
        self.le_LinkLength.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.le_LinkLength, 3, 1, 1, 1)

        self.lbl_LinkLength = QLabel(self.grp_LongestLink)
        self.lbl_LinkLength.setObjectName(u"lbl_LinkLength")
        sizePolicy3.setHeightForWidth(self.lbl_LinkLength.sizePolicy().hasHeightForWidth())
        self.lbl_LinkLength.setSizePolicy(sizePolicy3)
        self.lbl_LinkLength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_LinkLength, 3, 0, 1, 1, Qt.AlignRight)

        self.le_Node2Name = QLineEdit(self.grp_LongestLink)
        self.le_Node2Name.setObjectName(u"le_Node2Name")
        sizePolicy.setHeightForWidth(self.le_Node2Name.sizePolicy().hasHeightForWidth())
        self.le_Node2Name.setSizePolicy(sizePolicy)
        self.le_Node2Name.setMinimumSize(QSize(50, 0))
        self.le_Node2Name.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.le_Node2Name, 2, 1, 1, 1)

        self.le_LinkName = QLineEdit(self.grp_LongestLink)
        self.le_LinkName.setObjectName(u"le_LinkName")
        sizePolicy.setHeightForWidth(self.le_LinkName.sizePolicy().hasHeightForWidth())
        self.le_LinkName.setSizePolicy(sizePolicy)
        self.le_LinkName.setMinimumSize(QSize(50, 0))
        self.le_LinkName.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.le_LinkName, 0, 1, 1, 1)

        self.lbl_Node2Name = QLabel(self.grp_LongestLink)
        self.lbl_Node2Name.setObjectName(u"lbl_Node2Name")
        sizePolicy3.setHeightForWidth(self.lbl_Node2Name.sizePolicy().hasHeightForWidth())
        self.lbl_Node2Name.setSizePolicy(sizePolicy3)
        self.lbl_Node2Name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_Node2Name, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.grp_LongestLink)


        self.verticalLayout.addWidget(self.grp_DesignReport)

        self.gv_Main = QGraphicsView(TrussStructuralDesign)
        self.gv_Main.setObjectName(u"gv_Main")

        self.verticalLayout.addWidget(self.gv_Main)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_MousePos = QLabel(TrussStructuralDesign)
        self.lbl_MousePos.setObjectName(u"lbl_MousePos")
        sizePolicy3.setHeightForWidth(self.lbl_MousePos.sizePolicy().hasHeightForWidth())
        self.lbl_MousePos.setSizePolicy(sizePolicy3)
        self.lbl_MousePos.setMinimumSize(QSize(500, 0))
        self.lbl_MousePos.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_3.addWidget(self.lbl_MousePos, 0, Qt.AlignLeft)

        self.lbl_Zoom = QLabel(TrussStructuralDesign)
        self.lbl_Zoom.setObjectName(u"lbl_Zoom")
        sizePolicy3.setHeightForWidth(self.lbl_Zoom.sizePolicy().hasHeightForWidth())
        self.lbl_Zoom.setSizePolicy(sizePolicy3)
        self.lbl_Zoom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_Zoom)

        self.spnd_Zoom = QDoubleSpinBox(TrussStructuralDesign)
        self.spnd_Zoom.setObjectName(u"spnd_Zoom")
        sizePolicy.setHeightForWidth(self.spnd_Zoom.sizePolicy().hasHeightForWidth())
        self.spnd_Zoom.setSizePolicy(sizePolicy)
        self.spnd_Zoom.setMinimum(0.250000000000000)
        self.spnd_Zoom.setMaximum(10.000000000000000)
        self.spnd_Zoom.setSingleStep(0.250000000000000)

        self.horizontalLayout_3.addWidget(self.spnd_Zoom)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(TrussStructuralDesign)

        QMetaObject.connectSlotsByName(TrussStructuralDesign)
    # setupUi

    def retranslateUi(self, TrussStructuralDesign):
        TrussStructuralDesign.setWindowTitle(QCoreApplication.translate("TrussStructuralDesign", u"Form", None))
        self.grp_Load.setTitle(QCoreApplication.translate("TrussStructuralDesign", u"Truss File and Load Set", None))
        self.btn_Open.setText(QCoreApplication.translate("TrussStructuralDesign", u"Open and Read a Truss File", None))
        self.grp_DesignReport.setTitle(QCoreApplication.translate("TrussStructuralDesign", u"Design Report", None))
        self.grp_LongestLink.setTitle(QCoreApplication.translate("TrussStructuralDesign", u"LongestLink", None))
        self.lbl_Node1Name.setText(QCoreApplication.translate("TrussStructuralDesign", u"Node 1 Name", None))
        self.lbl_LinkName.setText(QCoreApplication.translate("TrussStructuralDesign", u"Link Name", None))
        self.lbl_LinkLength.setText(QCoreApplication.translate("TrussStructuralDesign", u"Link Length", None))
        self.lbl_Node2Name.setText(QCoreApplication.translate("TrussStructuralDesign", u"Node 2 Name", None))
        self.lbl_MousePos.setText(QCoreApplication.translate("TrussStructuralDesign", u"TextLabel", None))
        self.lbl_Zoom.setText(QCoreApplication.translate("TrussStructuralDesign", u"Zoom", None))
    # retranslateUi

