import os
import sys
from pickle import dump
from pickle import load
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

inData = load(open('input_2.pkl' , 'rb' ))  #load pickled training data
outData = load(open('output_2.pkl' , 'rb' ))
print(inData)
print(outData)
print(type(inData))
print(type(outData))
print(inData.shape)
print(outData.shape)
for a in range(10):     #print data to make sure it looks right
    i = 0
    for b in range(16):
        temp = ""
        for c in range(16):
            temp+=str(int(inData[a][i]))+" "
            i+=1
        print(temp)
    print(outData[a])
    print(outData[a][0])
    print()

model = Sequential()    #instantiate network
model.add(Dense(200, input_dim=256, activation='tanh', use_bias=True))  #first layer of 200, input layer also defined (256)
model.add(Dense(100, activation='tanh'))    #2nd layer, 100 nodes
model.add(Dense(1, activation='tanh'))  #output layer, not sure what activation function is best

##testData = []
##for a in inData[3]:
##    testData.append(float(a))
##print(testData)
##print(type(testData))
##print(type(testData[0]))

model.compile(optimizer='sgd',loss='mean_squared_error', metrics=['accuracy'])  #important step I think
model.fit(inData, outData, epochs=16, verbose=2)    #train network
testData = np.reshape(inData[3], (-1,256))  #didn't work until I did this idk
print(model.predict(testData))  #testing with some training data for now
