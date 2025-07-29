import sys

sys.stdin = open("test.in", "r")
T = int(input())
for _ in range(T):
    n = input().strip()
    k = len(n)
    min_score = float("inf")
    digits_removed = 0

    for i in range(1, 2**k):  # Iterate from 1 to 2**k - 1 (avoid empty subsequence)
        mask = bin(i)[2:].zfill(k)  # Get binary, remove "0b", pad with zeros
        sub = ""
        for j in range(k):
            if mask[j] == "1":
                sub += n[j]
        if sub:
            m = mask.count("0")
            if int(sub) > 0:
                score = int(sub) / sum(map(int, sub))

                if score < min_score:
                    min_score = score
                    digits_removed = m
                elif score == min_score and m < digits_removed:
                    digits_removed = m
    print(digits_removed)
