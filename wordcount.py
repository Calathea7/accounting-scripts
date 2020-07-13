# put your code here.

import sys
from collections import Counter

filename = sys.argv[1]

def count_words(filename):

    all_data = open(filename)

    word_count = {}

    for line in all_data:

        words = line.strip().split(" ")

        for word in words:
            word = word.lower().strip('._,?!;:"')
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in sorted(word_count.items()):
        print(str(word) + " " + str(count))

count_words(filename)
        

 
