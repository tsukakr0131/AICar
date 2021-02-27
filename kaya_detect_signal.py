#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 04:24:06 2019

@author: Tsukasa
"""

import cv2
import numpy as np

class DetectSignal():
    def __init__(self):
        self.cascade = cv2.CascadeClassifier('./blue_signal.xml')
        self.count = 0

    def blue(self, frame, debug):
        gray = cv2.equalizeHist(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        """
        objects:
        矩形を要素とするベクトル。それぞれの矩形には、検出した物体を含みます。
        scaleFactor:
        画像スケールにおける縮小量を表します。
        minNeighbors:
        物体候補となる矩形は、最低でもこの数だけの近傍矩形を含む必要があります。
        minSize:
        物体が取り得る最小サイズ。これよりも小さい物体は無視されます。
        maxSize:
        物体が取り得る最大サイズ。
        """
        signal = self.cascade.detectMultiScale(gray, scaleFactor=1.11, minNeighbors=1, minSize=(100, 100))
        if len(signal) == 1:
            x, y, w, h = signal[0, :]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            dst = frame[y:y+h, x:x+w]
            print(np.sum(dst[:,:,1])), np.sum(dst[:,:,2])
            if np.sum(dst[:,:,1]) > np.sum(dst[:,:,2]):
                self.count = self.count + 1

        if debug == 1:
            cv2.imshow('DetectSignal', frame)
            cv2.waitKey(1)

        if self.count > 5:
            return True
