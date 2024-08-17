import numpy as np

# Element-wise addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Element-wise addition:", a + b)

# Element-wise multiplication
print("Element-wise multiplication:", a * b)

# Dot product
print("Dot product:", np.dot(a, b))

# Broadcasting
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([1, 0, 1])
print("Broadcasting example:\n", c + d)