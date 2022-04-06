


import os
import cv2
import numpy as np

def xywh2xxyy(box):
	x1 = box[0]
	y1 = box[1]
	x2 = box[0] + box[2]
	y2 = box[1] + box[3]
	return (x1, x2, y1, y2)

def convert(size, box):
	dw = 1. / (size[0])
	dh = 1. / (size[1])
	x = (box[0] + box[1]) / 2.0 - 1
	y = (box[2] + box[3]) / 2.0 - 1
	w = box[1] - box[0]
	h = box[3] - box[2]
	x = x * dw
	w = w * dw
	y = y * dh
	h = h * dh
	return (x, y, w, h)

ignore_small = 0
roundName ="wider_face_train_bbx_gt.txt"
with open(roundName, "r") as readTruthFile:
    while True:
        file_name = readTruthFile.readline()
        if file_name == '':
            print('End Of File')
            break
        noLineBreak = file_name.rstrip()
        fileWithoutExtension = noLineBreak.replace('.jpg', '.txt')
        img = cv2.imread('trainFace/images/'+ noLineBreak)
        height, width, _ = img.shape
        
        [imageFolder,imageName] = fileWithoutExtension.split('/')
        if not os.path.exists('trainFace/labelV2/'+ imageFolder):
            os.makedirs('trainFace/labelV2/'+imageFolder)        
        with open('trainFace/labelV2/' + fileWithoutExtension, 'w') as fileWriter:
            numberOfFaces = readTruthFile.readline().rstrip()
            count = 0
            while (count < int(numberOfFaces)):
                count = count + 1
                facePrediction = readTruthFile.readline().rstrip()
                box = np.array(facePrediction.split()[0:4], dtype=np.float32) # (x1,y1,w,h)
                if box[2] < ignore_small or box[3] < ignore_small:
                    continue
                box = convert((width, height), xywh2xxyy(box))
                fileWriter.write('0 {} {} {} {}'.format(round(box[0],4), round(box[1],4), round(box[2],4), round(box[3],4)))
                fileWriter.write('\n')
        fileWriter.close()
readTruthFile.close


