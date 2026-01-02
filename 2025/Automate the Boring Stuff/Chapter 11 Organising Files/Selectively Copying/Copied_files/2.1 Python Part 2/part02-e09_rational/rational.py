#!/usr/bin/env python3

class Rational(object):
    def __init__(self, n1, n2):
        self.num = n1
        if n2 != 0:
            self.den = n2
        else:
            raise ValueError("Denominator cannot equal zero")
        self.value = n1 /n2

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __repr__(self):
        return f"Rational({self.num}, {self.den})"
    
    def __add__(self, other):
        n = self.num * other.den + other.num * self.den 
        d = self.den * other.den
        return Rational(n, d)
    
    def __sub__(self, other):
        n = self.num * other.den - other.num * self.den 
        d = self.den * other.den
        return Rational(n, d)
    
    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Rational(n, d)
    
    def __truediv__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Rational(n, d)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __lt__(self, other):
        return self.value < other.value

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
