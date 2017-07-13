import sys
import os
import numpy as np
import math
import random
import cv2
from pickle import dump

letter = "abcdefghijklmnopqrstuvwxyz"                           ########ignore for now, this is just pickler but uses the small images instead of creating them. I was impatient.
inData = np.zeros((1430,256))
outData = np.zeros((1430,1))
index=0
basedir = 'C:/Jarvis/Small'
for typ in os.listdir(basedir):
    for folder in os.listdir(basedir+"/"+typ):
        for file in os.listdir(basedir+"/"+typ+"/"+folder):
            print(basedir+"/"+typ+"/"+folder+"/"+file)
            img = cv2.imread(basedir+"/"+typ+"/"+folder+"/"+file)
            i = 0
            for y in range(img.shape[0]):
                temp = ""
                for x in range(img.shape[1]):
                    if img[y,x][0] == 0:
                        inData[index][i] = 1
                    temp+=str(int(inData[index][i]))+" "
                    i+=1
                print(temp)
            print()
            outData[index][0] = float(letter.index(folder))/25
            print(outData[index][0])
            index+=1

            iOut = open('input_2.pkl' , 'wb')
            dump(inData,iOut,protocol=2)
            iOut.close()

            oOut = open('output_2.pkl' , 'wb')
            dump(outData,oOut,protocol=2)
            oOut.close()

            cv2.imwrite("C:/Jarvis/Small/"+typ+"/"+folder+"/"+file, img)
            #cv2.imshow('image', img)
            #cv2.waitKey()

iOut = open('input.pkl' , 'wb')
dump(inData,iOut,protocol=2)
iOut.close()

oOut = open('output.pkl' , 'wb')
dump(outData,oOut,protocol=2)
oOut.close()
