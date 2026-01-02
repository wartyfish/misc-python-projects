#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    H = a.shape[0]
    W = a.shape[1]

    return ((H-1) / 2, (W-1) / 2)

def radial_distance(a):
    centre_y, centre_x = center(a)
    y_coords, x_coords = np.indices(a.shape[:2])
    
    distance_matrix =  ((y_coords - centre_y)**2 + (x_coords - centre_x)**2)**0.5
    return distance_matrix

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax].""" 
    
    amin = a.min()
    amax = a.max()

    # protect against / 0 error for homogenous arrays
    if amax == amin:
        return np.full_like(a, tmin, dtype=float)

    return (a - amin) / (amax - amin) * (tmax - tmin) + tmin


def radial_mask(a):
    return 1 - scale(radial_distance(a))

def radial_fade(a):
    H = a.shape[0]
    W = a.shape[1]

    return a * radial_mask(a).reshape(H, W, 1)

def main():
    painting = plt.imread("src/painting.png")
    mask = radial_mask(painting)
    vignette = radial_fade(painting)


    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(painting)
    ax[1].imshow(mask)
    ax[2].imshow(vignette)
    plt.show()

if __name__ == "__main__":
    main()
