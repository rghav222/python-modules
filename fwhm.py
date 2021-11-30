# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 08:39:09 2021

@author: rmurty
"""

#find FWHM
def fwhm(x,y):
    from scipy.interpolate import interp1d
    from scipy import optimize
    f = interp1d(x,y)
    f_ = lambda x: f(x) - 0.5
    return round(2*optimize.newton(f_, 1),3)

#find FWHM better method
def fwhm2(x,y):
    from scipy.interpolate import interp1d
    from numpy import argwhere, arange
    f = interp1d(x,y)
    a = argwhere(y>0.1)
    b = x[a[0]]
    x1 = arange(b,0,0.00001)
    y1 = f(x1)
    c = x[a[-1]]
    x2 = arange(0,c,0.00001)
    y2 = f(x2)
    d = argwhere(y1>0.49999)
    e = x1[d[0]]
    g = argwhere(y2>0.49999)
    h = x2[g[-1]]
    i = (h-e)[0]
    return round(i,5)

#find FWTM better method
def fwtm2(x,y):
    from scipy.interpolate import interp1d
    from numpy import argwhere, arange
    f = interp1d(x,y)
    a = argwhere(y>0.001)
    b = x[a[0]]
    x1 = arange(b,0,0.00001)
    y1 = f(x1)
    c = x[a[-1]]
    x2 = arange(0,c,0.00001)
    y2 = f(x2)
    d = argwhere(y1>0.09999)
    e = x1[d[0]]
    g = argwhere(y2>0.09999)
    h = x2[g[-1]]
    i = (h-e)[0]
    return round(i,5)