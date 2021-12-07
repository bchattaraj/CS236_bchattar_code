# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:51:58 2021

@author: bchat
"""

from PIL import Image, ImageSequence
import os

index=0
for filename in os.listdir("E:\STANFORD_AI\STANFORD_CS236_FALL2021\PROJECT\DATA\RADAR_PROCESSING"):
    if filename.endswith(".gif"): 
        print(filename)
        im = Image.open(filename)

        numframe=im.n_frames

        blockframe=int(numframe/10)
        startframe=int(numframe*0.05)
        endframe=startframe+9*blockframe



        listframe=[]

        for i in range(10):
            listframe.append(startframe+i*blockframe)
    


        
        iframe=0
        for frame in ImageSequence.Iterator(im):
            iframe+=1
            if iframe in listframe:
                frame.save("S%d.png" % index)
                index += 1
        
        im.close()  
        continue
    else:
        continue
