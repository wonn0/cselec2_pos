from dict import *
from structures import *

def tag_string(s):
    res = []
    #tokenization
    words = s.split()
    #tagging
    for word in words:
        res.append([word, lexicon[word]])
    return res

s = tag_string(input("Write a sentence here: "))

print(s)

