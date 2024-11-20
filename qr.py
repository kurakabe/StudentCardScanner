import cv2
import numpy as np
import re
import time
import pyzbar.pyzbar as qr

cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN



f = open("students.txt", "r")

studentsInClass = []
studentDictionary = {}
for line in f:
    studentInfo = line.split(", ")
    studentDictionary[studentInfo[1]] = studentInfo[0]

#print(studentDictionary)

while True:
      ret,frame = cap.read()
      flipped = cv2.flip(frame, flipCode=1)
      frame1=cv2.resize(flipped,(1000,700))
      qrdetect=qr.decode(frame1)

     
      for i in qrdetect:
          x = re.search("\d{6}(\d{7})\d+", str(i.data))
          studentCode = x.group(1)
          print(studentCode)
          #print (i.rect.left,i.rect.top,i.rect.width,i.rect.height)
          #print (i.data)
          
          if studentCode in studentDictionary.keys() and studentCode not in studentsInClass:
              print("student: " + studentDictionary.get(studentCode) + " is in the class");
              studentsInClass.append(studentCode)
              inClass = True
              
          if studentCode not in studentDictionary.keys():
              studentName = input("Enter Student full name(Name Surname): ")
              studentFile = open("students.txt", "a")
              studentFile.write("\n{0}, {1}".format(studentName, studentCode))
              studentDictionary[studentCode] = studentName
              studentFile.close()
        
          if studentCode in studentsInClass and inClass == False :
              print("student: " + studentDictionary.get(studentCode) + " is out of the class")
              studentsInClass.remove(studentCode)
              
          cv2.rectangle(frame1,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,255,0),3)
          cv2.putText(frame1,str(i.data),(20,20),font,2,(255,0,0),2)
          inClass = False
          time.sleep(4)
      cv2.imshow("Frame", frame1)
      key = cv2.waitKey(1) & 0xFF
      if key == ord("q"):
         break
        