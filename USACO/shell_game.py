# cpid=891
import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

n = int(input())

swaps = []
for i in range(n):
    swaps.append(list(map(int, input().split())))

answer = 0

for i in range(3):
    shells = [0] * 3  # [0, 0, 0]
    score = 0
    shells[i] = 1  # [1, 0, 0]
    for a, b, g in swaps:
        a, b, g = a - 1, b - 1, g - 1
        shells[a], shells[b] = shells[b], shells[a]
        if shells[g]:
            score += 1
            answer = max(answer, score)

print(answer)
