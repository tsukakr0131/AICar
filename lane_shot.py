# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:43:02 2019

@author: Tsukasa
"""

import cv2
import readchar

#webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # カメラ画像の縦幅を720に設定

#movie
#cap = cv2.VideoCapture('./test.avi')

#image
#frame = cv2.imread('./test.jpg')
img_l = 0
img_c = 0
img_r = 0

while True:
    kb = readchar.readchar()
    ret, frame = cap.read()
    #cv2.imshow('now_image', frame)
    #k = cv2.waitKey(5)
    if kb == 'l':
        #frame = cv2.resize(frame, (1280,720))
        cv2.imshow('shotted_image_L', frame)
        k = cv2.waitKey(5)
        cv2.imwrite('./lane_train/img_l/' + str(img_l) + ".png",frame)
        print('imageL'+ str(img_l) + 'shotted')
        img_l = img_l + 1
    elif kb == 'c':
        cv2.imshow('shoted_image_C', frame)
        k = cv2.waitKey(5)
        cv2.imwrite('./lane_train/img_c/' + str(img_c) + ".png",frame)
        print('imageC'+ str(img_c) + 'shotted')
        img_c = img_c + 1
    elif kb == 'r':
        cv2.imshow('shotted_image_R', frame)
        k = cv2.waitKey(5)
        cv2.imwrite('./lane_train/img_r/' + str(img_r) + ".png",frame)
        print('imageR'+ str(img_r) + 'shotted')
        img_r = img_r + 1
    elif kb == 'p':
        break
