#!/usr/bin/env python3
import re

def word_frequencies(filename):
    word_count = {}
    with open(filename, "r") as book:
        for line in book:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""").lower()
                #if word not in word_count:
                #    word_count[word] = 1
                #else:
                #    word_count[word] +=1
                if re.fullmatch(r"[a-z']+", word):
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1

    return word_count
    

def main():
    word_count = word_frequencies("alice.txt")
    words_sorted = {word: word_count[word] for word, count in sorted(word_count.items(), key = lambda item: item[1], reverse=True)}

    with open("count.csv", "w") as output:
        for word in words_sorted:
            output.write(f"{word},{words_sorted[word]}\n")

if __name__ == "__main__":
    main()
