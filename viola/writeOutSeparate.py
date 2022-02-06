def writeOutSeparate(fileName: str, predictions) -> None:
    fileWithoutExtension = fileName.replace('.jpg', '.txt')
    with open('detections/' + fileWithoutExtension, 'w') as fileWriter:
        for boundingBox in (predictions):
            fileWriter.write(' '.join(str(x) for x in boundingBox))
            fileWriter.write('\n')
    
        fileWriter.close()