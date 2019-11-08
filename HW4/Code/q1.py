from numpy import *
from pylab import *

a = 1.
b = 3.

delta = 10 ** -10  



x0 = 0.
y0 = 0.
ti = 0.
tf = 20.

r = array([x0, y0])
tpoints = [ti]
xpoints = [x0]
ypoints = [y0]

def f(r):

    return array([1-(b+1)*r[0]+a*r[0]**2*r[1], b*r[0]-a*r[0]**2*r[1]])

def BS_step(r,t,H):
    global tpoints,xpoints,ypoints
    def R_n(R1,n):

        if n >8:
            r1=BS_step(r,t,H/2)
            return BS_step(r1,t+H/2, H/2)
        else:
            r_temp=zeros(2)
            r_temp[0],r_temp[1] = r[0],r[1]
            h=float(H)/n
            r_temp_1=r_temp + 0.5 * h * f(r_temp)
            r_temp=r_temp+h*f(r_temp_1)
            for i in range(n-1):
                r_temp_1=r_temp_1+h*f(r_temp)
                r_temp=r_temp+h*f(r_temp_1)
            R2=[0.5 * (r_temp + r_temp_1 + 0.5 * h * f(r_temp))]
            
            
            for m in range(2,n+1):
                R2.append(R2[m - 2] + (R2[m - 2] - R1[m - 2]) / ((float(n) / (float(n) - 1)) ** (2 * (float(m) - 1)) - 1))
            
            R2=array(R2)
            error= sqrt(sum(( (R2[n - 2] - R1[n - 2]) / ((float(n) / (float(n) - 1)) ** (2 * (float(n) - 1)) - 1))**2))
            
            tol= H * delta
            
            if error < tol:
                tpoints.append(t+H)
                xpoints.append(R2[n-1][0])
                ypoints.append(R2[n-1][1])
                return R2[n-1]
            else:
                return R_n(R2,n+1)
    
    n=1
    r_temp=zeros(2)
    r_temp[0],r_temp[1]= r[0],r[1]
    h=float(H)/n
    r_temp_1=r_temp + 0.5 * h * f(r_temp)
    r_temp=r_temp+h*f(r_temp_1)
    for i in range(n-1):
        r_temp_1=r_temp_1+h*f(r_temp)
        r_temp=r_temp+h*f(r_temp_1)
    R1=array([0.5 * (r_temp + r_temp_1 + 0.5 * h * f(r_temp))])
    
    
    return R_n(R1,2)
         
BS_step(r, ti, 20.)
%matplotlib notebook
plot(tpoints, xpoints,'.',color='r')
plot(tpoints, ypoints,'.',color='b')
plot(tpoints, xpoints,'-',color='r',label='x points')
plot(tpoints, ypoints,'-',color='b',label='y points')
xlabel('time')
legend()