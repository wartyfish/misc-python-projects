#!/usr/bin/env python3
from functools import reduce
import numpy as np

def matrix_power(a, n):
    if n == 0:
        # Return identity matrix of same size
        return np.eye(a.shape[0], dtype=a.dtype)
    
    # Multiply a by itself n times using reduce
    if n > 0:
        return reduce(lambda x, y: x @ y, (a for _ in range(n)))
    
    else: 
        return reduce(lambda x, y: x @ y, (np.linalg.inv(a) for _ in range(-n)))

    
    

def main():
    a = np.array(
        [[1, 6, 7],
        [7, 8, 1],
        [5, 9, 8]]
    )
    n = -2

    print(matrix_power(a, n))

if __name__ == "__main__":
    main()
