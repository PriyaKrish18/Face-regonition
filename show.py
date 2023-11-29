# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 01:31:08 2022

@author: manopriya
"""

from PIL import Image,ImageFilter
pil_g=Image.open('shrey.png')
pil_g.show()
pil_g_b=pil_g.filter(ImageFilter.SMOOTH())
pil_g_b.show()

