""" Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random.
Print the matrix which is the matrix multiplication of A and B.
The shape of the new matrix should be (10,25).
Using basic numpy math functions only & find the sum of all the elements of the new matrix."""


import  numpy as np

array_random_a = np.random.random((10, 20))
array_random_b = np.random.random((20, 25))
array_random_c = np.dot(array_random_a, array_random_b)
print("Matrix of numpy array a and b: ", array_random_c)

print("-------------First Array-----------------")
print("First Numpy Array a: \n", array_random_b)

print("-------------Second Array----------------")
print("Second Numpy Array b: \n", array_random_b)

print("Shape of the matrix coming is: ", np.shape(array_random_c))
print("Sum of all the elements is: \n", np.sum(array_random_c))
