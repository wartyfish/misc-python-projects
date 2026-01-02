#!/usr/bin/env python3

def reverse_dictionary(d):
    r_d = {}
    for k in d:
        for w in d[k]:
            if w not in r_d:
                r_d[w] = []
            r_d[w].append(k)
    return r_d

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    r_d = reverse_dictionary(d)
    print(r_d)

if __name__ == "__main__":
    main()
