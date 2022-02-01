def writeOut(fileWriter , fileName: str, predictions) -> None:
    fileWriter.write(fileName)
    fileWriter.write('\n')
    fileWriter.write(str(len(predictions)))
    fileWriter.write('\n')
    for boundingBox in predictions:
        fileWriter.write(' '.join(str(x) for x in boundingBox) + str(' 0 0 0 0 0 0'))
        fileWriter.write('\n')
    
