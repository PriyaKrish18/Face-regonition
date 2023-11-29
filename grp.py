# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:30:08 2022

@author: manopriya
"""
from PIL import Image
import face_recognition
grp_photo=face_recognition.load_image_file('./pics/grp_photo.png')
face_locations=face_recognition.face_locations(grp_photo)
print("There are {} face in this photo".format(len(face_locations)))
face_count=0
for face_location in face_locations:
    face_count=face_count+1
    top,right,bottom,left=face_location
    print("face {}...top: {},left: {}, bottom: {}, right:{}".format(face_count,top,left,bottom,right))
    face_image=grp_photo[top:bottom, left:right]
    pil_image=Image.fromarray(face_image)
    pil_image.show()
    