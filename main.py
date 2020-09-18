import cv2
import numpy as np

#A function to get the model which can detect face better
def getmodel(img):
    frontalface = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
    profileface = cv2.CascadeClassifier('data\\haarcascade_profileface.xml')


    front_faces = frontalface.detectMultiScale(img,1.1,4)
    profile_faces = profileface.detectMultiScale(img,1.1,4)

    max_detetcted_faces = max(0,len(front_faces),len(profile_faces))

    if(len(front_faces)==max_detetcted_faces):
        return front_faces,len(front_faces),"Front Facing"


    return profile_faces ,len(profile_faces),"Profile facing"



smile_cascade = cv2.CascadeClassifier('data\\haarcascade_smile.xml')

try:
    sample_image = cv2.imread('Images\\smile\\img (11).jpg')
    sample_image = cv2.resize(sample_image,(500,500),interpolation=cv2.INTER_AREA)
    sample_image_gray = cv2.cvtColor(sample_image,cv2.COLOR_BGR2GRAY)
except cv2.error as e:
    print("Could not read Image file please check the path")
    exit()

model,number_of_faces,model_name = getmodel(sample_image_gray)

if(number_of_faces==0):
    print("Sorry cound'nt recognise face in the picture!!")
    exit()

print("Model being used is:" + model_name)
print("Number of faces detected " + str(number_of_faces))

for face in model:
    x,y,w,h= face
    face_width = w
    face_height = h

    print("Face height {} and width {} ".format(face_height,face_width))
    
    #Draw rectangle over face
    cv2.rectangle(sample_image,(x,y),(x+w,y+h),(255,0,0),2)

    #Detect Smile in face
    roi_face_gray = sample_image_gray[y:y+h,x:x+w]
    roi_face_color = sample_image[y:y+h,x:x+w]
    smile = smile_cascade.detectMultiScale(roi_face_gray,1.1,4)
    if(len(smile)==0):
        print("No smile detected")
        cv2.imshow('Smile Not detected',sample_image)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
        exit()

    #Sort the smile areas according to decreasig width
    #Assumption -> More width is better chance of smile
    smile =sorted(smile,key=lambda x: x[2],reverse=True)

    #Assuming top 3 regions will be more of a smile area
    smile = smile[:3] #Top 3 regions according to width
    #smile = remove_out_of_scope(smile,face_height,face_width)
    
    print("Smile")
    for s in smile:
        print(s)


    for sx,sy,sw,sh in smile:
        cv2.rectangle(roi_face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
        #cv2.putText(sample_image,"Smile",(sx,sy),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,2),2)
        cv2.putText(sample_image,"SMILE",(0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,102,255),3)
        cv2.imshow('Smile Detected',sample_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    print("-------------------------------------------------")

