import numpy as np

# create a matrix of zero values
a0 = np.zeros((2,2))
print(a0)
# create a matrix of ones values
a1 = np.ones((2,2))
print(a1)
# create a matrix of random value between 0 and 10 for a matrix 3,3
ar = np.random.randint(10,size=(3,3))
print (ar)
# manipulate the entire values in a matrix
a01 = a0 + 3
print(a01)
a02 = a01 *2
print(a02)
# accessing 