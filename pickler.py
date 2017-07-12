import sys
import os
import numpy as np
import math
import random
import cv2
from pickle import dump

inData = np.zeros((1430,256))
outData = np.zeros((1430,1))
index=0
basedir = 'C:/Jarvis/Hnd'
for typ in os.listdir(basedir):
    for folder in os.listdir(basedir+"/"+typ):
        i=0
        for file in os.listdir(basedir+"/"+typ+"/"+folder):
            i+=1
            img = cv2.imread(basedir+"/"+typ+"/"+folder+"/"+file)
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
            #tempData = np.zeros(256)
            i = 0
            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    if img[y,x][0] == 0:
                        inData[index][i] = 1
                        outData[index] = file
                    i+=1
            index+=1
            print(inData)

            iOut = open('input.pkl' , 'wb')
            dump(inData,iOut,protocol=2)
            iOut.close()

            oOut = open('output.pkl' , 'wb')
            dump(outData,oOut,protocol=2)
            oOut.close()

            cv2.imwrite("C:/Jarvis/Small/"+typ+"/"+folder+"/"+file, img)
            #cv2.imshow('image', img)
            #cv2.waitKey()
print(inData)

dOut = open('input.pkl' , 'wb')
dump(inData,dOut,protocol=2)
dOut.close()
