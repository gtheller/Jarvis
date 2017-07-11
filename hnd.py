import sys
import os
import numpy as np
import math
import random
import cv2

#import keras
#from keras.models import Sequential
#from keras.layers import Dense, Activation

#inData = [ [[1,...,16],[1,...,16]] , [[1,...,16],[1,...,16]], [[1,...,16],[1,...,16]], ... ]

basedir = 'C:/Jarvis/Hnd/Img'
for typ in os.listdir(basedir):
    for folder in os.listdir(basedir+"/"+typ):
        i=0
        for file in os.listdir(basedir+"/"+typ+"/"+folder):
            #os.rename(basedir+"/"+typ+"/"+folder+"/"+file, basedir+"/"+typ+"/"+folder+"/"+str(i)+".png")
            i+=1
            img = cv2.imread(basedir+"/"+typ+"/"+folder+"/"+file)
            print(basedir+"/"+typ+"/"+folder+"/"+file)
            x0 = img.shape[1]
            x1 = 0
            y0 = img.shape[0]
            y1 = 0
            for y in range(img.shape[0]):
                    for x in range(img.shape[1]):
                        pixel = img[y,x]
                        gray = .3*pixel[0] + .59*pixel[1] + .11*pixel[2]
                        if(gray<150):
                            img[y,x] = [0,0,0]
                            if x<x0:
                                x0=x
                            if x>x1:
                                x1=x
                            if y<y0:
                                y0=y
                            if y>y1:
                                y1=y
                        else:
                            img[y,x] = [255,255,255]
            img = img[y0:y1,x0:x1]
            img = cv2.resize(img,(16,16))
            tempData = np.zeros(256)
            i = 0
            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    if img[y,x][0] == 0:
                        tempData[i] = 1
                    i+=1
            print(tempData)
            #cv2.imshow('image', img)
            #cv2.waitKey()

exit(0)

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
