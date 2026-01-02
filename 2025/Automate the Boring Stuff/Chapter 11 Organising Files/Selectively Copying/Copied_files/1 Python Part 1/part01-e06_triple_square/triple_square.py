#!/usr/bin/env python3
def triple(a):
    return 3 * a

def square(a):
    return a ** 2

def main():
    for i in range(10):
        i_squared = square(i+1)
        i_tripled = triple(i+1)
        if i_squared > i_tripled:
            break
        else:
            print(f"triple({i+1})=={i_tripled} square({i+1})=={i_squared}")

if __name__ == "__main__":
    main()
