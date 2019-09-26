#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 01:27:28 2019

@author: jiachenwan
"""

from numpy import *
from pylab import *

def midpoint_int(f,a,b,N):
    h=float32((b-a)/N)
    result=float32(0.)
    for k in range(N):
        result += f(a+(k+float32(1./2))*h)
    return result*h

def trapezoid_int(f,a,b,N):
    h=float32((b-a)/N)
    result=float32(0.5)*(f(a)+f(b))
    for k in range(1,N):
        result += f(a+k*h)
    return result*h

def simpson(f, a, b, n):
    h=float32((b-a)/n)
    result=float32(f(a)+f(b))
    for i in range(1,n/2 + 1):
        result += float32(4*f(a + (2*i - 1)*h))

    for i in range(1,n/2):
        result += float32(2*f(a + 2*i*h))
    return float32(h/3)*(result)

def f(x):
    return float32(e**float32(-x))

a=float32(0)
b=float32(1.)
answer=float32(1-1/e)

N=around(logspace(0.5, 6, num=30),decimals=-1)
N[0],N[1]=float32(4),float32(8)
result_mid=[]
result_tra=[]
result_simp=[]

for n in N:
    result_mid.append(abs(midpoint_int(f,a,b,int(n))-answer))
    result_tra.append(abs(trapezoid_int(f,a,b,int(n))-answer))
    result_simp.append(abs(simpson(f,a,b,int(n))-answer))

loglog(N,abs(array(result_mid)),label='Midpoint')
loglog(N,abs(array(result_tra)),label='Trapezoid')
loglog(N,abs(array(result_simp)),label='Simpsons')
loglog(N,10**-0.5*float32(N)**-1,'--',label='degree -1')
loglog(N,10**-1.5*float32(N)**-2,'-.',label='degree -2')
loglog(N[:10],10**-2.5*float32(N[:10])**-4,':',label='degree -4')
xlabel('N')
ylabel('relative error')
legend()