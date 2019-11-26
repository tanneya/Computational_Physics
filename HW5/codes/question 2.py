from numpy import *
from pylab import *

data = genfromtxt('particles.dat')


density_function=zeros([100,100])
for points in data:
    y,x=points[0],points[1]
    i,j=int(x-0.5), int(y-0.5)


    xc=i+0.5
    yc=j+0.5
    dx=x-xc
    dy=y-yc
    tx=1.-dx
    ty=1.-dy
    
    density_function[i,j] =density_function[i,j]+tx*ty
    density_function[i+1,j] =density_function[i+1,j]+dx*ty
    density_function[i,j+1] =density_function[i,j+1]+tx*dy
    density_function[i+1,j+1] =density_function[i+1,j+1]+dx*dy

        

imshow((-1.*(1.6*10**-19)/(8.85418782 * 10**-12)*density_function))
colorbar()

#relaxation

delta=1.0
target=10**-10

# Create arrays to hold potential values
phi = zeros([101,101],float)

phiprime = empty([101,101],float)

n=0
# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(101):
        for j in range(101):
#             phiprime[1:100,1:100]=(phi[2:101,1:100]+phi[0:99,1:100]+phi[1:100,2:101]+phi[1:100,0:99])/4.#+1./4*(-1.*density_function[1:101,1:101])
            if i==0 or i==100 or j==0 or j==100:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = (phi[i+1,j] + phi[i-1,j] \
                                 + phi[i,j+1] + phi[i,j-1])/4 +1./4*(-1.*(1.6*10**-19)/(8.85418782 * 10**-12)*density_function[i,j])

    # Calculate maximum difference from old values
    delta = abs(phi-phiprime).max()

    # Swap the two arrays around
    phi,phiprime = phiprime,phi
    print(n,delta)
    n=n+1
# Make a plot
imshow(phi)

#over relaxation
def f(omega):
    delta=1.0
    target=10**-10

    # Create arrays to hold potential values
    phi = zeros([101,101],float)

    n=0
    # Main loop
    delta = 1.0

    while delta>target:
        delta_temp=0.
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    phi[i,j] = phi[i,j]
                else:
                    difference=((phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])/4 +1./4*(-1.*(1.6*10**-19)/(8.85418782 * 10**-12)*density_function[i,j]))-phi[i,j]
                    phi[i,j] = phi[i,j] + (1+omega)*difference
                    if abs(difference)>delta_temp:
                        delta_temp=abs(difference)

        delta=delta_temp
        n=n+1
    # Make a plot
    return n


# golden ration search

"""Python program for golden section search.  This implementation
   does not reuse function evaluations and assumes the minimum is c
   or d (not on the edges at a or b)"""
gr = (math.sqrt(5) + 1) / 2
list_of_iterations=[]
list_of_omega=[]
def gss(f, a, b, tol=1e-5):
    global list_of_iterations,list_of_omega
    """Golden section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    Example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f, 1, 5)
    >>> x
    2.000009644875678

    """
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(c - d) > tol:
        
        if f(c) < f(d):
            b = d
            

        else:
            a = c

        # We recompute both c and d here to avoid loss of precision which may lead to incorrect results or infinite loop
        c = b - (b - a) / gr
        d = a + (b - a) / gr
        list_of_omega.append(d)


    return (b + a) / 2

gss(f,0.91,0.96,tol=0.001)

plot(list_of_omega)
xlabel('Golden search iterstion number')
ylabel('omega')