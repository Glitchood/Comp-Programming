import sys

sys.stdin = open("test.in", "r")

T = int(input())
for _ in range(T):
    n = int(input())
    s = str(input().strip())
    print(s.count("1") * (n - 2) + n)
