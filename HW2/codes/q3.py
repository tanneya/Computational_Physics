#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 04:58:23 2019

@author: jiachenwan
"""

from numpy import *
from pylab import *

# 2d gradient descent
'''
def gradient_descent(f,r0,delta_r,learning_rate,tol=10**-8):
    r1=r0
    r2=r1+delta_r
    epsilon=sqrt(sum((r2-r1)**2))/learning_rate
    result=[]
    result1=[]
    r3=zeros(2)
    while epsilon > tol:
        
        r3=zeros(2)
        r3[0] = r2[0] - learning_rate*(f(r2[0],r1[1])-f(r1[0],r1[1]))/(r2[0]-r1[0])
        r3[1] = r2[1] - learning_rate*(f(r1[0],r2[1])-f(r1[0],r1[1]))/(r2[1]-r1[1])
        
        
        r1=r2
        r2=r3
        result.append(r1[0])
        result1.append(r1[1])
        epsilon=sqrt(sum((r2-r1)**2))
    subplot(2,1,1)
    plot(result)
    xlabel('number of interation')
    ylabel('x')
    ylim(1.98,2.02)
    subplot(2,1,2)
    plot(result1)
    xlabel('number of interation')
    ylabel('y')
    ylim(1.98,2.02)
    return r3
'''

# 3d gradient descent

def gradient_descent(f,r0,delta_r,learning_rate,tol=10**-6.5):
    r1=r0
    r2=r1+delta_r
    epsilon=sqrt(sum((r2-r1)**2))/learning_rate
    result=[]
    r3=zeros(3)
    while epsilon > tol:
        
        r3=zeros(3)
        r3[0] = r2[0] - learning_rate*(f(r2[0],r1[1],r1[2])-f(r1[0],r1[1],r1[2]))/(r2[0]-r1[0])
        r3[1] = r2[1] - learning_rate*(f(r1[0],r2[1],r1[2])-f(r1[0],r1[1],r1[2]))/(r2[1]-r1[1])
        r3[2] = r2[2] - learning_rate*(f(r1[0],r1[1],r2[2])-f(r1[0],r1[1],r1[2]))/(r2[2]-r1[2])
        
        r1=r2
        r2=r3
        result.append(epsilon)
        epsilon=sqrt(sum((r2-r1)**2))
    plot(log(result[:])/log(10))
    xlabel('number of interation')
    ylabel('log($\epsilon$)')
    show()
    return r3
'''

def f(x,y):
    return (x-2.)**2*(y-2.)**2


# for 2d demonstration
result=gradient_descent(f,array([1.1,1.1]),array([0.1,0.1]),1.)

print(result)
'''
#read files
filename='smf_cosmos.dat'
data = np.loadtxt( filename )
x=data[:,0]
y=data[:,1]
err=data[:,2]
x=10**x


def f(phi,M,alpha):
    global x,y,err
    chi2=sum((phi*(x/(M*10**10))**(alpha+1)*e**(-x/(M*10**10) )*log(10) - y)**2/err**2)
    return chi2

gradient_descent(f,array([ 0.003,  10.39, -1.03]),array([0.0001,0.01,0.01]),10**-8)

phi,M,alpha=2.45046871e-03,  1.03981070e+01, -1.04158915e+00
plot(log(x)/log(10),log(phi*(x/(M*10**10))**(alpha+1)*e**(-x/((M*10**10)))*log(10) )/log(10))
errorbar(log(x)/log(10),log(y)/log(10),yerr=err/(y*log(10)),fmt='.')
ylabel('log(n)')
xlabel('log($M_{gal}$)')
show()