from viola import viola
from writeOut import writeOut
from saveImg import saveImg
import cv2 as cv
import os
import shutil

roundName ="trainSet.txt"
with open(roundName, "r") as readFiles:
    for image in readFiles:
        noLineBreak = image.rstrip()
        [imageFolder,imageName] = noLineBreak.split('/')
        filePath = 'WIDER_train/images/' + noLineBreak
        with open('result' + roundName, 'a') as fileWriter:

            original_image = cv.imread(filePath)
            teste = viola(original_image)
            writeOut(fileWriter,noLineBreak,teste)
            #saveImg(original_image,imageName,teste)
            
            fileWriter.close()
    readFiles.close()