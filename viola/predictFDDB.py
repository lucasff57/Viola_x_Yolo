from saveImg import saveImg
from writeOutSeparateFDDB import writeOutSeparateFDDB
import cv2 as cv
from viola import viola
from saveImg import saveImg



countArch = 0
while (countArch < 10):
    countArch = countArch + 1
    roundName ='FDDB/FDDB-fold-' + str(countArch) + '.txt'

    with open(roundName, "r") as readFiles:
        for image in readFiles:
            noLineBreak = image.rstrip()
            imageSplitNames = noLineBreak.split('/')[0:5]
            filePath = r'C:/Users/T-GAMER/Desktop/TCC/viola/images/' + noLineBreak +'.jpg'
            original_image = cv.imread(filePath)
            teste = viola(original_image)
            writeOutSeparateFDDB(imageSplitNames[4], teste, str(countArch))
            saveImg(original_image,imageSplitNames[4],teste)
                
            
        readFiles.close()
    