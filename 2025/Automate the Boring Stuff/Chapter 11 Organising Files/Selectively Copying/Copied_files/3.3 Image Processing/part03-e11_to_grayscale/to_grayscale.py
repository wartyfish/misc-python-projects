#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    weights = np.array([0.2126, 0.7152, 0.0722])
    gray = image.copy() 
    gray = np.dot(gray[:, :, :3], weights)
    return gray

def to_red(image):
    return image * np.array([[[1, 0, 0]]])

def to_blue(image):
    return image * np.array([[[0, 0, 1]]])

def to_green(image):
    return image * np.array([[[0, 1, 0]]])

def main():
    painting = plt.imread("src/painting.png")

    # grayscale
    plt.imshow(to_grayscale(painting), cmap="gray")
    plt.show()

    # rgb channels
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_blue(painting))
    ax[2].imshow(to_green(painting))
    plt.show()

if __name__ == "__main__":
    main()