#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 19:07:36 2018

@author: ming
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 15:54:13 2018

@author: xm
"""

import face_recognition
import time
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX 
name=input('registering,please input your name:')   
i=-20
while True:
    time1=time.time()
    ret,img=cap.read()
    if ret ==1:
#        fps=1/(time.time()-time1)
#        cv2.putText(img,'fps:%0.1f'%fps,(20,20),font,1.0,(255,255,0),1)
        
        cv2.imshow('img',img)
        ll=face_recognition.face_encodings(img)
        if len(ll)==1:
            face_locations = face_recognition.face_locations(img)
            top,right,bottom,left=face_locations[0]
            face0=img[top:bottom,left:right]
#            cv2.imshow('img',face0)
            if i>-1:
                cv2.imwrite('know/%s_%d.jpg'%(name,i),face0)
        i+=1
        if i>4:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()  
'''
f=open('register/register.csv','a')
files=os.listdir('know')
for file in files:
    img=cv2.imread('know/'+file)
    if len(face_recognition.face_encodings(img))==1:
            str0=face_recognition.face_encodings(img)[0].reshape(1,128)
            f.write(file+',')
            np.savetxt(f,str0,delimiter=',')
f.close()

'''



