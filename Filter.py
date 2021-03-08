
# import the opencv library 
from cv2 import cv2 
from PIL import Image
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
import numpy as np
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    frame = cv2.flip(frame,1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    # Display the resulting frame 
    bg = Image.fromarray(frame)
    
    img = np.array(bg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    filename = '—Pngtree—3d diamond crown queen_849404.png'
    ironman = Image.open(filename, 'r').crop((150,430,1830,1380)).convert('RGBA')
    # print(ironman.mode,bg.mode)
    
    # display(ironman)
    text_img = Image.new('RGBA', bg.size, (255, 255, 255,0))
    text_img.paste(bg, (0,0))

    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 

        ironman = ironman.resize((w,int(w*(np.array(ironman).shape)[0]/(np.array(ironman).shape)[1])))
        text_img.paste(ironman, (x,y-np.array(ironman).shape[0]), mask=ironman)
        
    text_img = cv2.cvtColor(np.array(text_img),cv2.COLOR_RGBA2BGR)
    cv2.imshow('frame',np.array(text_img))
    # cv2.imshow('frame2', frame) 
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
