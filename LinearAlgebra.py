from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
import functools
import math

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    return functools.reduce(vector_add, vectors)

def scalar_multiply(multiplier, vectors): 
    return [multiplier * vector_item for vector_item in vectors]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot_product(v, w):
    #The dot product of two vectors is the sum of their componentwise products
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(vectors):
    return dot_product(vectors, vectors)

def magnitude(vectors):
    return math.sqrt(sum_of_squares(vectors))

def vector_test():
    #VECTORS
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
    plt.show()

    print(f'Original vector: {vectors}')

    print(f'Reducing the vector: {vector_sum( vectors )}')

    double_vector = scalar_multiply(2, vectors)
    print(f'Multiplying each vector element by 2 {double_vector}')

    print(f'This is the mean of the vectors: {vector_mean(vectors)}')

    print(f'And this is the DOT PRODUCT of two vectors (the original and the vector*2): {dot_product(vectors, double_vector)}')

    print(f'Sum of squares of the original vectors: {sum_of_squares(vectors[1])}')

    print(f'Sum of squares of the first element of the original vectors ({vectors[1]}): {sum_of_squares(vectors[1])}')

    print(f'Magnitued of vectors: {magnitude(vectors[1])}')

vector_test()