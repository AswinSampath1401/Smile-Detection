import cv2
import numpy as np


def getmodel(img):
    frontalface = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
    profileface = cv2.CascadeClassifier('data\\haarcascade_profileface.xml')
    #defaultfaces = cv2.CascadeClassifier('data\\haarcascade_frontalface_default.xml')

    front_faces = frontalface.detectMultiScale(img,1.1,4)
    profile_faces = profileface.detectMultiScale(img,1.1,4)
    #default_faces = defaultfaces.detectMultiScale(img,1.1,4)

    max_detetcted_faces = max(0,len(front_faces),len(profile_faces))

    if(len(front_faces)==max_detetcted_faces):
        return front_faces,len(front_faces),"Front Facing"


    return profile_faces ,len(profile_faces),"Profile facing"

def filterdata(smile,face_height,face_width):
    res=[]
    for data in smile:
        x,y,width,height = data
        if(width>0.75*face_width or height<0.2*face_height or height>0.5*face_height):
            continue
        res.append(data)
    return res

def getrangedata(smile):
    return


def remove_out_of_scope(smile,face_height,face_width):
    res=[]

    for s in smile:
        x,y,width,height = s
        if(width>0.75*face_width or height<0.2*face_height or height>0.5*face_height):
            continue
        res.append(s)
    return res

#Classifiers
#face_cascade = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
#face_cascade = cv2.CascadeClassifier('data\\haarcascade_profileface.xml')
#face_cascade = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt_tree.xml')

smile_cascade = cv2.CascadeClassifier('data\\haarcascade_smile.xml')

try:
    sample_image = cv2.imread('Images\\smile\\virat.jpg')
    sample_image = cv2.resize(sample_image,(1000,1000),interpolation=cv2.INTER_AREA)
    sample_image_gray = cv2.cvtColor(sample_image,cv2.COLOR_BGR2GRAY)
except cv2.error as e:
    print("Could not read Image file please check the path")
    exit()

model,number_of_faces,model_name = getmodel(sample_image_gray)

#faces = face_cascade.detectMultiScale(sample_image_gray,1.1,4)
#print(face)
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
    smile =sorted(smile,key=lambda x: x[2],reverse=True)
    #smile = remove_out_of_scope(smile,face_height,face_width)

    # TODO- Filter Smile using width and height criteria 
    # Refer sample image of Dhoni and Jasprit 
    # Filter according to height and width treshold
    # Get the maximum width out of them to predict the almost smile
    # Run different classifiers and get the best out of them

    # WHAT TODO -> height>height_treshold (remove)
    #width <width_treshold (case not seen yet) (remove)
    #width - 100 height 60-70 
    # 100<width<160    50<height<70

    print("Smile")
    
    for s in smile:
        print(s)

    for sx,sy,sw,sh in smile:
        cv2.rectangle(roi_face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
        #cv2.putText(sample_image,"Smile",(sx,sy),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,2),2)
        cv2.putText(sample_image,"SMILE",(0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(50,100,100),2)
        cv2.imshow('Smile Detected',sample_image)
        cv2.waitKey(0)

    print("-------------------------------------------------")

#sx,sy,sw,sh= smile[0]
#print(smile)
#print(len(smile))
#cv2.rectangle(roi_face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
#cv2.putText(sample_image,"Smile",(sx,sy),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,2),2)
#cv2.imshow('Smile Detected',sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
