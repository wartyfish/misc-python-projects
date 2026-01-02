#!/usr/bin/env python3

def merge(L1, L2):
    i, j = 0, 0
    L = []
    
    # Merge while both lists have elements
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    
    # Add remaining elements (one of these will be empty)
    L.extend(L1[i:])
    L.extend(L2[j:])

    return L

def main():
    pass

if __name__ == "__main__":
    main()
