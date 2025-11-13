import numpy as np

matrix = np.random.rand(5, 4)
print("Original matrix (5x4):")
print(matrix)

transpose = matrix.T
print("\nTranspose (4x5):")
print(transpose)

col_mean = np.mean(matrix, axis=0)
print("\nColumn-wise mean:")
print(col_mean)

row_std = np.std(matrix, axis=1)
print("\nRow-wise standard deviation:")
print(row_std)

dot_product = np.dot(matrix, transpose)
print("\nDot product (matrix × transpose) - 5x5:")
print(dot_product)