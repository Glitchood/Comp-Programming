#cpid=664
import sys
from collections import Counter

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

n = int(input())
words = [input().split() for _ in range(n)]

def count_frequencies(w1, w2):
    freq1, freq2 = dict(Counter(w1)), dict(Counter(w2))
    for c in freq2.keys():
        freq1[c] = max(freq1.get(c, 0),freq2.get(c,0))
    return freq1

def combine_dicts(dict1, dict2):
    for key in dict2.keys():
        dict1[key] = dict1.get(key,0) + dict2.get(key,0)
    return dict1

def convert_freq_to_list(freq_dict):
    max_freqs = [0] * 26
    for char in list(freq_dict.keys()):
        max_freqs[ord(char) - ord('a')] = freq_dict.get(char)
    return max_freqs

freq_dict = {}

for word1, word2 in words:
    freq_dict = combine_dicts(freq_dict, count_frequencies(word1, word2))

for x in convert_freq_to_list(freq_dict):
    print(x, end="\n")