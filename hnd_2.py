import os
import sys
from pickle import dump
from pickle import load

inData = load(open('input.pkl' , 'rb' ))
for a in range(10):
    i = 0
    for b in range(16):
        temp = ""
        for c in range(16):
            temp+=str(int(inData[a][i]))+" "
            i+=1
        print(temp)
    print()
