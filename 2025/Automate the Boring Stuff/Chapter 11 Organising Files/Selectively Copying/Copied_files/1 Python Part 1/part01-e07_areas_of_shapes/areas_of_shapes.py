#!/usr/bin/env python3

import math

def triangle(b, h):
    return 0.5 * b * h

def rectangle(w, h):
    return w * h

def circle(r):
    return math.pi * r ** 2

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")

        if shape == "":
            break

        elif shape == "triangle":
            b = int(input("Give base of the triangle: "))
            h = int(input("Give height of the triangle: "))
            print("The area is", triangle(b, h))

        elif shape == "rectangle":
            w = int(input("Give width of the rectangle: "))
            h = int(input("Give height of the rectangle: "))
            print("The area is", rectangle(w, h))

        elif shape == "circle":
            r = int(input("Give radius of circle: "))
            print("The area is ", circle(r))

        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
