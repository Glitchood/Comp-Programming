# cpid=615
import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")
X, Y, M = map(int, input().split())

for N in reversed(range(M + 1)):
    m = N
    while m >= X:
        if (not m % X) or (not m % Y):
            print(N)
            exit()
        m -= Y
