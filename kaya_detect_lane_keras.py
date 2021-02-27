# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:43:02 2019

@author: Tsukasa
"""

import cnn_model
import keras
#import matplotlib.pyplot as plt
import numpy as np
import cv2

from kaya_angle_control import KayaAngleController

angle_control = KayaAngleController()
model=cnn_model.get_model((32,32,3),6)#画像のshape、ラベルデータの数
model.load_weights("./kaya_detect_lane.hdf5")
#webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

angle = 0
power = 0
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
        #Center
        elif vector == 1:
            angle = 0
            left = 100
            right = -100
        #Right
        elif vector == 2:
            left = 100
            right = -50
        #Wall
        elif vector == 3:
            angle = 90
            left = 0
            right = 0
        #Recovery
        elif vector == 4:
            angle = -90
            left = 0
            right = 0
        #Stop
        elif vector == 5:
            power = 0
            left = 0
            right = 0
        print(vector, per)
    else:
        left = 0
        right = 0
        angle = 0
        power = 80
    #print(left, right, angle, per)
    angle_control.angle(left, right, angle, power)
