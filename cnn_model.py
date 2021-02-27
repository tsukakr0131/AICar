# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:43:02 2019

@author: Tsukasa
"""

import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras.optimizers import RMSprop

def def_model(in_shape,nb_classes):
    model=Sequential()
    model.add(Conv2D(32,
                    kernel_size=(3,3),
                    activation="relu",
                    input_shape=in_shape))
    model.add(Conv2D(32,(3,3),activation="relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64,(3,3),activation="relu"))
    model.add(Conv2D(64,(3,3),activation="relu",name="relu_conv2"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(512,activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes,activation="softmax"))

    return model

def get_model(in_shape,nb_classes):
    model=def_model(in_shape,nb_classes)
    model.compile(
        loss="categorical_crossentropy",
        optimizer=RMSprop(),
        metrics=["accuracy"])
    return model
