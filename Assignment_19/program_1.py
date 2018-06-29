"""Create a numpy array with 10 elements of the shape(10,1) using np.random and
find out the mean of the elements using basic numpy functions."""

import numpy as np

array_random = np.random.random((10, 1))
print(array_random)
print("Mean of elements: ", np.average(array_random))
