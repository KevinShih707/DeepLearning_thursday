# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'problem5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Problem_5(object):
    def setupUi(self, Problem_5):
        Problem_5.setObjectName("Problem_5")
        Problem_5.resize(400, 300)
        self.button_5_1 = QtWidgets.QPushButton(Problem_5)
        self.button_5_1.setGeometry(QtCore.QRect(60, 20, 251, 31))
        self.button_5_1.setObjectName("button_5_1")
        self.button_5_2 = QtWidgets.QPushButton(Problem_5)
        self.button_5_2.setGeometry(QtCore.QRect(60, 60, 251, 31))
        self.button_5_2.setObjectName("button_5_2")
        self.button_5_3 = QtWidgets.QPushButton(Problem_5)
        self.button_5_3.setGeometry(QtCore.QRect(60, 100, 251, 31))
        self.button_5_3.setObjectName("button_5_3")
        self.button_5_4 = QtWidgets.QPushButton(Problem_5)
        self.button_5_4.setGeometry(QtCore.QRect(60, 140, 251, 31))
        self.button_5_4.setObjectName("button_5_4")
        self.label = QtWidgets.QLabel(Problem_5)
        self.label.setGeometry(QtCore.QRect(80, 190, 61, 16))
        self.label.setObjectName("label")
        self.text_input = QtWidgets.QTextEdit(Problem_5)
        self.text_input.setGeometry(QtCore.QRect(160, 190, 151, 21))
        self.text_input.setObjectName("text_input")
        self.button_5_5 = QtWidgets.QPushButton(Problem_5)
        self.button_5_5.setGeometry(QtCore.QRect(60, 220, 251, 31))
        self.button_5_5.setObjectName("button_5_5")

        self.retranslateUi(Problem_5)
        QtCore.QMetaObject.connectSlotsByName(Problem_5)

    def retranslateUi(self, Problem_5):
        _translate = QtCore.QCoreApplication.translate
        Problem_5.setWindowTitle(_translate("Problem_5", "Dialog"))
        self.button_5_1.setText(_translate("Problem_5", "5.1 Show Train Images"))
        self.button_5_2.setText(_translate("Problem_5", "5.2 Show Hyperparameters"))
        self.button_5_3.setText(_translate("Problem_5", "5.3 Show Epoch"))
        self.button_5_4.setText(_translate("Problem_5", "5.4 Show Train Result"))
        self.label.setText(_translate("Problem_5", "Test Image Index:"))
        self.button_5_5.setText(_translate("Problem_5", "5.5 Inference"))
