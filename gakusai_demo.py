# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:43:02 2019

@author: Tsukasa
"""
wait_time = 20
import time
import cnn_model
import keras
#import matplotlib.pyplot as plt
import numpy as np
import cv2
from time import sleep
from kaya_angle_control import KayaAngleController

angle_control = KayaAngleController()
model=cnn_model.get_model((32,32,3),6)#画像のshape、ラベルデータの数
model.load_weights("./kaya_detect_lane.hdf5")
#webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360) # カメラ画像の縦幅を720に設定
count = 0
count_flg = 0
angle = 0
power = 0
print('start')

while True:
    ret, frame = cap.read()
    x=(np.asarray(cv2.cvtColor(cv2.resize(frame, (32,32)), cv2.COLOR_BGR2RGB)).reshape(-1,32,32,3))/255
    #pre 0:C, 1:L, 2:R  Predict:%
    per = model.predict([x])[0][model.predict([x])[0].argmax()]
    if per > 0.8:
        vector = model.predict([x])[0].argmax()
        power = 100
        #Left
        if vector == 0:
            left = 50
            right = -100
            count_flg = 0
        #Center
        elif vector == 1:
            angle = 0
            left = 100
            right = -100
            count_flg = 0
        #Right
        elif vector == 2:
            left = 100
            right = -50
            count_flg = 0
        #Wall
        elif vector == 3:
            angle = 90
            left = 0
            right = 0
            count_flg = 0
        #Recovery
        elif vector == 4:
            angle = -90
            left = 0
            right = 0
            count_flg = 0
        #Stop
        elif vector == 5:
            if count_flg == 30:
                sleep(2)
                angle = 0
                left = 100
                right = -100
                count_flg = 0
                
                angle_control.angle(left, right, angle, power)
                sleep(2)
                print('aaaaaaaaaaaaaaaaa')
            else:
                count_flg += 1
                power = 0
                left = 0
                right = 0
    else:
        left = 0
        right = 0
        angle = 0
        power = 80
    print(left, right, angle, per)
    angle_control.angle(left, right, angle, power)
