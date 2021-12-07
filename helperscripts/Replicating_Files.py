# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:43:48 2021

@author: bchat
"""

import os
 
os.chdir('C:\TEMP\V2TRACK')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "S" + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)