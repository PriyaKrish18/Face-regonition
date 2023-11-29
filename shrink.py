# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:43:23 2022

@author: manopriya
"""
from PIL import Image
import face_recognition
shrey_photo=face_recognition.load_image_file('./pics/shrey.png')
print(shrey_photo.shape)
l=face_recognition.face_locations(shrey_photo,model='hog')
print(l)
top=l[0][0]
right=l[0][1]
bottom=l[0][2]
left=l[0][3]
shrey_face=shrey_photo[top:bottom,left:right]
print(shrey_face.shape)
shrey_face_image=Image.fromarray(shrey_face)
shrey_face_image.show()



