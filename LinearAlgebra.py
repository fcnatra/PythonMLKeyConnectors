from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
import functools

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return functools.reduce(vector_add, vectors)

def vector_test():
    #VECTORS
    vectors = np.array( [ [1, 2], [2, 1], [3, 3] ] )

    origin = [0], [0]
    plt.quiver( *origin, vectors[:,0], vectors[:,1], color=['r','b','g'], scale=20 )
    plt.title("Quiver with origin")
    #plt.show()

    plt.quiver( vectors[:,0], vectors[:,1], color=['r','b','g'], scale=20 )
    plt.title("Quiver without origin")
    #plt.show()

    plt.quiver( vectors[:,1], vectors[:,1], color=['r','b','g'], scale=20 )
    plt.title("Quiver without origin starting on vector one")
    #plt.show()

    plt.plot( vectors )
    plt.title("Plot al vectors")
    plt.show()

    other_vector = vector_sum( vectors )
    print( 'Other vector: ' )
    print( other_vector )

vector_test()