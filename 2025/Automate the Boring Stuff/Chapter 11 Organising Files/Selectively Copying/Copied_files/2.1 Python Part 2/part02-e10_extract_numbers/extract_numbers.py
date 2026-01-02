#!/usr/bin/env python3

def extract_numbers(s):
    result = []
    for element in s.split():
        try:
            result.append(int(element))
        except ValueError:
            try:
                result.append(float(element))
            except:
                pass
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
