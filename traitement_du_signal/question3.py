import numpy as np
import matplotlib.pyplot as plt
from ressources1 import fourier1D 

SR = 50

t = np.arange(0, 1.02, 1/SR)

s = 1 + np.cos(2*np.pi*5*t) + 0.3*np.cos(2*np.pi*9*t)

s_pad = np.concatenate((s, np.zeros(5 * len(s))))


#other ways to do it : 

#s_pad = np.zeros(5*len(s))
#s_pad[:len(s)] = s

# s_pad = np.pad(s, (5,5), mode='constant', constant_values=0)

fourier1D(s_pad, SR)
