import numpy as np
import h5py
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (5.0, 4.0)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

np.random.seed(1)

a = [[1,1],[2,2]]
b = np.pad(a, ((1,1),(1,1)), 'constant')
c = np.pad(a, ((1,0),(1,1)), 'constant')
print(a)
print('\n')
print(b)
print('\n')
print(c)
