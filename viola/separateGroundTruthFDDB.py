

import sys, os
import numpy as np
from math import *
import math

from PIL import Image

import cv2
import os


def filterCoordinate(c,m):
    if c < 0:
        return 0
    elif c > m:
        return m
    else:
        return c

countArch = 0
while (countArch < 10):
    countArch = countArch + 1
    roundName ='data/FDDB/FDDB-fold-' + str(countArch) + '-ellipseList.txt'
    print(roundName)
    with open(roundName, "r") as readTruthFile:
        while True:
            file_name = readTruthFile.readline()
            if file_name == '':
                print('End Of File')
                break
            noLineBreak = file_name.rstrip()
            img = Image.open('data/images/'+noLineBreak+'.jpg')
            w = img.size[0]
            h = img.size[1]
            imageSplitNames = noLineBreak.split('/')[0:5]
            with open('groundtruthsFDDB/' + imageSplitNames[4] + 'Round' +str(countArch) + '.txt', 'w') as fileWriter:
                numberOfFaces = readTruthFile.readline().rstrip()
                count = 0
                while (count < int(numberOfFaces)):
                    count = count + 1
                    facePrediction = readTruthFile.readline().rstrip()
                    ellipse = facePrediction.split(' ')
                    a = float(ellipse[0])
                    b = float(ellipse[1])
                    angle = float(ellipse[2])
                    centre_x = float(ellipse[3])
                    centre_y = float(ellipse[4])
                    
                    tan_t = -(b/a)*tan(angle)
                    t = atan(tan_t)
                    x1 = centre_x + (a*cos(t)*cos(angle) - b*sin(t)*sin(angle))
                    x2 = centre_x + (a*cos(t+pi)*cos(angle) - b*sin(t+pi)*sin(angle))
                    x_max = filterCoordinate(max(x1,x2),w)
                    x_min = filterCoordinate(min(x1,x2),w)
                    
                    if tan(angle) != 0:
                        tan_t = (b/a)*(1/tan(angle))
                    else:
                        tan_t = (b/a)*(1/(tan(angle)+0.0001))
                    t = atan(tan_t)
                    y1 = centre_y + (b*sin(t)*cos(angle) + a*cos(t)*sin(angle))
                    y2 = centre_y + (b*sin(t+pi)*cos(angle) + a*cos(t+pi)*sin(angle))
                    y_max = filterCoordinate(max(y1,y2),h)
                    y_min = filterCoordinate(min(y1,y2),h)
                
                    text = str(x_min) + ' ' + str(y_min) + ' ' + str(abs(x_max-x_min)) + ' ' + str(abs(y_max-y_min))
                    #elipsis 
                    fileWriter.write(text)
                    fileWriter.write('\n')
            fileWriter.close()
    readTruthFile.close


