#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:43:40 2020

@author: shailesh
"""

import keras.backend as K
from keras.models import Model
from keras.layers import Input, Dense
from keras import metrics
import helpers

xPath = "Data/ScoreData/inputs.txt"
yPath = "Data/ScoreData/labels.txt"

X = helpers.readInputData(xPath)
Y = helpers.readLabels(yPath)

inputs = Input(shape=(768,))
layer1 = Dense(2048, activation='relu')(inputs)
layer2 = Dense(2048, activation='relu')(layer1)
layer3 = Dense(2048, activation='relu')(layer2)
output = Dense(1, activation='relu')(layer2)
model = Model(inputs=inputs, outputs=output)

def custom_loss(layer):			##add penalty for wrong sign in the future

    
    def loss(y_true,y_pred):
        return K.mean(K.square(y_pred - y_true) + K.square(layer), axis=-1)
   
    # Return a function
    return loss
    
# Compile the model
model.compile(optimizer='adam',
              loss=custom_loss(output), # Call the loss function with the selected layer
              metrics=[metrics.mae])

# train
model.fit(X, Y)