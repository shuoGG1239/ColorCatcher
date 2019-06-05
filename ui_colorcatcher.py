# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_colorcatcher.ui'
#
# Created: Wed Jun  5 19:07:17 2019
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ColorCatcher(object):
    def setupUi(self, ColorCatcher):
        ColorCatcher.setObjectName("ColorCatcher")
        ColorCatcher.resize(259, 88)
        self.verticalLayout = QtWidgets.QVBoxLayout(ColorCatcher)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditMove = QtWidgets.QLineEdit(ColorCatcher)
        self.lineEditMove.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditMove.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMove.setReadOnly(True)
        self.lineEditMove.setPlaceholderText("")
        self.lineEditMove.setObjectName("lineEditMove")
        self.verticalLayout.addWidget(self.lineEditMove)
        self.lineEditMark = QtWidgets.QLineEdit(ColorCatcher)
        self.lineEditMark.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditMark.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMark.setReadOnly(True)
        self.lineEditMark.setObjectName("lineEditMark")
        self.verticalLayout.addWidget(self.lineEditMark)

        self.retranslateUi(ColorCatcher)
        QtCore.QMetaObject.connectSlotsByName(ColorCatcher)

    def retranslateUi(self, ColorCatcher):
        _translate = QtCore.QCoreApplication.translate
        ColorCatcher.setWindowTitle(_translate("ColorCatcher", "ColorCatcher"))
        self.lineEditMark.setText(_translate("ColorCatcher", "Press Space to mark"))
        self.lineEditMark.setPlaceholderText(_translate("ColorCatcher", "Press Space to mark!"))

