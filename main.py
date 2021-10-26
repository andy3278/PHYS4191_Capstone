import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
from random import randint, random, randrange

#energy_range = (-4,2)

nx = 20
ny = 20
T0 = 1
T1 = 10
kB = 1
T = np.arange(T0, T1, 0.2)

numebr_amino_acids = 15
temperature = range(1,10)
# both end points are in 2d (x,y)
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
def sequence_N_integers(N):
    #array of numbers between 1-20, values represent type of amino acid, can repeat
    return [randrange(1,21) for _ in range(N)]



def random_select_from_N(N):
    return randint(0,N-1)

#initialize the lattice 20 by 20
lattice = np.zeros((nx,ny))
#print(sequence_N_integers(15))
#initialize lattice with stright protein chain in middle 
for i in range(nx):
    for j in range(ny):
        a  = 0
        if (i== 10 and j>2 and j < 18):
            a = j -2
        lattice[i][j] = a
#print(lattice)
Num_Gen = 1000
# one generation mean one loop over entire protein
coordinate_over_time = np.zeros((Num_Gen,numebr_amino_acids))
length_over_time = []
energy_ = [randrange(-4,3) for _ in range(numebr_amino_acids)]
print(energy_)
for t in T:
    for i in range(Num_Gen):
        for j in range(numebr_amino_acids):
            continue
