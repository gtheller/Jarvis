import sys
import os

basedir = 'C:/Jarvis/Hnd/Img_2'
for typ in os.listdir(basedir):
    for folder in os.listdir(basedir+"/"+typ):
        i=0
        for file in os.listdir(basedir+"/"+typ+"/"+folder):
            os.rename(basedir+"/"+typ+"/"+folder+"/"+file, basedir+"/"+typ+"/"+folder+"/"+str(i)+".png")
            i+=1
