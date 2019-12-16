
# initial state
from numpy import *
from pylab import *
state=zeros((50,50))
dimers=[]
Tmax = 10
Tmin = 10**-5
tau = 1000
T = Tmax
t = 0
def remove_dimer(coordinate):
    global dimers
    for dimer in dimers:
        if coordinate in dimer:
            dimers.remove(dimer)

def check_dimers(coordinate):
    global dimers
    for dimer in dimers:
        if coordinate in dimer:
            return True
    return False            
while T>Tmin:
    t=t+1
    T = Tmax*exp(-t/tau)
    #choose adjacent sites at random
    i_1 = randint(50)
    j_1 = randint(50)
    possible_adjacent=[[i_1,j_1-1],[i_1,j_1+1],[i_1-1,j_1],[i_1+1,j_1]]
    for items in possible_adjacent:
        if -1 in items or -1 in items or 50 in items or 50 in items:
            possible_adjacent.remove(items)
    possible_adjacent=array(possible_adjacent)
    i_2,j_2=possible_adjacent[randint(len(possible_adjacent))]
    
    #If those two sites are currently occupied by a single dimer, remove the dimer from the lattice.
    if check_dimers([i_1,j_1]) or check_dimers([i_2,j_2]):
        if check_dimers([i_1,j_1]) and check_dimers([i_2,j_2]):
            #do nothing
            pass
        elif random()<exp(-1/T):
            remove_dimer([i_1,j_1])
            remove_dimer([i_2,j_2])
        else:
            pass
    else:
        dimers.append([[i_1,j_1],[i_2,j_2]])

for temp in dimers:
    temp=array(temp).T
    plot(temp[0],temp[1])
print(len(dimers))