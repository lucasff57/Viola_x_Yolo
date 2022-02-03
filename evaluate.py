from IoU import bb_intersection_over_union

roundName ="trainEvalSet.txt"

totalFaces = 0
totalPredictedFaces = 0
totalGoodFaces = 0
oldFileName = ''

with open(roundName, "r") as readTruthFile:
    with open('evaluation_' + roundName, 'w') as resultFileWriter:
        while True:
            file_name = readTruthFile.readline()
            if file_name == '':
                print('End Of File')
                break
            numberOfFaces = readTruthFile.readline().rstrip()
            totalFaces = totalFaces + int(numberOfFaces)
            count = 0
            while (count < int(numberOfFaces)):
                count = count + 1
                facePrediction = readTruthFile.readline().rstrip()
                groundTruth = facePrediction.split(' ')
                with open('result_' + roundName, 'r') as predictedData:
                    searchlines = predictedData.readlines()
                    for i, line in enumerate(searchlines):
                        if file_name in line: 
                            predictionCount = 0
                            highestIoU = 0
                            if oldFileName != file_name:
                                totalPredictedFaces = totalPredictedFaces + int(searchlines[i+1])
                                oldFileName = file_name
                            while (predictionCount < int(searchlines[i+1])):
                                [x1p, y1p, wp, hp]  = searchlines[i+2+predictionCount].split(' ')
                                iou = bb_intersection_over_union([int(x1p), int(y1p), int(x1p) + int(wp), int(y1p) + int(hp)], [int(groundTruth[0]), int(groundTruth[1]), int(groundTruth[0]) + int(groundTruth[2]), int(groundTruth[1]) + int(groundTruth[3])])
                                if iou > highestIoU:
                                    highestIoU = iou
                                predictionCount = predictionCount + 1
                            if highestIoU >= 0.5:
                                totalGoodFaces = totalGoodFaces + 1
                            resultFileWriter.write(str(highestIoU))
                            resultFileWriter.write('\n')
                            break
                    predictedData.close()
                    
                    
                    
        resultFileWriter.write('\n')
        resultFileWriter.write('total good faces = ' + str(totalGoodFaces))     
        resultFileWriter.write('\n')
        resultFileWriter.write('total predicted = ' + str(totalPredictedFaces))     
        resultFileWriter.write('\n')
        resultFileWriter.write('total = ' + str(totalFaces))       
        resultFileWriter.close()
    readTruthFile.close()