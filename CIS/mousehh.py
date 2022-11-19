import cv2
from module import findpostion
import math
import pyautogui
from time import sleep
#import tkinter
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
def KeyBoard():
  pass
while True:

     ret, frame = cap.read()
     frame_height, frame_width, _ = frame.shape
     flipped = cv2.flip(frame, flipCode = 1)
     frame = cv2.resize(flipped, (840, 680))  
     cv2.rectangle(frame,(20,50),(120,50),(78,245,66),120)
     cv2.putText(frame,'Keyboard',(20,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),3)
     a=findpostion(frame) 
     if len(a)!=0:
      x1,y1=a[8][1],a[8][2]
      x2,y2=a[4][1],a[4][2]
      x3,y3 =a[0][1],a[0][1]
      index_x = screen_width/frame_width*x1
      index_y = screen_height/frame_height*y1
      thumb_x = screen_width/frame_width*x2
      thumb_y = screen_height/frame_height*y2  
      fist_x = screen_width/frame_width*x3
      fist_y = screen_width/frame_width*y3
      length = math.hypot(thumb_x-index_x,thumb_y-index_y)
      length2 = math.hypot(fist_x-index_x,fist_y-index_y)
      pyautogui.moveTo(index_x,index_y)
      print(length2)
      if(length<65):
        sleep(0.05)
        #pyautogui.leftClick()
     cv2.imshow("Frame", frame)
     if cv2.waitKey(1) & 0xFF==27:
       break
cap.release()
cv2.destroyAllWindows()
