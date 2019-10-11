from numpy import *
from pylab import *

#relaxation
#define constant
c=2.
#define the requred function
def f(x):
    global c
    return 1-e**(-c*x)

#define a starting position
x=1.0
#define a starting epsilon
epsilon=abs(f(x)-x)
#define n
n=0

while epsilon >= 10**-6:
    # x'=f(x)
    x=f(x)
    n+=1
    epsilon=abs(x-f(x))

print('the number of steps is '+str(n))



#overrelaxation
#define constant
c=2.
#define the requred function
def f(x):
    global c
    return 1-e**(-c*x)

#define a starting position
x=1.0
#define learning rate
omega=0.5
#define a starting epsilon
epsilon=abs(f(x)-x)
#define n
n=0

while epsilon >= 10**-6:
    # x'=f(x)
    x=(1.+omega)*f(x)-omega*x
    n+=1
    epsilon=abs(x-f(x))

print('the number of steps is '+str(n))