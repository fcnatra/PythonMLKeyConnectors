import linearAlgebra as la
import matrices as matrix
import numpy as np
from matplotlib import pyplot as plt

vectors = np.array( [ [1, 2], [2, 1], [3, 3] ] )

origin = [0], [0]
plt.quiver(*origin, vectors[:,0], vectors[:,1], color=['r','b','g'], scale=20)
plt.title("Quiver with origin")

plt.quiver( vectors[:,0], vectors[:,1], color=['r','b','g'], scale=20 )
plt.title("Quiver without origin")

plt.quiver( vectors[:,1], vectors[:,1], color=['r','b','g'], scale=20 )
plt.title("Quiver without origin starting on vector one")

plt.plot( vectors )
plt.title("Plot al vectors")
# UNCOMMENT THIS LINE TO SHOW THE CHART
# plt.show()

print(f'Original vector: {vectors}')

print(f'Reducing the vector: {la.vector_sum( vectors )}')

double_vector = la.scalar_multiply(2, vectors)
print(f'Multiplying each vector element by 2 {double_vector}')

print(f'This is the mean of the vectors: {la.vector_mean(vectors)}')

print(f'And this is the DOT PRODUCT of two vectors (the original and the vector*2): {la.dot_product(vectors, double_vector)}')

print(f'Sum of squares of the original vectors: {la.sum_of_squares(vectors[1])}')

print(f'Sum of squares of the first element of the original vectors ({vectors[1]}): {la.sum_of_squares(vectors[1])}')

print(f'Magnitued of vectors: {la.magnitude(vectors[1])}')

print(f'Distance between vectors {vectors[0]} and {vectors[1]}: {la.distance(vectors[0], vectors[1])}')

identity_matrix = matrix.make_matrix(5, 5, matrix.is_diagonal)
print('Identity matrix:')
for matrix_row in identity_matrix:
    print(matrix_row)
