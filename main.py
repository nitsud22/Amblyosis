import cv2 as cv

eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#open a camera for videocapture
cap = cv.VideoCapture(0)

while cap.isOpened():
    #capture every frame
    _, frame = cap.read()

    #convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)

    for(x, y, w, h) in eyes:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
    



