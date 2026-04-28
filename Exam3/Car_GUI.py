# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Car_GUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1143, 959)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.grp_Inputs = QGroupBox(Form)
        self.grp_Inputs.setObjectName(u"grp_Inputs")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_Inputs.sizePolicy().hasHeightForWidth())
        self.grp_Inputs.setSizePolicy(sizePolicy)
        self.grp_Inputs.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.grp_Inputs.setFont(font)
        self.grp_Inputs.setFlat(False)
        self.gridLayout = QGridLayout(self.grp_Inputs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.le_k2 = QLineEdit(self.grp_Inputs)
        self.le_k2.setObjectName(u"le_k2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_k2.sizePolicy().hasHeightForWidth())
        self.le_k2.setSizePolicy(sizePolicy1)
        self.le_k2.setMinimumSize(QSize(75, 0))
        self.le_k2.setMaximumSize(QSize(150, 16777215))
        self.le_k2.setFont(font)

        self.gridLayout.addWidget(self.le_k2, 5, 1, 1, 1)

        self.le_tmax = QLineEdit(self.grp_Inputs)
        self.le_tmax.setObjectName(u"le_tmax")
        sizePolicy1.setHeightForWidth(self.le_tmax.sizePolicy().hasHeightForWidth())
        self.le_tmax.setSizePolicy(sizePolicy1)
        self.le_tmax.setMinimumSize(QSize(75, 0))
        self.le_tmax.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.le_tmax, 7, 1, 1, 1)

        self.lbl_CarSpeed = QLabel(self.grp_Inputs)
        self.lbl_CarSpeed.setObjectName(u"lbl_CarSpeed")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_CarSpeed.sizePolicy().hasHeightForWidth())
        self.lbl_CarSpeed.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_CarSpeed, 1, 0, 1, 1, Qt.AlignRight)

        self.lbl_m2 = QLabel(self.grp_Inputs)
        self.lbl_m2.setObjectName(u"lbl_m2")
        sizePolicy2.setHeightForWidth(self.lbl_m2.sizePolicy().hasHeightForWidth())
        self.lbl_m2.setSizePolicy(sizePolicy2)
        self.lbl_m2.setFont(font)
        self.lbl_m2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_m2, 4, 0, 1, 1, Qt.AlignRight)

        self.lbl_k2 = QLabel(self.grp_Inputs)
        self.lbl_k2.setObjectName(u"lbl_k2")
        sizePolicy2.setHeightForWidth(self.lbl_k2.sizePolicy().hasHeightForWidth())
        self.lbl_k2.setSizePolicy(sizePolicy2)
        self.lbl_k2.setFont(font)
        self.lbl_k2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_k2, 5, 0, 1, 1, Qt.AlignRight)

        self.lbl_Spring1 = QLabel(self.grp_Inputs)
        self.lbl_Spring1.setObjectName(u"lbl_Spring1")
        sizePolicy2.setHeightForWidth(self.lbl_Spring1.sizePolicy().hasHeightForWidth())
        self.lbl_Spring1.setSizePolicy(sizePolicy2)
        self.lbl_Spring1.setFont(font)
        self.lbl_Spring1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_Spring1, 2, 0, 1, 1, Qt.AlignRight)

        self.le_c1 = QLineEdit(self.grp_Inputs)
        self.le_c1.setObjectName(u"le_c1")
        sizePolicy1.setHeightForWidth(self.le_c1.sizePolicy().hasHeightForWidth())
        self.le_c1.setSizePolicy(sizePolicy1)
        self.le_c1.setMinimumSize(QSize(75, 0))
        self.le_c1.setMaximumSize(QSize(150, 16777215))
        self.le_c1.setFont(font)

        self.gridLayout.addWidget(self.le_c1, 3, 1, 1, 1)

        self.le_m1 = QLineEdit(self.grp_Inputs)
        self.le_m1.setObjectName(u"le_m1")
        sizePolicy1.setHeightForWidth(self.le_m1.sizePolicy().hasHeightForWidth())
        self.le_m1.setSizePolicy(sizePolicy1)
        self.le_m1.setMinimumSize(QSize(75, 0))
        self.le_m1.setMaximumSize(QSize(150, 16777215))
        self.le_m1.setFont(font)

        self.gridLayout.addWidget(self.le_m1, 0, 1, 1, 1)

        self.lbl_tMax = QLabel(self.grp_Inputs)
        self.lbl_tMax.setObjectName(u"lbl_tMax")
        sizePolicy2.setHeightForWidth(self.lbl_tMax.sizePolicy().hasHeightForWidth())
        self.lbl_tMax.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_tMax, 7, 0, 1, 1, Qt.AlignRight)

        self.le_v = QLineEdit(self.grp_Inputs)
        self.le_v.setObjectName(u"le_v")
        sizePolicy1.setHeightForWidth(self.le_v.sizePolicy().hasHeightForWidth())
        self.le_v.setSizePolicy(sizePolicy1)
        self.le_v.setMinimumSize(QSize(75, 0))
        self.le_v.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.le_v, 1, 1, 1, 1)

        self.lbl_CarBodyMass = QLabel(self.grp_Inputs)
        self.lbl_CarBodyMass.setObjectName(u"lbl_CarBodyMass")
        sizePolicy2.setHeightForWidth(self.lbl_CarBodyMass.sizePolicy().hasHeightForWidth())
        self.lbl_CarBodyMass.setSizePolicy(sizePolicy2)
        self.lbl_CarBodyMass.setFont(font)
        self.lbl_CarBodyMass.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_CarBodyMass, 0, 0, 1, 1, Qt.AlignRight)

        self.gv_Schematic = QGraphicsView(self.grp_Inputs)
        self.gv_Schematic.setObjectName(u"gv_Schematic")
        self.gv_Schematic.setMinimumSize(QSize(500, 500))
        self.gv_Schematic.setMaximumSize(QSize(600, 600))

        self.gridLayout.addWidget(self.gv_Schematic, 15, 0, 1, 2)

        self.chk_IncludeAccel = QCheckBox(self.grp_Inputs)
        self.chk_IncludeAccel.setObjectName(u"chk_IncludeAccel")

        self.gridLayout.addWidget(self.chk_IncludeAccel, 12, 0, 1, 2, Qt.AlignRight)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_calculate = QPushButton(self.grp_Inputs)
        self.btn_calculate.setObjectName(u"btn_calculate")
        sizePolicy1.setHeightForWidth(self.btn_calculate.sizePolicy().hasHeightForWidth())
        self.btn_calculate.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.btn_calculate, 0, Qt.AlignRight)

        self.pb_Optimize = QPushButton(self.grp_Inputs)
        self.pb_Optimize.setObjectName(u"pb_Optimize")
        sizePolicy1.setHeightForWidth(self.pb_Optimize.sizePolicy().hasHeightForWidth())
        self.pb_Optimize.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.pb_Optimize, 0, Qt.AlignRight)


        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 2)

        self.chk_ShowAccel = QCheckBox(self.grp_Inputs)
        self.chk_ShowAccel.setObjectName(u"chk_ShowAccel")

        self.gridLayout.addWidget(self.chk_ShowAccel, 11, 0, 1, 2, Qt.AlignRight)

        self.lbl_MaxMinInfo = QLabel(self.grp_Inputs)
        self.lbl_MaxMinInfo.setObjectName(u"lbl_MaxMinInfo")

        self.gridLayout.addWidget(self.lbl_MaxMinInfo, 14, 0, 1, 2, Qt.AlignRight)

        self.lbl_RampANgle = QLabel(self.grp_Inputs)
        self.lbl_RampANgle.setObjectName(u"lbl_RampANgle")
        sizePolicy2.setHeightForWidth(self.lbl_RampANgle.sizePolicy().hasHeightForWidth())
        self.lbl_RampANgle.setSizePolicy(sizePolicy2)
        self.lbl_RampANgle.setFont(font)
        self.lbl_RampANgle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_RampANgle, 6, 0, 1, 1, Qt.AlignRight)

        self.le_k1 = QLineEdit(self.grp_Inputs)
        self.le_k1.setObjectName(u"le_k1")
        sizePolicy1.setHeightForWidth(self.le_k1.sizePolicy().hasHeightForWidth())
        self.le_k1.setSizePolicy(sizePolicy1)
        self.le_k1.setMinimumSize(QSize(75, 0))
        self.le_k1.setMaximumSize(QSize(150, 16777215))
        self.le_k1.setFont(font)

        self.gridLayout.addWidget(self.le_k1, 2, 1, 1, 1)

        self.le_m2 = QLineEdit(self.grp_Inputs)
        self.le_m2.setObjectName(u"le_m2")
        sizePolicy1.setHeightForWidth(self.le_m2.sizePolicy().hasHeightForWidth())
        self.le_m2.setSizePolicy(sizePolicy1)
        self.le_m2.setMinimumSize(QSize(75, 0))
        self.le_m2.setMaximumSize(QSize(150, 16777215))
        self.le_m2.setFont(font)

        self.gridLayout.addWidget(self.le_m2, 4, 1, 1, 1)

        self.le_ang = QLineEdit(self.grp_Inputs)
        self.le_ang.setObjectName(u"le_ang")
        sizePolicy1.setHeightForWidth(self.le_ang.sizePolicy().hasHeightForWidth())
        self.le_ang.setSizePolicy(sizePolicy1)
        self.le_ang.setMinimumSize(QSize(75, 0))
        self.le_ang.setMaximumSize(QSize(150, 16777215))
        self.le_ang.setFont(font)

        self.gridLayout.addWidget(self.le_ang, 6, 1, 1, 1)

        self.layourhorizontal = QHBoxLayout()
        self.layourhorizontal.setObjectName(u"layourhorizontal")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layourhorizontal.addItem(self.horizontalSpacer_2)

        self.chk_LogX = QCheckBox(self.grp_Inputs)
        self.chk_LogX.setObjectName(u"chk_LogX")

        self.layourhorizontal.addWidget(self.chk_LogX, 0, Qt.AlignRight)

        self.chk_LogY = QCheckBox(self.grp_Inputs)
        self.chk_LogY.setObjectName(u"chk_LogY")

        self.layourhorizontal.addWidget(self.chk_LogY, 0, Qt.AlignRight)

        self.chk_LogAccel = QCheckBox(self.grp_Inputs)
        self.chk_LogAccel.setObjectName(u"chk_LogAccel")

        self.layourhorizontal.addWidget(self.chk_LogAccel, 0, Qt.AlignRight)


        self.gridLayout.addLayout(self.layourhorizontal, 9, 0, 1, 2)

        self.lbl_Dashpot = QLabel(self.grp_Inputs)
        self.lbl_Dashpot.setObjectName(u"lbl_Dashpot")
        sizePolicy2.setHeightForWidth(self.lbl_Dashpot.sizePolicy().hasHeightForWidth())
        self.lbl_Dashpot.setSizePolicy(sizePolicy2)
        self.lbl_Dashpot.setFont(font)
        self.lbl_Dashpot.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_Dashpot, 3, 0, 1, 1, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.grp_Inputs)

        self.layout_horizontal_main = QHBoxLayout()
        self.layout_horizontal_main.setObjectName(u"layout_horizontal_main")

        self.horizontalLayout.addLayout(self.layout_horizontal_main)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.grp_Inputs.setTitle(QCoreApplication.translate("Form", u"Model Inputs", None))
        self.le_k2.setText(QCoreApplication.translate("Form", u"90000", None))
        self.le_tmax.setText(QCoreApplication.translate("Form", u"3", None))
        self.lbl_CarSpeed.setText(QCoreApplication.translate("Form", u"Car Speed (kph)", None))
        self.lbl_m2.setText(QCoreApplication.translate("Form", u"Wheel mass (m2, kg)", None))
        self.lbl_k2.setText(QCoreApplication.translate("Form", u"Tire spring constant (k2, N/m)", None))
        self.lbl_Spring1.setText(QCoreApplication.translate("Form", u"Suspension Spring (k1, N/m)", None))
        self.le_c1.setText(QCoreApplication.translate("Form", u"4500", None))
        self.le_m1.setText(QCoreApplication.translate("Form", u"450", None))
        self.lbl_tMax.setText(QCoreApplication.translate("Form", u"t, max plot (s)", None))
        self.le_v.setText(QCoreApplication.translate("Form", u"120", None))
        self.lbl_CarBodyMass.setText(QCoreApplication.translate("Form", u"Car body mass (m1, kg)", None))
        self.chk_IncludeAccel.setText(QCoreApplication.translate("Form", u"Include Accel in Opt.", None))
        self.btn_calculate.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.pb_Optimize.setText(QCoreApplication.translate("Form", u"Optimize Suspension", None))
        self.chk_ShowAccel.setText(QCoreApplication.translate("Form", u"Plot Car Accel.", None))
        self.lbl_MaxMinInfo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_RampANgle.setText(QCoreApplication.translate("Form", u"Ramp Angle (deg)", None))
        self.le_k1.setText(QCoreApplication.translate("Form", u"15000", None))
        self.le_m2.setText(QCoreApplication.translate("Form", u"20", None))
        self.le_ang.setText(QCoreApplication.translate("Form", u"45", None))
        self.chk_LogX.setText(QCoreApplication.translate("Form", u"log scale t", None))
        self.chk_LogY.setText(QCoreApplication.translate("Form", u"log scale Y", None))
        self.chk_LogAccel.setText(QCoreApplication.translate("Form", u"log scale Y''", None))
        self.lbl_Dashpot.setText(QCoreApplication.translate("Form", u"Suspension Shock Absorber (c1, N*s/m)", None))
    # retranslateUi

