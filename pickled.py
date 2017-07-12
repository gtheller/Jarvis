import os
import sys
from pickle import dump
from pickle import load

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

inData = load(open('input.pkl' , 'rb' ))
outData = load(open('output.pkl' , 'rb' ))
print(str(type(inData)) + " "  + str(type(outData)))
for a in range(10):
    i = 0
    for b in range(16):
        temp = ""
        for c in range(16):
            temp+=str(int(inData[a][i]))+" "
            i+=1
        print(temp)
    print(outData[a][0])
    print()

model = Sequential()
model.add(Dense(16, input_dim=256, activation='tanh', use_bias=True))
model.add(Dense(200, activation='tanh'))
model.add(Dense(100, activation='tanh'))
model.add(Dense(1, activation='softmax'))

model.compile(optimizer='adam',loss='mean_squared_error', metrics=['accuracy'])
print(outData[1])
model.fit(inData, outData, epochs=100, verbose=2)

print(model.predict(inData[3]))
