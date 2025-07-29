import sys

sys.stdin = open("C.in")

import bisect

N, K = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
M = N // K
t = (K + 1) // 2
required = (K - t + 1) * M
count = 0
for x in s:
    lower = bisect.bisect_left(s, x)
    upper = bisect.bisect_right(s, x)
    c_ge = N - lower
    c_le = upper
    if c_ge >= t and c_le >= required:
        count += 1
print(count)
