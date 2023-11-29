# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:25:20 2022

@author: manopriya
"""
from PIL import Image,ImageDraw
pil_g=Image.open('shrey.png')
pil_g.show()
draw=ImageDraw.Draw(pil_g)
draw.rectangle((300,300,300,300), outline=(255,0,0),width=10)
draw.line((100,200,550,650),width=5)
pil_g.show()
