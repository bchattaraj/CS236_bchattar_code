# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:56:12 2021

@author: bchat
"""

import PIL
import os
import os.path
from PIL import Image


path = r'C:\TEMP\V2RADAR\test'
for file in os.listdir(path): 
    f_img = path+"/"+file
    img = Image.open(f_img)
    img = img.resize((256, 256)) #(width, height)
    img.save(f_img)