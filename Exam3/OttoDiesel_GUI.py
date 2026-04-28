# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OttoDiesel_GUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1378, 1175)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.main_VerticalLayout = QVBoxLayout(Form)
        self.main_VerticalLayout.setObjectName(u"main_VerticalLayout")
        self.gb_Input = QGroupBox(Form)
        self.gb_Input.setObjectName(u"gb_Input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gb_Input.sizePolicy().hasHeightForWidth())
        self.gb_Input.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.gb_Input.setFont(font)
        self.gridLayout = QGridLayout(self.gb_Input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_P0 = QLabel(self.gb_Input)
        self.lbl_P0.setObjectName(u"lbl_P0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_P0.sizePolicy().hasHeightForWidth())
        self.lbl_P0.setSizePolicy(sizePolicy2)
        self.lbl_P0.setFont(font)

        self.gridLayout.addWidget(self.lbl_P0, 2, 0, 1, 1, Qt.AlignRight)

        self.lbl_TLow = QLabel(self.gb_Input)
        self.lbl_TLow.setObjectName(u"lbl_TLow")
        sizePolicy2.setHeightForWidth(self.lbl_TLow.sizePolicy().hasHeightForWidth())
        self.lbl_TLow.setSizePolicy(sizePolicy2)
        self.lbl_TLow.setFont(font)

        self.gridLayout.addWidget(self.lbl_TLow, 1, 0, 1, 1, Qt.AlignRight)

        self.le_TLow = QLineEdit(self.gb_Input)
        self.le_TLow.setObjectName(u"le_TLow")
        sizePolicy1.setHeightForWidth(self.le_TLow.sizePolicy().hasHeightForWidth())
        self.le_TLow.setSizePolicy(sizePolicy1)
        self.le_TLow.setMaximumSize(QSize(200, 16777215))
        self.le_TLow.setFont(font)
        self.le_TLow.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_TLow, 1, 1, 1, 1)

        self.lbl_V0 = QLabel(self.gb_Input)
        self.lbl_V0.setObjectName(u"lbl_V0")
        sizePolicy2.setHeightForWidth(self.lbl_V0.sizePolicy().hasHeightForWidth())
        self.lbl_V0.setSizePolicy(sizePolicy2)
        self.lbl_V0.setFont(font)

        self.gridLayout.addWidget(self.lbl_V0, 3, 0, 1, 1, Qt.AlignRight)

        self.lbl_THigh = QLabel(self.gb_Input)
        self.lbl_THigh.setObjectName(u"lbl_THigh")
        sizePolicy2.setHeightForWidth(self.lbl_THigh.sizePolicy().hasHeightForWidth())
        self.lbl_THigh.setSizePolicy(sizePolicy2)
        self.lbl_THigh.setFont(font)

        self.gridLayout.addWidget(self.lbl_THigh, 0, 0, 1, 1, Qt.AlignRight)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 4, 1, 1)

        self.le_THigh = QLineEdit(self.gb_Input)
        self.le_THigh.setObjectName(u"le_THigh")
        sizePolicy1.setHeightForWidth(self.le_THigh.sizePolicy().hasHeightForWidth())
        self.le_THigh.setSizePolicy(sizePolicy1)
        self.le_THigh.setMaximumSize(QSize(200, 16777215))
        self.le_THigh.setFont(font)
        self.le_THigh.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_THigh, 0, 1, 1, 1)

        self.le_V0 = QLineEdit(self.gb_Input)
        self.le_V0.setObjectName(u"le_V0")
        sizePolicy1.setHeightForWidth(self.le_V0.sizePolicy().hasHeightForWidth())
        self.le_V0.setSizePolicy(sizePolicy1)
        self.le_V0.setMaximumSize(QSize(200, 16777215))
        self.le_V0.setFont(font)
        self.le_V0.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_V0, 3, 1, 1, 1)

        self.le_P0 = QLineEdit(self.gb_Input)
        self.le_P0.setObjectName(u"le_P0")
        sizePolicy1.setHeightForWidth(self.le_P0.sizePolicy().hasHeightForWidth())
        self.le_P0.setSizePolicy(sizePolicy1)
        self.le_P0.setMaximumSize(QSize(200, 16777215))
        self.le_P0.setFont(font)
        self.le_P0.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_P0, 2, 1, 1, 1)

        self.le_CR = QLineEdit(self.gb_Input)
        self.le_CR.setObjectName(u"le_CR")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.le_CR.sizePolicy().hasHeightForWidth())
        self.le_CR.setSizePolicy(sizePolicy3)
        self.le_CR.setMaximumSize(QSize(200, 16777215))
        self.le_CR.setFont(font)
        self.le_CR.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_CR, 4, 1, 1, 1)

        self.lbl_CR = QLabel(self.gb_Input)
        self.lbl_CR.setObjectName(u"lbl_CR")
        sizePolicy2.setHeightForWidth(self.lbl_CR.sizePolicy().hasHeightForWidth())
        self.lbl_CR.setSizePolicy(sizePolicy2)
        self.lbl_CR.setFont(font)
        self.lbl_CR.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.lbl_CR, 4, 0, 1, 1, Qt.AlignRight)

        self.rdo_English = QRadioButton(self.gb_Input)
        self.rdo_English.setObjectName(u"rdo_English")
        sizePolicy2.setHeightForWidth(self.rdo_English.sizePolicy().hasHeightForWidth())
        self.rdo_English.setSizePolicy(sizePolicy2)
        self.rdo_English.setFont(font)
        self.rdo_English.setChecked(True)

        self.gridLayout.addWidget(self.rdo_English, 3, 3, 1, 1)

        self.rdo_Metric = QRadioButton(self.gb_Input)
        self.rdo_Metric.setObjectName(u"rdo_Metric")
        sizePolicy2.setHeightForWidth(self.rdo_Metric.sizePolicy().hasHeightForWidth())
        self.rdo_Metric.setSizePolicy(sizePolicy2)
        self.rdo_Metric.setFont(font)
        self.rdo_Metric.setChecked(False)

        self.gridLayout.addWidget(self.rdo_Metric, 3, 2, 1, 1)

        self.btn_Calculate = QPushButton(self.gb_Input)
        self.btn_Calculate.setObjectName(u"btn_Calculate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_Calculate.sizePolicy().hasHeightForWidth())
        self.btn_Calculate.setSizePolicy(sizePolicy4)
        self.btn_Calculate.setFont(font)

        self.gridLayout.addWidget(self.btn_Calculate, 4, 2, 1, 2)

        self.cmb_OttoDiesel = QComboBox(self.gb_Input)
        self.cmb_OttoDiesel.addItem("")
        self.cmb_OttoDiesel.addItem("")
        self.cmb_OttoDiesel.addItem("Dual")
        self.cmb_OttoDiesel.setObjectName(u"cmb_OttoDiesel")

        self.gridLayout.addWidget(self.cmb_OttoDiesel, 0, 2, 1, 2)


        self.main_VerticalLayout.addWidget(self.gb_Input)

        self.gb_Output = QGroupBox(Form)
        self.gb_Output.setObjectName(u"gb_Output")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.gb_Output.sizePolicy().hasHeightForWidth())
        self.gb_Output.setSizePolicy(sizePolicy5)
        self.gb_Output.setFont(font)
        self.grid_Output = QGridLayout(self.gb_Output)
        self.grid_Output.setObjectName(u"grid_Output")
        self.label_7 = QLabel(self.gb_Output)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_7, 4, 0, 1, 1)

        self.le_T3 = QLineEdit(self.gb_Output)
        self.le_T3.setObjectName(u"le_T3")
        self.le_T3.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_T3.sizePolicy().hasHeightForWidth())
        self.le_T3.setSizePolicy(sizePolicy2)
        self.le_T3.setMinimumSize(QSize(0, 0))
        self.le_T3.setMaximumSize(QSize(200, 16777215))
        self.le_T3.setBaseSize(QSize(150, 0))
        self.le_T3.setFont(font)

        self.grid_Output.addWidget(self.le_T3, 3, 1, 1, 1)

        self.le_T4 = QLineEdit(self.gb_Output)
        self.le_T4.setObjectName(u"le_T4")
        self.le_T4.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_T4.sizePolicy().hasHeightForWidth())
        self.le_T4.setSizePolicy(sizePolicy2)
        self.le_T4.setMinimumSize(QSize(0, 0))
        self.le_T4.setMaximumSize(QSize(200, 16777215))
        self.le_T4.setBaseSize(QSize(150, 0))
        self.le_T4.setFont(font)

        self.grid_Output.addWidget(self.le_T4, 4, 1, 1, 1)

        self.label_11 = QLabel(self.gb_Output)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_11, 3, 3, 1, 1, Qt.AlignRight)

        self.label_5 = QLabel(self.gb_Output)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_5, 2, 0, 1, 1)

        self.le_T2 = QLineEdit(self.gb_Output)
        self.le_T2.setObjectName(u"le_T2")
        self.le_T2.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_T2.sizePolicy().hasHeightForWidth())
        self.le_T2.setSizePolicy(sizePolicy2)
        self.le_T2.setMinimumSize(QSize(0, 0))
        self.le_T2.setMaximumSize(QSize(200, 16777215))
        self.le_T2.setBaseSize(QSize(150, 0))
        self.le_T2.setFont(font)

        self.grid_Output.addWidget(self.le_T2, 2, 1, 1, 1)

        self.le_T1 = QLineEdit(self.gb_Output)
        self.le_T1.setObjectName(u"le_T1")
        self.le_T1.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_T1.sizePolicy().hasHeightForWidth())
        self.le_T1.setSizePolicy(sizePolicy2)
        self.le_T1.setMinimumSize(QSize(0, 0))
        self.le_T1.setMaximumSize(QSize(200, 16777215))
        self.le_T1.setBaseSize(QSize(150, 0))
        self.le_T1.setFont(font)

        self.grid_Output.addWidget(self.le_T1, 0, 1, 1, 1)

        self.le_PowerStroke = QLineEdit(self.gb_Output)
        self.le_PowerStroke.setObjectName(u"le_PowerStroke")
        self.le_PowerStroke.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_PowerStroke.sizePolicy().hasHeightForWidth())
        self.le_PowerStroke.setSizePolicy(sizePolicy2)
        self.le_PowerStroke.setMinimumSize(QSize(0, 0))
        self.le_PowerStroke.setMaximumSize(QSize(200, 16777215))
        self.le_PowerStroke.setBaseSize(QSize(150, 0))
        self.le_PowerStroke.setFont(font)

        self.grid_Output.addWidget(self.le_PowerStroke, 0, 4, 1, 1)

        self.le_HeatAdded = QLineEdit(self.gb_Output)
        self.le_HeatAdded.setObjectName(u"le_HeatAdded")
        self.le_HeatAdded.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_HeatAdded.sizePolicy().hasHeightForWidth())
        self.le_HeatAdded.setSizePolicy(sizePolicy2)
        self.le_HeatAdded.setMinimumSize(QSize(0, 0))
        self.le_HeatAdded.setMaximumSize(QSize(200, 16777215))
        self.le_HeatAdded.setBaseSize(QSize(150, 0))
        self.le_HeatAdded.setFont(font)

        self.grid_Output.addWidget(self.le_HeatAdded, 3, 4, 1, 1)

        self.lbl_T1Units = QLabel(self.gb_Output)
        self.lbl_T1Units.setObjectName(u"lbl_T1Units")
        sizePolicy2.setHeightForWidth(self.lbl_T1Units.sizePolicy().hasHeightForWidth())
        self.lbl_T1Units.setSizePolicy(sizePolicy2)
        self.lbl_T1Units.setBaseSize(QSize(0, 0))
        self.lbl_T1Units.setFont(font)

        self.grid_Output.addWidget(self.lbl_T1Units, 0, 2, 1, 1)

        self.label_9 = QLabel(self.gb_Output)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_14 = QLabel(self.gb_Output)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_14, 0, 3, 1, 1, Qt.AlignRight)

        self.label_2 = QLabel(self.gb_Output)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(Qt.WheelFocus)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gb_Output)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(250, 0))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_10, 4, 3, 1, 1, Qt.AlignRight)

        self.lbl_PowerStrokeUnits = QLabel(self.gb_Output)
        self.lbl_PowerStrokeUnits.setObjectName(u"lbl_PowerStrokeUnits")
        sizePolicy2.setHeightForWidth(self.lbl_PowerStrokeUnits.sizePolicy().hasHeightForWidth())
        self.lbl_PowerStrokeUnits.setSizePolicy(sizePolicy2)
        self.lbl_PowerStrokeUnits.setFont(font)

        self.grid_Output.addWidget(self.lbl_PowerStrokeUnits, 0, 5, 1, 1)

        self.lbl_T4Units = QLabel(self.gb_Output)
        self.lbl_T4Units.setObjectName(u"lbl_T4Units")
        sizePolicy2.setHeightForWidth(self.lbl_T4Units.sizePolicy().hasHeightForWidth())
        self.lbl_T4Units.setSizePolicy(sizePolicy2)
        self.lbl_T4Units.setBaseSize(QSize(0, 0))
        self.lbl_T4Units.setFont(font)

        self.grid_Output.addWidget(self.lbl_T4Units, 4, 2, 1, 1)

        self.lbl_T3Units = QLabel(self.gb_Output)
        self.lbl_T3Units.setObjectName(u"lbl_T3Units")
        sizePolicy2.setHeightForWidth(self.lbl_T3Units.sizePolicy().hasHeightForWidth())
        self.lbl_T3Units.setSizePolicy(sizePolicy2)
        self.lbl_T3Units.setBaseSize(QSize(0, 0))
        self.lbl_T3Units.setFont(font)

        self.grid_Output.addWidget(self.lbl_T3Units, 3, 2, 1, 1)

        self.label_12 = QLabel(self.gb_Output)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font)

        self.grid_Output.addWidget(self.label_12, 4, 5, 1, 1)

        self.le_Efficiency = QLineEdit(self.gb_Output)
        self.le_Efficiency.setObjectName(u"le_Efficiency")
        self.le_Efficiency.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_Efficiency.sizePolicy().hasHeightForWidth())
        self.le_Efficiency.setSizePolicy(sizePolicy2)
        self.le_Efficiency.setMinimumSize(QSize(0, 0))
        self.le_Efficiency.setMaximumSize(QSize(200, 16777215))
        self.le_Efficiency.setBaseSize(QSize(150, 0))
        self.le_Efficiency.setFont(font)

        self.grid_Output.addWidget(self.le_Efficiency, 4, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.grid_Output.addItem(self.horizontalSpacer_2, 3, 6, 1, 1)

        self.lbl_HeatInUnits = QLabel(self.gb_Output)
        self.lbl_HeatInUnits.setObjectName(u"lbl_HeatInUnits")
        sizePolicy2.setHeightForWidth(self.lbl_HeatInUnits.sizePolicy().hasHeightForWidth())
        self.lbl_HeatInUnits.setSizePolicy(sizePolicy2)
        self.lbl_HeatInUnits.setFont(font)

        self.grid_Output.addWidget(self.lbl_HeatInUnits, 3, 5, 1, 1)

        self.lbl_CompressionStrokeUnits = QLabel(self.gb_Output)
        self.lbl_CompressionStrokeUnits.setObjectName(u"lbl_CompressionStrokeUnits")
        sizePolicy2.setHeightForWidth(self.lbl_CompressionStrokeUnits.sizePolicy().hasHeightForWidth())
        self.lbl_CompressionStrokeUnits.setSizePolicy(sizePolicy2)
        self.lbl_CompressionStrokeUnits.setFont(font)

        self.grid_Output.addWidget(self.lbl_CompressionStrokeUnits, 2, 5, 1, 1)

        self.lbl_T2Units = QLabel(self.gb_Output)
        self.lbl_T2Units.setObjectName(u"lbl_T2Units")
        sizePolicy2.setHeightForWidth(self.lbl_T2Units.sizePolicy().hasHeightForWidth())
        self.lbl_T2Units.setSizePolicy(sizePolicy2)
        self.lbl_T2Units.setBaseSize(QSize(0, 0))
        self.lbl_T2Units.setFont(font)

        self.grid_Output.addWidget(self.lbl_T2Units, 2, 2, 1, 1)

        self.le_CompressionStroke = QLineEdit(self.gb_Output)
        self.le_CompressionStroke.setObjectName(u"le_CompressionStroke")
        self.le_CompressionStroke.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_CompressionStroke.sizePolicy().hasHeightForWidth())
        self.le_CompressionStroke.setSizePolicy(sizePolicy2)
        self.le_CompressionStroke.setMinimumSize(QSize(0, 0))
        self.le_CompressionStroke.setMaximumSize(QSize(200, 16777215))
        self.le_CompressionStroke.setBaseSize(QSize(150, 0))
        self.le_CompressionStroke.setFont(font)

        self.grid_Output.addWidget(self.le_CompressionStroke, 2, 4, 1, 1)

        self.label_15 = QLabel(self.gb_Output)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Output.addWidget(self.label_15, 2, 3, 1, 1, Qt.AlignRight)


        self.main_VerticalLayout.addWidget(self.gb_Output)

        self.gb_Plot = QGroupBox(Form)
        self.gb_Plot.setObjectName(u"gb_Plot")
        sizePolicy5.setHeightForWidth(self.gb_Plot.sizePolicy().hasHeightForWidth())
        self.gb_Plot.setSizePolicy(sizePolicy5)
        self.gb_Plot.setFont(font)
        self.grid_Plot = QGridLayout(self.gb_Plot)
        self.grid_Plot.setObjectName(u"grid_Plot")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.grid_Plot.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.cmb_Ordinate = QComboBox(self.gb_Plot)
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.setObjectName(u"cmb_Ordinate")
        self.cmb_Ordinate.setMaximumSize(QSize(50, 16777215))

        self.grid_Plot.addWidget(self.cmb_Ordinate, 0, 3, 1, 1)

        self.lbl_Abcissa = QLabel(self.gb_Plot)
        self.lbl_Abcissa.setObjectName(u"lbl_Abcissa")
        self.lbl_Abcissa.setMaximumSize(QSize(150, 16777215))

        self.grid_Plot.addWidget(self.lbl_Abcissa, 0, 0, 1, 1)

        self.lbl_Ordinate = QLabel(self.gb_Plot)
        self.lbl_Ordinate.setObjectName(u"lbl_Ordinate")
        self.lbl_Ordinate.setMaximumSize(QSize(150, 16777215))
        self.lbl_Ordinate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_Plot.addWidget(self.lbl_Ordinate, 0, 2, 1, 1)

        self.chk_LogAbcissa = QCheckBox(self.gb_Plot)
        self.chk_LogAbcissa.setObjectName(u"chk_LogAbcissa")

        self.grid_Plot.addWidget(self.chk_LogAbcissa, 1, 0, 1, 2)

        self.chk_LogOrdinate = QCheckBox(self.gb_Plot)
        self.chk_LogOrdinate.setObjectName(u"chk_LogOrdinate")

        self.grid_Plot.addWidget(self.chk_LogOrdinate, 1, 2, 1, 2)

        self.cmb_Abcissa = QComboBox(self.gb_Plot)
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.setObjectName(u"cmb_Abcissa")
        sizePolicy5.setHeightForWidth(self.cmb_Abcissa.sizePolicy().hasHeightForWidth())
        self.cmb_Abcissa.setSizePolicy(sizePolicy5)
        self.cmb_Abcissa.setMaximumSize(QSize(50, 16777215))

        self.grid_Plot.addWidget(self.cmb_Abcissa, 0, 1, 1, 1)


        self.main_VerticalLayout.addWidget(self.gb_Plot)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_VerticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        self.cmb_Ordinate.setCurrentIndex(0)
        self.cmb_Abcissa.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gb_Input.setTitle(QCoreApplication.translate("Form", u"Input for Air Standard Otto Cycle", None))
        self.lbl_P0.setText(QCoreApplication.translate("Form", u"P0 (atm)", None))
        self.lbl_TLow.setText(QCoreApplication.translate("Form", u"T Low (R)", None))
        self.le_TLow.setText(QCoreApplication.translate("Form", u"500.0", None))
        self.le_TLow.setPlaceholderText(QCoreApplication.translate("Form", u"enter a value for the high pressure isobar", None))
        self.lbl_V0.setText(QCoreApplication.translate("Form", u"Cylinder V (ft^3)", None))
        self.lbl_THigh.setText(QCoreApplication.translate("Form", u"T High (R)", None))
        self.le_THigh.setText(QCoreApplication.translate("Form", u"3600.0", None))
        self.le_THigh.setPlaceholderText(QCoreApplication.translate("Form", u"enter a value for the high pressure isobar", None))
        self.le_V0.setText(QCoreApplication.translate("Form", u"0.02", None))
        self.le_P0.setText(QCoreApplication.translate("Form", u"1.0", None))
        self.le_P0.setPlaceholderText(QCoreApplication.translate("Form", u"enter a value for the low pressure isobar", None))
        self.le_CR.setText(QCoreApplication.translate("Form", u"8.0", None))
        self.le_CR.setPlaceholderText(QCoreApplication.translate("Form", u"turbine isentropic efficiency 0.0<eta<=1.0", None))
        self.lbl_CR.setText(QCoreApplication.translate("Form", u"Compression Ratio", None))
        self.rdo_English.setText(QCoreApplication.translate("Form", u"English", None))
        self.rdo_Metric.setText(QCoreApplication.translate("Form", u"Metric", None))
        self.btn_Calculate.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.cmb_OttoDiesel.setItemText(0, QCoreApplication.translate("Form", u"Otto cycle", None))
        self.cmb_OttoDiesel.setItemText(1, QCoreApplication.translate("Form", u"Diesel cycle", None))

        self.gb_Output.setTitle(QCoreApplication.translate("Form", u"Output", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"T4", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Heat Added", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"T2", None))
        self.lbl_T1Units.setText(QCoreApplication.translate("Form", u"C", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"T3", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Power Stroke", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"T1", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Cycle Efficiency", None))
        self.lbl_PowerStrokeUnits.setText(QCoreApplication.translate("Form", u"kJ/kg", None))
        self.lbl_T4Units.setText(QCoreApplication.translate("Form", u"C", None))
        self.lbl_T3Units.setText(QCoreApplication.translate("Form", u"C", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"%", None))
        self.lbl_HeatInUnits.setText(QCoreApplication.translate("Form", u"kJ/kg", None))
        self.lbl_CompressionStrokeUnits.setText(QCoreApplication.translate("Form", u"kJ/kg", None))
        self.lbl_T2Units.setText(QCoreApplication.translate("Form", u"C", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Compression Stroke", None))
        self.gb_Plot.setTitle(QCoreApplication.translate("Form", u"Plot", None))
        self.cmb_Ordinate.setItemText(0, QCoreApplication.translate("Form", u"P", None))
        self.cmb_Ordinate.setItemText(1, QCoreApplication.translate("Form", u"T", None))
        self.cmb_Ordinate.setItemText(2, QCoreApplication.translate("Form", u"u", None))
        self.cmb_Ordinate.setItemText(3, QCoreApplication.translate("Form", u"h", None))
        self.cmb_Ordinate.setItemText(4, QCoreApplication.translate("Form", u"s", None))
        self.cmb_Ordinate.setItemText(5, QCoreApplication.translate("Form", u"v", None))

        self.lbl_Abcissa.setText(QCoreApplication.translate("Form", u"Abcissa (x)", None))
        self.lbl_Ordinate.setText(QCoreApplication.translate("Form", u"Ordinate (y)", None))
        self.chk_LogAbcissa.setText(QCoreApplication.translate("Form", u"Logarithmic (x)", None))
        self.chk_LogOrdinate.setText(QCoreApplication.translate("Form", u"Logarithmic (y)", None))
        self.cmb_Abcissa.setItemText(0, QCoreApplication.translate("Form", u"P", None))
        self.cmb_Abcissa.setItemText(1, QCoreApplication.translate("Form", u"T", None))
        self.cmb_Abcissa.setItemText(2, QCoreApplication.translate("Form", u"u", None))
        self.cmb_Abcissa.setItemText(3, QCoreApplication.translate("Form", u"h", None))
        self.cmb_Abcissa.setItemText(4, QCoreApplication.translate("Form", u"s", None))
        self.cmb_Abcissa.setItemText(5, QCoreApplication.translate("Form", u"v", None))

        self.cmb_Abcissa.setCurrentText(QCoreApplication.translate("Form", u"v", None))
    # retranslateUi

