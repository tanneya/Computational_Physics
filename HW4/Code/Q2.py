from numpy import *
from pylab import *
from numpy.random import uniform

#rk4
def rk4_step(t,r,h):
    k1=h*f(t,r)
    k2=h*f(t+h/2,r+k1/2)
    k3=h*f(t+h/2,r+k2/2)
    k4=h*f(t+h,r+k3)
    r_next= r + 1./6*(k1 +2*k2 +2*k3 +k4)
    t_next=t+h
    return t_next,r_next

def rk4_adaptive(t,r,h):
    T,x=rk4_step(t,r,h)
    T1,x1=rk4_step(t+h,x,h)
    T2,x2=rk4_step(t,r,2*h)
    rho=30.*h*delta/sqrt(sum((x1[:2]-x2[:2])**2))
    if rho >=1:
        #proceed.
        h=h*rho**(1./4)
        return (T2,x2,h)
    
    else:
        return rk4_adaptive(t,r,h*rho**(1./4))
    
G=1.
M=1.
vx0=0.
vy0= 0.8*1./2 #1/2.*sqrt(2*10**-7)#
x0 = 1.
y0 = 0.
A=1.
B=1.
def f(t,r):
    # r=[x,y,vx,vy]
    #print(r)
    x,y,vx,vy=r[0],r[1],r[2],r[3]
    R= sqrt(r[0]**2+r[1]**2)
    V= sqrt(r[2]**2+r[3]**2)
    #x direction
    dvx_dt = - G*M*x/(4.*R**3)   - A*vx/(V**3+B)
    dx_dt = vx
    dvy_dt = -G*M*y/(4.*R**3) - A*vy/(V**3+B)
    dy_dt= vy
    
    return array([dx_dt,dy_dt,dvx_dt,dvy_dt])



r=[array([x0,y0,vx0,vy0])]
delta=10**-8
tpoints=[0.]
h=0.0001
t0=0.0
tf=50.
while t0<tf:
    t_next,r_next,h=rk4_adaptive(tpoints[-1],r[-1],h)
    tpoints.append(t_next)
    r.append(r_next)
    
    if sqrt(r_next[0]**2+r_next[1]**2) <= 10**-7:
        break
    t0=t_next
    
r=array(r)
print(min(sqrt(r[:,0]**2+r[:,1]**2)))


plot(r[:,0],r[:,1],'-')
xlabel('x')
ylabel('y')
show()

plot(tpoints,sqrt(r[:,0]**2+r[:,1]**2))
xlabel('time')
ylabel('r')
show()

plot(tpoints,log(sqrt(r[:,0]**2+r[:,1]**2))/log(10))
xlabel('time')
ylabel('log(r)')
show()



### generate A and B to analyze how the time the BH takes to reach 10^-7 chanegs with B/A

Time=[]
Alist=[]
Blist=[]
A=1.0
B=1.0
G=1.
M=1.
vx0=0.
vy0= 0.8*1./2 #1/2.*sqrt(20)
x0 = 1.
y0 = 0.
#for B in arange(0.5,10,0.5):
n=0
while n <=50:    
    A=uniform(0.5,10,1)[0]
    B=uniform(0.5,10,1)[0]
    Alist.append(A)
    Blist.append(B)
    r=[array([x0,y0,vx0,vy0])]
    delta=10**-8
    tpoints=[0.]
    h=0.01
    
    tf=15.
    t0=0.0
    while t0<tf:
        t_next,r_next,h = rk4_adaptive(tpoints[-1],r[-1],h)
    #     print(t_next)
        tpoints.append(t_next)
        r.append(r_next)
    
        if sqrt(r_next[0]**2+r_next[1]**2) <= 10**-7:
            break
        t0=t_next
    Time.append(t0)
    n=n+1
    print(n)
r=array(r)

plot(array(Blist)/array(Alist),array(Time)*0.5333618444372796,'.')
xlabel('B/A')
ylabel('Myr')
show()