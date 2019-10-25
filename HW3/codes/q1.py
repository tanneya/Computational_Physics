from numpy import *
from pylab import *

#loading the data
data=loadtxt('sunspots.txt')
x=data[:,0]
y=data[:,1]

#define the dft function
def dft(y):
    N=len(y)
    rst=[]
    for k in range(N//2+1):
        ck=0.
        for n in range(N):
            ck = ck+ y[n]*e**(-2j*pi*k*n/N)
        rst.append(ck)
    return array(rst)

#calculate the power spectrum
ck=dft(y)

#plot the graph
plot(x[1000:2000],y[1000:2000])
plot([1015,1015],[-10,200],'r--',label='t=1015 months')
plot([1964,1964],[-10,200],'g--',label='t=1964 months')

xlabel('time in month')
ylabel('sunspot number')
legend()
show()
#plot the power spectrum
plot(abs(ck)**2)
xlabel('k')
ylabel('Power Spectrum')
show()