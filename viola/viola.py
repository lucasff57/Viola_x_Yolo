import cv2 as cv
import time


def viola(original_image)-> list([int,int,int,int]):
    start_time = time.time()
    # Convert color image to grayscale for Viola-Jones
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

    face_cascade = cv.CascadeClassifier('../venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
    start_time2 = time.time()
    detected_faces = face_cascade.detectMultiScale(grayscale_image)
   
    print("--- %s seconds full ---" % (time.time() - start_time))
    #print("--- %s seconds partial ---" % (time.time() - start_time2))
    return detected_faces

