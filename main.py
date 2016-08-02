import cv2
import faceDetect

cam = cv2.VideoCapture(0)

while(True):
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    img = faceDetect.detect(frame)
    cv2.imshow('Camera Face', img)
    
    # if you press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cam.release()
cv2.destroyAllWindows()
