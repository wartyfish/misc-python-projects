#!/usr/bin/env python3
import matplotlib

import numpy as np
import matplotlib.pyplot as plt


def subfigures(a):
    x = a[:, 0]
    y = a[:, 1]
    colors = a[:, 2]
    sizes = a[:, 3].astype(float)

    fig, ax = plt.subplots(1, 2)

    ax[0].plot(x, y)
    ax[1].scatter(x, y, c=colors, s=sizes)

    plt.show()


def main():
    a = np.array([
        [3, 5, "xkcd:puke green", 100],
        [4, 6, "xkcd:baby shit brown", 1],
        [5, 7, "xkcd:baby poop", 4],
        [6, 10, "xkcd:puke brown", 200]
    ], dtype=object)

    subfigures(a)
if __name__ == "__main__":
    main()
    