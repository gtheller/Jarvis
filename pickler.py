import sys
import os
import numpy as np
import math
import random
import cv2
from pickle import dump

letter = "abcdefghijklmnopqrstuvwxyz"
inData = np.zeros((1430,256))   #input training data
outData = np.zeros((1430,1))    #output training data
index=0
basedir = 'C:/Jarvis/Hnd'
for typ in os.listdir(basedir): #upper, lower, numbers
    for folder in os.listdir(basedir+"/"+typ):  #a,b,c,...
        i=0
        for file in os.listdir(basedir+"/"+typ+"/"+folder): #actual images
            print(basedir+"/"+typ+"/"+folder+"/"+file)
            i+=1
            img = cv2.imread(basedir+"/"+typ+"/"+folder+"/"+file)   #create cv2 images
            x0 = img.shape[1]   #define borders
            x1 = 0
            y0 = img.shape[0]
            y1 = 0
            for y in range(img.shape[0]):   #calculate borders to crop
                for x in range(img.shape[1]):
                    pixel = img[y,x]
                    gray = .3*pixel[0] + .59*pixel[1] + .11*pixel[2]
                    if(gray<150):           #if black enough
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
            img = img[y0:y1,x0:x1]  #crop
            img = cv2.resize(img,(16,16))   #resize
            #tempData = np.zeros(256)
            i = 0
            for y in range(img.shape[0]):   #create integer matrix from image pixels
                for x in range(img.shape[1]):
                    if img[y,x][0] == 0:
                        inData[index][i] = 1
                    i+=1
            outData[index][0] = float(letter.index(folder))/25  #output data is float between 0 and 1 correspoding to letter
            print(outData[index][0])
            index+=1

            iOut = open('input_2.pkl' , 'wb')   #pickle input training data
            dump(inData,iOut,protocol=2)
            iOut.close()

            oOut = open('output_2.pkl' , 'wb')  #pickle output data
            dump(outData,oOut,protocol=2)
            oOut.close()

            cv2.imwrite("C:/Jarvis/Small/"+typ+"/"+folder+"/"+file, img)    #save 16x16 image
            #cv2.imshow('image', img)
            #cv2.waitKey()

iOut = open('input.pkl' , 'wb')     #final pickel just cuz
dump(inData,iOut,protocol=2)
iOut.close()

oOut = open('output.pkl' , 'wb')
dump(outData,oOut,protocol=2)
oOut.close()
