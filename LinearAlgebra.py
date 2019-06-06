from __future__ import division
import functools
import math

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
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

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))
