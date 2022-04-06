import cv2 as cv

def saveImg(original_image, filename:str, predictions: list([int,int,int,int])) -> None:
    for (column, row, width, height) in predictions:
        cv.rectangle(
            original_image,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )

    cv.imwrite('testefddb/'+filename+'.jpg', original_image) 
        