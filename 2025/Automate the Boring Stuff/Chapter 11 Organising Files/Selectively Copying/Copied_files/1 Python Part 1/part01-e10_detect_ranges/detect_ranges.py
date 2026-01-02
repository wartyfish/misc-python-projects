#!/usr/bin/env python3

def detect_ranges(L):
    S = sorted(L)
    result = []
    start = S[0]
    end = S[0]

    step = 1
    for num in S[1:]:
        step += 1

        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(start)

            if start != end:
                result.append((start, end + 1))
            start = end = num

        if num == S[-1]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    result.append(start)

                if start != end:
                    result.append((start, end + 1))
                start = end = num

    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
