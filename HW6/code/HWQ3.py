
from numpy import *
from pylab import *
def generate_random_number(x,N):
    a=1664525
    c=1013904223
    m=4294967296
    rst=[]
    for i in range(N):
        x=(a*x+c)%m
        rst.append(x)
    return array(rst)/float(m)

# plot(generate_random_number(19,100),'.')
sigma=1.
numbers1=generate_random_number(648736287566,10**4)
numbers2=generate_random_number(894687637856,10**4)
theta=2*pi*numbers1
r=sqrt(-2*sigma*sigma*log(1-numbers2))


#####plot the gaussian sequence
# mu=0.
# hist(r*cos(theta),30)
# bins=linspace(-4,4,100)
# plt.plot(bins, 2500*1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
# xlabel('x')
# plt.yscale('log', nonposy='clip')



def dft(y):
    N=len(y)
    rst=[]
    for k in range(N//2+1):
        ck=0.
        for n in range(N):
            ck = ck+ y[n]*e**(-2j*pi*k*n/N)
        rst.append(ck)
    return array(rst)


####dft of gaussian sequence

# ck=dft(r*cos(theta))

# loglog(abs(ck)**2)
# xlabel('wavenumber k')
# ylabel('power spectrum')


#random walk
position=zeros(10000)
for i in range(1,10000):
    position[i]=position[i-1]+(r*cos(theta))[i]

####plot the random walk sequence
# plot(position)
# xlabel('number of iteration')
# ylabel('position')

#dft of random walk sequence
# ck1=dft(position)
loglog(abs(ck1)**2)
loglog(logspace(0,4,100),10**10*logspace(0,4,100)**-2)
xlabel('wave number k')
ylabel('power spectrum')