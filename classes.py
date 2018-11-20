#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:51:30 2018

@author: pepegar
"""
#%%
class Door:
    
    is_open = False
    
    def __init__(self, height, width,color):
        self.height = height
        self.width = width
        self.color = color
        
    def openn(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False


door1 = Door(215,80, "blue")
door2 = Door(234, 90, "red")