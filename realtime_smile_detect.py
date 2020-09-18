import cv2

face_cascade = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml') 
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier('data\\haarcascade_smile.xml') 



def detect(gray, frame): 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
	for (x, y, w, h) in faces: 
		cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
		roi_gray = gray[y:y + h, x:x + w] 
		roi_color = frame[y:y + h, x:x + w] 
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.7,18) #Set your parameter according to your surroundings 

		for (sx, sy, sw, sh) in smiles: 
			cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
	return frame 


video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
while True: 
# Captures video_capture frame by frame 
	_, frame = video_capture.read() 

	# Convert image to grayscale					 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	
	# Get the canvas	 
	canvas = detect(gray, frame) 

	cv2.imshow('Video', canvas) 

	# Press q in the keyboard to quit(exit)
	if cv2.waitKey(1) & 0xff == ord('q'):			 
		break

# Release the capture once all the processing is done. 
video_capture.release()								 
cv2.destroyAllWindows() 
