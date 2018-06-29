""" Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and
standard deviation of the elements."""

import  numpy as np

array_random = np.random.random((20, 1))
print(array_random)
print("Variance of elements: ", np.var(array_random))
print("Standard Deviation of elements: ", np.std(array_random))
