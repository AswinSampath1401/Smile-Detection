import cv2
import numpy as np

#Classifiers
face_cascade = cv2.CascadeClassifier('data\\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('data\\haarcascade_smile.xml')

try:
    sample_image = cv2.imread('Images\\smile\\sachin.jpeg')
    sample_image_gray = cv2.cvtColor(sample_image,cv2.COLOR_BGR2GRAY)
except cv2.error as e:
    print("Could not read Image file please check the path")
    exit()
faces = face_cascade.detectMultiScale(sample_image_gray,1.1,4)
#print(face)
if(len(faces)==0):
    print("Sorry cound'nt recognise face in the picture!!")
    exit()

for face in faces:
    x,y,w,h= face
    cv2.rectangle(sample_image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_face_gray = sample_image_gray[y:y+h,x:x+w]
    roi_face_color = sample_image[y:y+h,x:x+w]

    smile = smile_cascade.detectMultiScale(roi_face_gray,1.1,4)
    if(len(smile)==0):
        print("No smile detected")
        cv2.imshow('Smile Not detected',sample_image)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
        exit()

    for sx,sy,sw,sh in smile:
        cv2.rectangle(roi_face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
        #cv2.putText(sample_image,"Smile",(sx,sy),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,2),2)
        cv2.putText(sample_image,"SMILE",(0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(50,100,100),2)
        cv2.imshow('Smile Detected',sample_image)
        cv2.waitKey(0)



sx,sy,sw,sh= smile[0]
print(smile)
print(len(smile))
cv2.rectangle(roi_face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
cv2.putText(sample_image,"Smile",(sx,sy),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,2),2)
cv2.imshow('Smile Detected',sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
