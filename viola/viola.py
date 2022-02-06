import cv2 as cv

def viola(original_image)-> list([int,int,int,int]):

    # Convert color image to grayscale for Viola-Jones
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

    face_cascade = cv.CascadeClassifier('../venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')

    detected_faces = face_cascade.detectMultiScale(grayscale_image)
    return detected_faces

