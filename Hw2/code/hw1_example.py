# -*- coding: utf-8 -*-

import sys
from hw1_ui import Ui_MainWindow
import cv2
import os
import numpy as np
import glob
from PyQt5.QtWidgets import QMainWindow, QApplication
from decimal import Decimal


class MainWindow(QMainWindow, Ui_MainWindow):
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
        self.btn1_1.clicked.connect(self.on_btn1_1_click)
        self.btn1_2.clicked.connect(self.on_btn1_2_click)
        self.btn1_3.clicked.connect(self.on_btn1_3_click)
        self.btn1_4.clicked.connect(self.on_btn1_4_click)
        self.btn2_1.clicked.connect(self.on_btn2_1_click)
        self.btn3_1.clicked.connect(self.on_btn3_1_click)
        self.btn3_2.clicked.connect(self.on_btn3_2_click)
        self.btn4_1.clicked.connect(self.on_btn4_1_click)
        self.btn4_2.clicked.connect(self.on_btn4_2_click)

    # ---------------------------------- #
    # --------------- Q1 --------------- #
    # ---------------------------------- #
    def on_btn1_1_click(self):
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

    def on_btn1_2_click(self):
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
        

    def on_btn1_3_click(self):
        box_num = int(self.cboxImgNum.currentText()) + 1
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

        for i in range(0,3):
            print(str(rotation_matrix[0][i][0]) + ", " + str(rotation_matrix[0][i][1]) + ", " + str(rotation_matrix[0][i][1]) + ", " + str(tvecs[0][i][0]))
        print()

    def on_btn1_4_click(self):
        images = glob.glob('images/CameraCalibration/*.bmp')
        for fname in images:
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
            objp = np.zeros((11*8,3), np.float32)
            objp[:,:2] = np.mgrid[0:8,0:11].T.reshape(-1,2)

            # Arrays to store object points and image points from all the images.
            objpoints = [] # 3d point in real world space
            imgpoints = [] # 2d points in image plane.
            
            img = cv2.imread(fname)
            # img = cv2.resize(img, (480, 480))
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
        print("-------- 1.4 Distortion Matrix --------")
        print(dist)
        print()


    # ---------------------------------- #
    # --------------- Q2 --------------- #
    # ---------------------------------- #

    def on_btn2_1_click(self):
        
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)





        corners2 = []
        original_images = []
        ar_images = []
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.



        for num in range(1,16):
            fname = "images/CameraCalibration/" + str(num) + ".bmp"
            

            # Arrays to store object points and image points from all the images.
            
            
            img = cv2.imread(fname)
            original_images.append(img)
            # img = cv2.resize(img, (480, 480))
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

        # criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # objp = np.zeros((11*8,3), np.float32)
        # objp[:,:2] = np.mgrid[0:8,0:11].T.reshape(-1,2)

        # axis = np.float32([[0,0,0],[0,2,0],[2,2,0],[2,0,0],
        #                     [0,0,-2], [0,2,-2], [2,2,-2], [2,0,-2]])

        # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        # for num in range(1,6):
        #     fname = "images/CameraCalibration/" + str(num) + ".bmp"
        #     img = cv2.imread(fname)
            
        #     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     ret, corners = cv2.findChessboardCorners(gray, (11,8),None)

        #     if ret == True:
        #         # corners2 = cv2.cornerSubPix(gray,corners,(11,8),(-1,-1),criteria)

        #         # Find the rotation and translation vectors.
        #         # rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)

        #         # project 3D points to image plane
        #         imgpts, jac = cv2.projectPoints(axis, rvecs[num], tvecs[num], mtx, dist)

        #         img = self.draw(img,corners2,imgpts)
        #         # cv2.namedWindow()
        #         cv2.imshow('img',img)
        #         k = cv2.waitKey(500) & 0xff
                # if k == 's':
                #     cv2.imwrite(fname[:6]+'.png', img)

        # cv2.destroyAllWindows()
        # ======================
        def display_ar(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                for img in ar_images:
                    cv2.imshow('AR image', img)
                    cv2.waitKey(500) & 0xFF


        def draw(img, corners, imgpts):
            imgpts = np.int32(imgpts).reshape(-1,2)
            img = cv2.drawContours(img, [imgpts[:4]],-1,(0,0,255),3)
            for i,j in zip(range(4),range(4,8)):
                img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(0,0,255),3)
            img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
            return img

    

        axis = np.float32([[0,0,0], [0,2,0], [2,2,0], [2,0,0],
                   [0,0,-2],[0,2,-2],[2,2,-2],[2,0,-2] ])

        cv2.namedWindow('AR image',cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('AR image', display_ar)

        for index, image in enumerate(original_images[0:5]):
            
            imgpts, jac = cv2.projectPoints(axis, rvecs[index], tvecs[index], mtx, dist)
            image = draw(image,corners2,imgpts)
            ar_images.append(image)
            cv2.imshow('AR image',image)
            cv2.waitKey(500) & 0xFF 



    # ---------------------------------- #
    # --------------- Q3 --------------- #
    # ---------------------------------- #

    def on_btn3_1_click(self):
        # edtAngle, edtScale. edtTx, edtTy to access to the ui object
        fname = 'images/OriginalTransform.png'

        img = cv2.imread(fname)
        shape = img.shape

        M = cv2.getRotationMatrix2D((130,125), 
                                     float(self.edtAngle.text()), 
                                     float(self.edtScale.text()))
        
        dst = cv2.warpAffine(img, M, (shape[1], shape[0]))

        M = np.float32([[1, 0, float(self.edtTx.text())], [0, 1, float(self.edtTy.text())]])
        dst = cv2.warpAffine(dst, M, (shape[1], shape[0]))

        cv2.imshow('img', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        

    def on_btn3_2_click(self):
        count = 0
        self._image = cv2.imread('images/OriginalPerspective.png')
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',self.q3_2_onclick)
        cv2.imshow("image", self._image)
        cv2.waitKey(0)
        self._count = 0
        self._image = None
        self._arrPoint = []

    # ---------------------------------- #
    # --------------- Q4 --------------- #
    # ---------------------------------- #

    def on_btn4_1_click(self):
        imgL = cv2.imread('images/imL.png',0)
        imgR = cv2.imread('images/imR.png',0)

        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        disparity = stereo.compute(imgL,imgR)
        disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('Without L-R Disparity Check',disp)
        cv2.waitKey(0)

    def on_btn4_2_click(self):
        imgL = cv2.imread('images/imL.png',0)
        imgR = cv2.imread('images/imR.png',0)

        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        stereo.setDisp12MaxDiff(-1)
        disparity = stereo.compute(imgL,imgR)
        disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        stereo2 = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        stereo2.setDisp12MaxDiff(1)
        disparity2 = stereo2.compute(imgL,imgR)
        disp2 = cv2.normalize(disparity2, disparity2, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        backtorgb = cv2.cvtColor(disp, cv2.COLOR_GRAY2RGB)
        differences = np.subtract(disp, disp2)
        x, y = differences.nonzero()
        backtorgb[x, y] = [0,0,255]

        cv2.imshow('Without L-R Disparity Check',disp)
        cv2.imshow('With L-R Disparity',disp2)
        cv2.imshow('Mark the diff.',backtorgb)
        cv2.waitKey(0)


    ### ### ###

    def draw(self, img, corners, imgpts):
        imgpts = np.int32(imgpts).reshape(-1,2)

        # draw ground floor in green
        img = cv2.drawContours(img, [imgpts[:4]],-1,(0,0,255),3)

        # draw pillars in blue color
        for i,j in zip(range(4),range(4,8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(0,0,255),3)

        # draw top layer in red color
        img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

        return img

    def q3_2_onclick(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._count += 1
            cv2.circle(self._image, (x, y), 5, (0, 0, 255), -1)
            self._arrPoint.append([x,y])
            print(self._arrPoint)
            print(self._count)
            cv2.imshow("image", self._image)
            if(self._count == 4):
                src = np.float32([self._arrPoint[0], self._arrPoint[1], self._arrPoint[2], self._arrPoint[3]])
                dst = np.float32([[20, 20], [450, 20], [450, 450], [20, 450]])
                matrix = cv2.getPerspectiveTransform(src, dst)
                result = cv2.warpPerspective(self._image, matrix, (450, 450))
                cv2.imshow("image2", result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    os.system("clear")
    sys.exit(app.exec_())
