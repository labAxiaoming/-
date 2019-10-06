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
import os
import numpy as np
i=0
##cap=cv2.VideoCapture('http://222.204.248.71:8080/?action=stream')
cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX 
print('------------注册中-----------\n')
name=input('registering,please input your name:')   

f=open('register/register.csv','a')

while True:
    time1=time.time()
    ret,img=cap.read()
    if ret ==1:
#        fps=1/(time.time()-time1)
#        cv2.putText(img,'fps:%0.1f'%fps,(20,20),font,1.0,(255,255,0),1)
        
        cv2.imshow('img',img)
        
        if len(face_recognition.face_encodings(img))==1:
            str0=face_recognition.face_encodings(img)[0].reshape(1,128)
            f.write(name+',')
            np.savetxt(f,str0,delimiter=',')
#            cv2.imwrite('know/%s_%d.jpg'%(name,i),img)
            i+=1
        if i>4:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
	   

            break
#cv2.waitKey(0)
f.close()
print('-----------注册成功----------\n')
print('-----------注册成功----------\n')
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



