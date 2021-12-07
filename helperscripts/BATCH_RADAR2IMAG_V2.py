# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:51:58 2021

@author: bchat
"""

from PIL import Image, ImageSequence
import os
import random

index=1
for filename in os.listdir("E:\STANFORD_AI\STANFORD_CS236_FALL2021\PROJECT\DATA\RADAR_PROCESSING_V2\RADAR_PROCESSING"):
    if filename.endswith(".gif"): 
        print(filename)
        im = Image.open(filename)

        numframe=im.n_frames

        startframe=int(numframe*0.76)
        endframe=int(numframe*0.99)
        
        # rList=list(random.sample(range(startframe,endframe),10))
        rList=list(random.randint(startframe,endframe) for i in range(10))
        rList.sort()
        print(len(rList))

        
    


        
        iframe=-1
        
        for frame in ImageSequence.Iterator(im):
            iframe+=1
            if iframe>=startframe and iframe<=endframe:
    
                for iList in range(len(rList)):
                    iCheck=int(rList[iList])
                    if iCheck>iframe:
                        break
                    elif iframe ==iCheck:
                        frame.save(".\TRACKH2B\S%d.png" % index)
                        index += 1
        print(index)
        im.close()  
        continue
    else:
        continue
