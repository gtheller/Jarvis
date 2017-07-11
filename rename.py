import sys
import os

basedir = 'C:/Jarvis/Fnt'
name = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
i = 0
for f in os.listdir(basedir):
    if f=="Lower" or f=="Numbers" or f=="Upper":
        continue
    if i<=25:
        os.rename(basedir+"/"+f,basedir+"/Upper/"+name[i])
    else:
        os.rename(basedir+"/"+f,basedir+"/Lower/"+name[i])
    i+=1
