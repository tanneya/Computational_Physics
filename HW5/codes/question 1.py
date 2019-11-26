from numpy import *
from pylab import *
#constants
g=9.8
target=10**-6
x=zeros(101)
h=0.1
x_prime=zeros(101)
delta=1.0

while delta >target:
    x_prime[1:100]=1./2*(x[2:101]+x[0:99]+g*h**2)
    delta=max(abs(x-x_prime))
    x,x_prime=x_prime,x
    
    
plot(linspace(0,10,101),x,'.')
xlabel('t')
ylabel('height')