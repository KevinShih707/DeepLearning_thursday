import sys
from PyQt5.QtWidgets import QDialog, QApplication
from problem5 import Ui_Problem_5    #test .py file name
import numpy as np
import os
import cv2
import math
import glob
from matplotlib import pyplot as plt

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Problem_5()
        self.ui.setupUi(self)
        self.clickBinding()
        
    #button handler
    def clickBinding(self):
        self.ui.button_1_1.clicked.connect(self.button_1_1_click)
        self.ui.button_1_2.clicked.connect(self.button_1_2_click)
        self.ui.button_1_3.clicked.connect(self.button_1_3_click)
        self.ui.button_ok.clicked.connect(self.button_ok_click)
        self.ui.button_cancel.clicked.connect(self.button_cancel_click)

    def button_1_1_click(self):
        images = glob.glob('images/CameraCalibration/*.bmp')
        for fname in images:
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
            objp = np.zeros((8*11,3), np.float32)
            objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

            # Arrays to store object points and image points from all the images.
            objpoints = [] # 3d point in real world space
            imgpoints = [] # 2d points in image plane.

            img = cv2.imread(fname)
            img = cv2.resize(img, (480, 480))
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, (11, 8),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray,corners,(11,8),(-1,-1),criteria)
                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, (11, 8), corners2,ret)
                cv2.imshow(fname,img)
        
        cv2.waitKey(0)

        cv2.destroyAllWindows()
    
    def button_1_2_click(self):
        images = glob.glob('images/CameraCalibration/*.bmp')
        for fname in images:
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
            objp = np.zeros((8*11,3), np.float32)
            objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

            # Arrays to store object points and image points from all the images.
            objpoints = [] # 3d point in real world space
            imgpoints = [] # 2d points in image plane.

            img = cv2.imread(fname)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, (11, 8),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray,corners,(11,8),(-1,-1),criteria)
                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, (11, 8), corners2,ret)


        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        print("-------- 1.2 Intrinsic Matrix --------")
        print(mtx)
        print()

        self.ui.label_output_title.setText("-------- 1.2 Intrinsic Matrix --------")
        self.ui.label_output.setText(str(mtx))
    
    def button_1_3_click(self):
        box_num = int(self.ui.comboBox_1_3.currentText()) + 1
        fname = 'images/CameraCalibration/' + str(box_num) + '.bmp'

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.        
        
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (11, 8),None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray,corners,(11,8),(-1,-1),criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (11, 8), corners2,ret)


        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

        rotation_matrix = cv2.Rodrigues(rvecs[0])

        print("-------- 1.3 Extrinsic Matrix --------")

        label_print = ""
        for i in range(0,3):
            label_print+=(str(round(rotation_matrix[0][i][0],5)) + ", " + str(round(rotation_matrix[0][i][1],5)) + ", " + str(round(rotation_matrix[0][i][1],5)) + ", " + str(round(tvecs[0][i][0],5))+"\n")

        for i in range(0,3):
            print(str(rotation_matrix[0][i][0]) + ", " + str(rotation_matrix[0][i][1]) + ", " + str(rotation_matrix[0][i][1]) + ", " + str(tvecs[0][i][0]))
        print()

        self.ui.label_output_title.setText("-------- 1.3 Extrinsic Matrix --------")
        self.ui.label_output.setText(label_print)


    def button_ok_click(self):
        sys.exit(app.exec_())
    
    def button_cancel_click(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())