#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 04:24:06 2019

@author: Tsukasa
"""

import Jetson.GPIO as GPIO
import Adafruit_PCA9685

class KayaMotorController():
    def __init__(self):
        self.ll = 11
        self.lr = 12
        self.lp = 0
        self.cl = 15
        self.cr = 16
        self.cp = 1
        self.rl = 21
        self.rr = 22
        self.rp = 2
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ll, GPIO.OUT)
        GPIO.setup(self.lr, GPIO.OUT)
        GPIO.setup(self.cl, GPIO.OUT)
        GPIO.setup(self.cr, GPIO.OUT)
        GPIO.setup(self.rl, GPIO.OUT)
        GPIO.setup(self.rr, GPIO.OUT)



    def left(self, l):
        if l > 0:
            GPIO.output(self.ll, True)
            GPIO.output(self.lr, False)
            self.pwm.set_pwm(self.lp, 0, l * 15)
        elif l < 0:
            GPIO.output(self.ll, False)
            GPIO.output(self.lr, True)
            self.pwm.set_pwm(self.lp, 0, l * -15)
        elif l == 0:
            GPIO.output(self.ll, False)
            GPIO.output(self.lr, False)
            self.pwm.set_pwm(self.lp, 0, 0)

    def center(self, c):
        if c > 0:
            GPIO.output(self.cl, True)
            GPIO.output(self.cr, False)
            self.pwm.set_pwm(self.cp, 0, c * 15)
        elif c < 0:
            GPIO.output(self.cl, False)
            GPIO.output(self.cr, True)
            self.pwm.set_pwm(self.cp, 0, c * -15)
        elif c == 0:
            GPIO.output(self.cl, False)
            GPIO.output(self.cr, False)
            self.pwm.set_pwm(self.cp, 0 ,0)

    def right(self, r):
        if r > 0:
            GPIO.output(self.rl, True)
            GPIO.output(self.rr, False)
            self.pwm.set_pwm(self.rp, 0, r * 15)
        elif r < 0:
            GPIO.output(self.rl, False)
            GPIO.output(self.rr, True)
            self.pwm.set_pwm(self.rp, 0, r * -15)
        elif r == 0:
            GPIO.output(self.rl, False)
            GPIO.output(self.rr, False)
            self.pwm.set_pwm(self.rp, 0, 0)


    def clean(self):
        self.pwm.set_pwm(self.lp, 0, 0)
        self.pwm.set_pwm(self.cp, 0, 0)
        self.pwm.set_pwm(self.rp, 0, 0)
        GPIO.cleanup()
