# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 08:56:28 2021

@author: rmurty
"""

#function to read exr

def read_data(R0,file0):#R0 is colour channel, file0 is filename
    from OpenEXR import InputFile
    from Imath import PixelType
    from numpy import frombuffer, float32
    pt = PixelType(PixelType.FLOAT)
    file = InputFile(file0)
    dw = file.header()['dataWindow']
    size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
    R = file.channel(R0, pt)
    R = frombuffer(R, dtype = float32)
    R.shape = (size[1], size[0]) # Numpy arrays are (row, col)
    return R

def read_exr(file0):
    from numpy import asarray
    R = read_data("R",file0)
    G = read_data("G",file0)
    B = read_data("B",file0)
    return asarray((R,G,B))
