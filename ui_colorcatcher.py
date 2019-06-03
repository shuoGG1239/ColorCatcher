# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_colorcatcher.ui'
#
# Created: Mon Jun  3 20:46:00 2019
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ColorCatcher(object):
    def setupUi(self, ColorCatcher):
        ColorCatcher.setObjectName("ColorCatcher")
        ColorCatcher.resize(214, 84)
        self.verticalLayout = QtWidgets.QVBoxLayout(ColorCatcher)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelActive = QtWidgets.QLabel(ColorCatcher)
        self.labelActive.setObjectName("labelActive")
        self.verticalLayout.addWidget(self.labelActive)
        self.labelMark = QtWidgets.QLabel(ColorCatcher)
        self.labelMark.setObjectName("labelMark")
        self.verticalLayout.addWidget(self.labelMark)

        self.retranslateUi(ColorCatcher)
        QtCore.QMetaObject.connectSlotsByName(ColorCatcher)

    def retranslateUi(self, ColorCatcher):
        _translate = QtCore.QCoreApplication.translate
        ColorCatcher.setWindowTitle(_translate("ColorCatcher", "ColorCatcher"))
        self.labelActive.setText(_translate("ColorCatcher", "This is color"))
        self.labelMark.setText(_translate("ColorCatcher", "This is color"))

