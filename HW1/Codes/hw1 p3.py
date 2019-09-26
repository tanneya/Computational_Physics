#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:30:26 2019

@author: jiachenwan
"""

from numpy import *
from pylab import *
from scipy.interpolate import CubicSpline
from scipy.optimize import root_scalar

filename='lcdm_z0.matter_pk.txt'
data=loadtxt(filename)

P=CubicSpline(data[:,0],data[:,1])

loglog(data[:,0],data[:,1],'.',alpha=0.5,label='actual data')
loglog(data[:,0],P(data[:,0]),label='interpolation')

xlabel('r Mpc/h')
ylabel('P(k) Power Spectrum')
legend()

show()
def func(k):
    global r
    return (1./(2*pi**2))*(k**2)*P(k)*sin(k*r)/(k*r)

def simpson(f, a, b, n):
    h=float64((b-a)/n)
    result=float64(f(a)+f(b))
    for i in range(1,n/2 + 1):
        result += float64(4*f(a + (2*i - 1)*h))

    for i in range(1,n/2):
        result += float64(2*f(a + 2*i*h))
    return float64(h/3)*(result)


b=root_scalar(P, bracket=[10,16], method='brentq').root
a=root_scalar(P, bracket=[0,3], method='brentq').root
print('the integration range is from a='+str(a)+' to b='+str(b))
R=linspace(0,120,1000)
result=[]
for r in R:
    result.append(simpson(func,a,b,1000))

plot(R,R**2*result)
plot([107.38738738738739]*2,[0,60],'--',label='r=107.3874')
xlabel('r Mpc/h')
ylabel('r^2*xi(r)')
legend()
show()


peak=R[700:][argsort((R**2*result)[700:])[-1]]

print('the scale of Baryon Acoustic Peak is '+str(peak))