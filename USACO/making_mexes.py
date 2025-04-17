# cpid=1480
import sys
from collections import defaultdict

N = int(input())
FjFavCows = list(map(int, input().split()))

freq = defaultdict(int)  # how many times each number (0=>N) appears in array
for num in FjFavCows:
    if num <= N:
        freq[num] += 1  # which numbers are present, which are missing

# Precompute the number of missing numbers up to each index
prefix_missing = [0] * (N + 2)  # prefix_missing[i] is missing numbers in 0..i-1
current_missing = 0
for i in range(N + 1):
    prefix_missing[i] = current_missing
    if freq[i] == 0:
        current_missing += 1

# Calculate operations for each mex i
for i in range(N + 1):
    required_missing = prefix_missing[i]
    count_i = freq[i]
    operations = max(required_missing, count_i)  # same as x+y-min(x,y)
    print(operations)  # operations = prefix_missing[i] + freq[i] − overlap

# prefix_missing[i] == # operations to ADD a number to the array
# freq[i] == # operations to REMOVE/REPLACE i in the array
# overlap == # operations which could be saved by replacing i => a number in the array
