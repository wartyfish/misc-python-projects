#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import math

def vector_angles(X, Y):
    internal_product = np.sum(X*Y, axis=1)
    X_len = np.sqrt(np.sum(X ** 2, axis=1)) # scipy.linalg.norm(X, 2, axis=1)
    Y_len = np.sqrt(np.sum(Y ** 2, axis=1))
    
    return np.arccos(np.clip((internal_product / (X_len*Y_len)), -1.0, 1.0)) * 180 / np.pi # clip between -1 and 1 to protect against floating point rounding errors
    

def main():
    X = np.random.randint(-100,100, (1, 2))
    Y = np.random.randint(-100,100, (1, 2))
    print(X, Y)
    print(vector_angles(X, Y))

if __name__ == "__main__":
    #main()
    a = np.random.randint(0, 10, (2, 3, 3))
    print(a)
    b = np.random.randint(0, 10, (3,))
    print(b)
    print(a+b)