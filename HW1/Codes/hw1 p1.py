#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:06:45 2019

@author: jiachenwan
"""

from numpy import *
from pylab import *


def forward_dif(f,x,h):
    return float32(f(x+h)-f(x))/float32(h)

def central_dif(f,x,h):
    return float32(f(x+h/2)-f(x-h/2))/float32(h)

def extrapolated_dif(f,x,h):
    return float32(-f(x+2*h)+ 8*f(x+h) -8*f(x-h)+ f(x-2*h))/float32(12*h)







def f(x):
    return float32(e**x)
x=float32(10)
h=arange(10**-4,10**-0,(10**-0-10**-4)/1000,dtype='f')


# h=logspace(-2, -5, num=30)
loglog(h,abs(forward_dif(f,x,h)-e**x),label='Forward')
loglog(h,abs(central_dif(f,x,h)-e**x),label='Central')
loglog(h,abs(extrapolated_dif(f,x,h)-e**x),label='Extrapolated')
loglog(h[-997:],(10**4)*h[-997:]**1,'--',alpha=0.5,label='degree 1')
loglog(h[-997:],(10**3)*h[-997:]**2,'-.',alpha=0.5,label='degree 2')
loglog(h[-990:],(10**3)*h[-990:]**4,':',alpha=0.5,label='degree 4')
legend()
xlabel('h')
ylabel('relative error')
title('e^x x=10')