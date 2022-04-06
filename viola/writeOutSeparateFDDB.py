def writeOutSeparateFDDB(fileName: str, predictions, roundNumber) -> None:
    with open('detectionsFDDB/' + fileName + 'Round'+ roundNumber +'.txt', 'w') as fileWriter:
        for boundingBox in (predictions):
            fileWriter.write(' '.join(str(int(x)) for x in boundingBox[:4]))
            fileWriter.write('\n')
    
        fileWriter.close()