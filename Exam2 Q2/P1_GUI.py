# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'P1_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
## Yeah... Since I generated this myself using PySide6, I'm pretty sure that warning is moot.
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(681, 1255)
        self.layout_VertMain = QVBoxLayout(MainForm)
        self.layout_VertMain.setObjectName(u"layout_VertMain")
        self.gb_Input = QGroupBox(MainForm)
        self.gb_Input.setObjectName(u"gb_Input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Input.sizePolicy().hasHeightForWidth())
        self.gb_Input.setSizePolicy(sizePolicy)
        self.layout_VertInput = QVBoxLayout(self.gb_Input)
        self.layout_VertInput.setObjectName(u"layout_VertInput")
        self.layout_GridInput = QGridLayout()
        self.layout_GridInput.setObjectName(u"layout_GridInput")
        self.le_Resistance = QLineEdit(self.gb_Input)
        self.le_Resistance.setObjectName(u"le_Resistance")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_Resistance.sizePolicy().hasHeightForWidth())
        self.le_Resistance.setSizePolicy(sizePolicy1)
        self.le_Resistance.setMaximumSize(QSize(100, 16777215))
        self.le_Resistance.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_Resistance, 1, 1, 1, 1)

        self.lbl_freq = QLabel(self.gb_Input)
        self.lbl_freq.setObjectName(u"lbl_freq")
        self.lbl_freq.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_freq, 5, 0, 1, 1)

        self.le_Freq = QLineEdit(self.gb_Input)
        self.le_Freq.setObjectName(u"le_Freq")
        sizePolicy1.setHeightForWidth(self.le_Freq.sizePolicy().hasHeightForWidth())
        self.le_Freq.setSizePolicy(sizePolicy1)
        self.le_Freq.setMaximumSize(QSize(100, 16777215))
        self.le_Freq.setBaseSize(QSize(300, 0))
        self.le_Freq.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_Freq, 5, 1, 1, 1)

        self.lbl_Resistor = QLabel(self.gb_Input)
        self.lbl_Resistor.setObjectName(u"lbl_Resistor")
        self.lbl_Resistor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_Resistor, 1, 0, 1, 1)

        self.le_Phase = QLineEdit(self.gb_Input)
        self.le_Phase.setObjectName(u"le_Phase")
        sizePolicy1.setHeightForWidth(self.le_Phase.sizePolicy().hasHeightForWidth())
        self.le_Phase.setSizePolicy(sizePolicy1)
        self.le_Phase.setMaximumSize(QSize(100, 16777215))
        self.le_Phase.setBaseSize(QSize(300, 0))
        self.le_Phase.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_Phase, 6, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_GridInput.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_3 = QLabel(self.gb_Input)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_GridInput.addWidget(self.label_3, 2, 0, 1, 1)

        self.lbl_Phase = QLabel(self.gb_Input)
        self.lbl_Phase.setObjectName(u"lbl_Phase")
        self.lbl_Phase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_Phase, 6, 0, 1, 1)

        self.lbl_DrivingVoltage = QLabel(self.gb_Input)
        self.lbl_DrivingVoltage.setObjectName(u"lbl_DrivingVoltage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_DrivingVoltage.sizePolicy().hasHeightForWidth())
        self.lbl_DrivingVoltage.setSizePolicy(sizePolicy2)

        self.layout_GridInput.addWidget(self.lbl_DrivingVoltage, 3, 0, 1, 3)

        self.le_Amplitude = QLineEdit(self.gb_Input)
        self.le_Amplitude.setObjectName(u"le_Amplitude")
        sizePolicy1.setHeightForWidth(self.le_Amplitude.sizePolicy().hasHeightForWidth())
        self.le_Amplitude.setSizePolicy(sizePolicy1)
        self.le_Amplitude.setMaximumSize(QSize(100, 16777215))
        self.le_Amplitude.setBaseSize(QSize(300, 0))
        self.le_Amplitude.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_Amplitude, 4, 1, 1, 1)

        self.le_Inductance = QLineEdit(self.gb_Input)
        self.le_Inductance.setObjectName(u"le_Inductance")
        sizePolicy1.setHeightForWidth(self.le_Inductance.sizePolicy().hasHeightForWidth())
        self.le_Inductance.setSizePolicy(sizePolicy1)
        self.le_Inductance.setMaximumSize(QSize(100, 16777215))
        self.le_Inductance.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_Inductance, 0, 1, 1, 1)

        self.pb_Calculate = QPushButton(self.gb_Input)
        self.pb_Calculate.setObjectName(u"pb_Calculate")

        self.layout_GridInput.addWidget(self.pb_Calculate, 9, 0, 1, 2)

        self.lbl_Indutor = QLabel(self.gb_Input)
        self.lbl_Indutor.setObjectName(u"lbl_Indutor")
        self.lbl_Indutor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_Indutor, 0, 0, 1, 1)

        self.le_Capacitence = QLineEdit(self.gb_Input)
        self.le_Capacitence.setObjectName(u"le_Capacitence")
        sizePolicy1.setHeightForWidth(self.le_Capacitence.sizePolicy().hasHeightForWidth())
        self.le_Capacitence.setSizePolicy(sizePolicy1)
        self.le_Capacitence.setMaximumSize(QSize(100, 16777215))
        self.le_Capacitence.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_Capacitence, 2, 1, 1, 1)

        self.lbl_Amplitude = QLabel(self.gb_Input)
        self.lbl_Amplitude.setObjectName(u"lbl_Amplitude")
        self.lbl_Amplitude.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_Amplitude, 4, 0, 1, 1)

        self.lbl_SimTime = QLabel(self.gb_Input)
        self.lbl_SimTime.setObjectName(u"lbl_SimTime")
        self.lbl_SimTime.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_SimTime, 7, 0, 1, 1)

        self.lbl_simPts = QLabel(self.gb_Input)
        self.lbl_simPts.setObjectName(u"lbl_simPts")
        self.lbl_simPts.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.layout_GridInput.addWidget(self.lbl_simPts, 8, 0, 1, 1)

        self.le_simTime = QLineEdit(self.gb_Input)
        self.le_simTime.setObjectName(u"le_simTime")
        sizePolicy1.setHeightForWidth(self.le_simTime.sizePolicy().hasHeightForWidth())
        self.le_simTime.setSizePolicy(sizePolicy1)
        self.le_simTime.setMaximumSize(QSize(100, 16777215))
        self.le_simTime.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_simTime, 7, 1, 1, 1)

        self.le_simPts = QLineEdit(self.gb_Input)
        self.le_simPts.setObjectName(u"le_simPts")
        sizePolicy1.setHeightForWidth(self.le_simPts.sizePolicy().hasHeightForWidth())
        self.le_simPts.setSizePolicy(sizePolicy1)
        self.le_simPts.setMaximumSize(QSize(100, 16777215))
        self.le_simPts.setClearButtonEnabled(True)

        self.layout_GridInput.addWidget(self.le_simPts, 8, 1, 1, 1)


        self.layout_VertInput.addLayout(self.layout_GridInput)


        self.layout_VertMain.addWidget(self.gb_Input)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.gb_Input.setTitle(QCoreApplication.translate("MainForm", u"Input", None))
        self.le_Resistance.setText(QCoreApplication.translate("MainForm", u"10.0", None))
        self.le_Resistance.setPlaceholderText(QCoreApplication.translate("MainForm", u"10.0", None))
        self.lbl_freq.setText(QCoreApplication.translate("MainForm", u"f (Hz)", None))
        self.le_Freq.setText(QCoreApplication.translate("MainForm", u"20", None))
        self.le_Freq.setPlaceholderText(QCoreApplication.translate("MainForm", u"20.0", None))
        self.lbl_Resistor.setText(QCoreApplication.translate("MainForm", u"R (ohm)", None))
        self.le_Phase.setText(QCoreApplication.translate("MainForm", u"0.0", None))
        self.le_Phase.setPlaceholderText(QCoreApplication.translate("MainForm", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("MainForm", u"C (F)", None))
        self.lbl_Phase.setText(QCoreApplication.translate("MainForm", u"p (deg)", None))
        self.lbl_DrivingVoltage.setText(QCoreApplication.translate("MainForm", u"Driving Voltage:  v(t) = A*sin(f*t+p)", None))
        self.le_Amplitude.setText(QCoreApplication.translate("MainForm", u"20", None))
        self.le_Amplitude.setPlaceholderText(QCoreApplication.translate("MainForm", u"20.0", None))
        self.le_Inductance.setText(QCoreApplication.translate("MainForm", u"20.0", None))
        self.le_Inductance.setPlaceholderText(QCoreApplication.translate("MainForm", u"20.0", None))
        self.pb_Calculate.setText(QCoreApplication.translate("MainForm", u"Calculate", None))
        self.lbl_Indutor.setText(QCoreApplication.translate("MainForm", u"L (H)", None))
        self.le_Capacitence.setText(QCoreApplication.translate("MainForm", u"0.05", None))
        self.le_Capacitence.setPlaceholderText(QCoreApplication.translate("MainForm", u"0.05", None))
        self.lbl_Amplitude.setText(QCoreApplication.translate("MainForm", u"A (V)", None))
        self.lbl_SimTime.setText(QCoreApplication.translate("MainForm", u"sim time (s)", None))
        self.lbl_simPts.setText(QCoreApplication.translate("MainForm", u"sim points", None))
        self.le_simTime.setText(QCoreApplication.translate("MainForm", u"10.0", None))
        self.le_simTime.setPlaceholderText(QCoreApplication.translate("MainForm", u"10.0", None))
        self.le_simPts.setText(QCoreApplication.translate("MainForm", u"500", None))
        self.le_simPts.setPlaceholderText(QCoreApplication.translate("MainForm", u"500", None))
    # retranslateUi

