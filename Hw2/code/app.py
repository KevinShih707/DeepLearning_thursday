# -*- coding: utf-8 -*-

import sys
from ui import Ui_Dialog
import cv2
import os
import numpy as np
import glob
from PyQt5.QtWidgets import QMainWindow, QApplication
from decimal import Decimal


class MainWindow(QMainWindow, Ui_Dialog):
    _count = 0
    _image = None
    _arrPoint = []
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    # Write your code below
    # UI components are defined in hw1_ui.py, please take a look.
    # You can also open hw1.ui by qt-designer to check ui components.

    def onBindingUI(self):
        self.button_1_1.clicked.connect(self.button_1_1_click)


    def button_1_1_click(self):
        imgL = cv2.imread('image/imL.png',0)
        imgR = cv2.imread('image/imR.png',0)

        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        disparity = stereo.compute(imgL,imgR)
        disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('Without L-R Disparity Check',disp)
        cv2.waitKey(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
