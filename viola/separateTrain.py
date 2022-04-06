
import os
from pickle import TRUE
from PIL import Image

roundName ="wider_face_train_bbx_gt.txt"
with open(roundName, "r") as readTruthFile:
    while True:
        file_name = readTruthFile.readline()
        if file_name == '':
            print('End Of File')
            break
        noLineBreak = file_name.rstrip()
        image = Image.open('images/'+noLineBreak)
        # summarize some details about the image
        [xSize, ySize] = image.size
        fileWithoutExtension = noLineBreak.replace('.jpg', '.txt')
        [imageFolder,imageName] = fileWithoutExtension.split('/')
        os.makedirs('labels/' + imageFolder, exist_ok=True)
        with open('labels/' + fileWithoutExtension, 'w') as fileWriter:
            numberOfFaces = readTruthFile.readline().rstrip()
            count = 0
            while (count < int(numberOfFaces)):
                count = count + 1
                facePrediction = readTruthFile.readline().rstrip()
                groundTruth = facePrediction.split(' ')[:4]
                xc= (int(groundTruth[0]) + (int(groundTruth[2])/2))/xSize
                yc= (int(groundTruth[1]) + (int(groundTruth[3])/2))/ySize
                w= ((int(groundTruth[2])/2))/xSize
                h= ((int(groundTruth[3])/2))/ySize
                fileWriter.write('0 '+ str(xc) + ' ' + str(yc) + ' '+ str(w) + ' '+ str(h))
                fileWriter.write('\r')
        fileWriter.close()
readTruthFile.close

