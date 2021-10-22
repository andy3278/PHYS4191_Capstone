import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
from random import randint, random, randrange

#energy_range = (-4,2)

numebr_amino_acids = 15
temperature = range(1,10)
# both end points are in 2d (x,y)
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
def sequence_N_integers(N):
    #array of numbers between 1-20, values represent type of amino acid, so can be repeated
    return [randrange(1,21) for _ in range(N)]

def random_select_from_N(N):
    return randint(0,N-1)

#initialize the lattice 20 by 20
lattice = np.zeros((20,20))
#print(sequence_N_integers(15))