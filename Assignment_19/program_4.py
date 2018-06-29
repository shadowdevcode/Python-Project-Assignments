"""

Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1)
such that each element is the following function applied on each element of A.

f(x)= 1 / (1 + exp(-x))

Apply this function to each element of A and print the new array holding the value the function returns
Example:

a = [a1, a2, a3]

n(new array to be printed )=[ f(a1), f(a2), f(a3)]

"""

import numpy as np

numpy_array_a = np.random.random((10, 1))
print("Array a: \n", numpy_array_a)

func_exp = 1 / (1 + np.exp(-numpy_array_a))

print("Modified Array after applying function is: \n", func_exp)
