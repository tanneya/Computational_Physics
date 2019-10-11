from numpy import *
from pylab import *

#define binary search algorithm
def binary_search(f,a,b,tol=10**-6):
    #starting and ending points
    x1=a
    x2=b
    #epsilon
    epsilon=abs(x1-x2)
    #main loop
    while epsilon >= tol:
        #break the loop if f(x1) and f(x2) are the same sign, also flag it.
        if sign(f(x1))==sign(f(x2)):
            flag=False
            break
        #otherwise, calculate x'
        x_prime=1./2*(x1+x2)
        #replace either x1 or x2 with x', depedning on the sign of f(x')
        if sign(f(x_prime)) ==  sign(f(x1)):
            x1=x_prime
        else:
            x2=x_prime
        #calculate the new 
        epsilon = abs(x1-x2)
    
    #print the result or print warning
    if epsilon <= tol:
        flag=True
    if flag:
        return 1./2*(x1+x2)
    else:
        print('Same sign!')

#  define the interested equation to solve
def f(x):
    return 5*e**-x+x-5
#
print('x =',binary_search(f,0.1,10))