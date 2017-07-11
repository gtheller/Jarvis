import sys
import os
import numpy as np
import math
import random

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

with open('JH_90_Neural.txt') as f:
    data = [float(i) for i in f.read().split()]


X=[]
Y=[]
for a in range(int(len(data)/10)):
    alpha = data[a:a+8]
    beta = data[a+8:a+13]
    X.append(alpha)
    Y.append(beta)
X=np.array(X)
Y=np.array(Y)

print(X.shape)
print(X)
print()
print(Y.shape)
print(Y)


##num = 100
##for a in range(num):
##    l = []
##    total = 0
##    for b in range(4):
##        temp = random.randint(0,10)
##        l.append(temp)
##        total+=(b+1)*temp
##    X.append(l)
##    Y.append([total])
##print(X)
##print()
##print(Y)
#X = np.array([[0,0],[0,1],[1,0],[1,1]])
#Y = np.array([[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(16, input_dim=8, activation='tanh', use_bias=True))
model.add(Dense(16, activation='tanh'))
model.add(Dense(16, activation='tanh')) #elu worked pretty well
model.add(Dense(5, activation='linear'))

model.compile(optimizer='adam',loss='mean_squared_error', metrics=['accuracy'])

model.fit(X, Y, epochs=100, verbose=2)

i=0
a = random.randint(0,len(data) - 9)
for j in range(8):
    test.append(data[a+j])
for a in range(1):
    sub = test[i:i+8]
    print("sub:")
    print(sub)
    print()
    temp = model.predict(np.array([sub]))
    print("temp:")
    for i in range(5):
        print(temp[0][i])
    print(type(temp[0][0]))
    print()
    data.append(temp[0][0])
    i+=1
