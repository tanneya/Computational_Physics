
from numpy import *
from pylab import *
#setting constants
seed(5)
J=1
T=1
kb=1
beta=1./(kb*T)
N=20
#initialize a random state, 20x20
state=zeros((N,N))#,int)
for i in range(20):
    for j in range(20):
        if random() < 0.5:
            state[i,j]=1
        else:
            state[i,j]=-1
#energy function for part a
def energy(state):
    u=state[:-1,:]*state[1:,:]
    v=state[:,:-1]*state[:,1:]
    return -J*(sum(u) + sum(v))

seed(2983)
E_old=energy(state)
n=0
rst=[]
coor=logspace(0,6,6,dtype=int)
coor[-1]=999999
for k in range(1000000):
    #choose a random particle
    i = randint(20) 
    j = randint(20)
    #flip it
    state[i,j] = -state[i,j]
    #calculate the new energy
    E_new = energy(state)
    #compare
    dE = E_new - E_old
    #now decide wether to keep
    if dE>0:
        if random()<e**(-beta*dE):
            E_old = E_new #acepted
            M = sum(state)
        else:
            state[i,j]=-1*state[i,j]#rejected
    else:
        E_old = E_new #accepted
        M = sum(state)
    rst.append(M)
    if k in coor:
        n=n+1
        subplot(2,3,n)
        imshow(state)