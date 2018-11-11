# Import OpenCV2 for image processing
import RPi.GPIO as GPIO
import cv2
import os

# Import numpy for matrices calculations
import numpy as np

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(27,0)
GPIO.output(17,0)

# Create a binary pattern histogram 
recognizer = cv2.face.createLBPHFaceRecognizer()

# trained yml file
recognizer.load('trainer/trainer.yml')

# loading the pre build model we are using haarcascade frontal face for face recog if you want to detect body eyes you can change the xml file which is located in the cmake path
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

while True:
    # Read the video frame
    ret, im =cam.read()

    # convert frame into grayscale format
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # get faces from the video frames
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        
        # Check the ID if exist 
        # you can control the led's which is wrt your face the led lights will be turned on or off!!!! that can be implimented in doors etc.
        if(Id == 1):
            Id = "" #type your first trained name from face datasets
            GPIO.output(27,0)
            GPIO.output(17,0)
        elif(Id == 2):
            Id = "" #type your second trained name from face datasets
            GPIO.output(27,1) 
            GPIO.output(17,1)
            print("open door")
        #If not exist, then it is Unknown
        else:
            Id = "unknown"
            GPIO.output(27,0)
            GPIO.output(17,0)
            
        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
