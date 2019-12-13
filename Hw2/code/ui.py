# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cvdl.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 488)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 60, 251, 151))
        self.groupBox.setObjectName("groupBox")
        self.button_1_1 = QtWidgets.QPushButton(self.groupBox)
        self.button_1_1.setGeometry(QtCore.QRect(50, 40, 161, 71))
        self.button_1_1.setObjectName("button_1_1")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 60, 231, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.button_3_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_3_1.setGeometry(QtCore.QRect(40, 30, 151, 41))
        self.button_3_1.setObjectName("button_3_1")
        self.button_3_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_3_2.setGeometry(QtCore.QRect(40, 90, 151, 41))
        self.button_3_2.setObjectName("button_3_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 280, 241, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.button_2_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_2_1.setGeometry(QtCore.QRect(40, 30, 141, 51))
        self.button_2_1.setObjectName("button_2_1")
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(380, 370, 93, 28))
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(490, 370, 93, 28))
        self.button_cancel.setObjectName("button_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "1. Stereo"))
        self.button_1_1.setText(_translate("Dialog", "1.1 Disparity"))
        self.groupBox_2.setTitle(_translate("Dialog", "3. SIFT"))
        self.button_3_1.setText(_translate("Dialog", "3.1 Keypoints"))
        self.button_3_2.setText(_translate("Dialog", "3.2 Matched keypoints"))
        self.groupBox_3.setTitle(_translate("Dialog", "2. Normalized Cross Correlation"))
        self.button_2_1.setText(_translate("Dialog", "2.1 NCC"))
        self.button_ok.setText(_translate("Dialog", "OK"))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))
