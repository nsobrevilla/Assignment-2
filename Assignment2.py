import numpy as np

# Define 3x3 matrices
a = np.array([[1, 2, 3], [9, 6, 5], [2, 1, 3]])
b = np.array([[2, 4, 6], [7, 5, 3], [3, 2, 1]])

# 1. Dot product
result_dot = np.dot(a, b)
print("Dot product of a and b:")
print(result_dot)

# 2. Transpose
result_transpose = a.transpose()
print("\nTranspose of a:")
print(result_transpose)

# 3. Inverse
result_inv = np.linalg.inv(a)
print("\nInverse of a:")
print(result_inv)

# 4. Determinant
result_det = np.linalg.det(a)
print("\nDeterminant of a:")
print(result_det)

# 5. Flatten
result_flatten = a.flatten()
print("\nFlattened a:")
print(result_flatten)