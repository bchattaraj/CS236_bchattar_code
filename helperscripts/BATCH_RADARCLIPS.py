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

       
        startframe=int(numframe*0.05)
        endframe=int(numframe*0.95)



        

        for i in range(1):
            rList=list(random.sample(range(startframe,endframe),4))
            
            rList.sort()
            print(rList)
            listframe=[]
            
            for frame in ImageSequence.Iterator(im):
                listframe.append(frame)
               
            print(len(listframe)) 
            # Uisng all()method
            result = all(element == listframe[0] for element in listframe)
            if (result):
                print("All the elements are Equal")
            else:
                print("All Elements are not equal")
           
                #print(iframe)
            image1=listframe[10]
            image2=listframe[40]
            image3=listframe[100]
            image4=listframe[150]
            image1.save("Image1.png")
            image2.save("Image2.png")
            image3.save("Image3.png")
            #image4=im.seek(180)
            image4.save("Image4.png")
            # image1=im.seek(rList[0])
            # image1.show()
            # image2=im.seek(rList[1])
            
            #image1 = image1.resize((256, 256))
            image1_size = image1.size
            image2_size = image2.size
            new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (256,256,256))
            new_image.paste(image1,(0,0))
            new_image.paste(image2,(image1_size[0],0))
            new_image.save("S%d.png" % index)
            
            image1=image3
            image2=image4
            
            #image1 = image1.resize((256, 256))
            image1_size = image1.size
            image2_size = image2.size
            new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (256,256,256))
            new_image.paste(image1,(0,0))
            new_image.paste(image2,(image1_size[0],0))
            new_image.save("T%d.png" % index)
            index +=1


        
        
        im.close()  
        continue
    else:
        continue
