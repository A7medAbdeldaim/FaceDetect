import cv2

# Haarcasade File
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def faceDetect(img):
    # Detect Faces
    faces = faceCascade.detectMultiScale(img, 1.3, 5)
    # get the cordnates of the face
    for (x,y,w,h) in faces:
        # draw rectangle around it
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img

