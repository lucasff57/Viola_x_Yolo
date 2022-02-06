


roundName ="validationGT.txt"
with open(roundName, "r") as readTruthFile:
    while True:
        file_name = readTruthFile.readline()
        if file_name == '':
            print('End Of File')
            break
        noLineBreak = file_name.rstrip()
        fileWithoutExtension = noLineBreak.replace('.jpg', '.txt')
        [imageFolder,imageName] = fileWithoutExtension.split('/')
        with open('groundtruths/' + imageName, 'w') as fileWriter:
            numberOfFaces = readTruthFile.readline().rstrip()
            count = 0
            while (count < int(numberOfFaces)):
                count = count + 1
                facePrediction = readTruthFile.readline().rstrip()
                groundTruth = facePrediction.split(' ')
                fileWriter.write(' '.join(str(int(x)) for x in groundTruth[:4]))
                fileWriter.write('\n')
        fileWriter.close()
readTruthFile.close


