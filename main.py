import cv2
import numpy as np

#Classifiers
face_cascade = cv2.CascadeClassifier('data\\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('data\\haarcascade_smile.xml')

sample_image = cv2.imread('Images\\Not_smile\\msd.jpg')
sample_image_gray = cv2.cvtColor(sample_image,cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(sample_image_gray,1.1,4)
#print(face)
x,y,w,h= face[0]
cv2.rectangle(sample_image,(x,y),(x+w,y+h),(255,0,0),2)

roi_face_gray = sample_image_gray[y:y+h,x:x+w]
roi_face_color = sample_image[y:y+h,x:x+w]

smile = smile_cascade.detectMultiScale(roi_face_gray,1.1,4)
if(len(smile)==0):
    print("No smile detected")
    cv2.imshow('Sachin',sample_image)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    exit()
sx,sy,sw,sh= smile[0]
cv2.rectangle(roi_face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
cv2.imshow('Sachin',sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
