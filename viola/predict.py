from viola import viola
from writeOutSeparate import writeOutSeparate
from saveImg import saveImg
import cv2 as cv

roundName ="validationImageList.txt"
with open(roundName, "r") as readFiles:
    for image in readFiles:
        noLineBreak = image.rstrip()
        [imageFolder,imageName] = noLineBreak.split('/')
        filePath = r'C:/Users/T-GAMER/Desktop/TCC/viola/WIDER_train/images/' + noLineBreak
        original_image = cv.imread(filePath)
        teste = viola(original_image)
        writeOutSeparate(imageName,teste)
        #saveImg(original_image,imageName,teste)
            
        
    readFiles.close()