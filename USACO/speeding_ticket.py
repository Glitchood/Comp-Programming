#cpid=568
import sys
sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

N,M=map(int, input().split())
road_segs = [[int(i) for i in input().split()] for _ in range(N)]
bessie_segs = [[int(i) for i in input().split()] for _ in range(M)]

r_sl = [x for xs in [[seg[1]]*seg[0] for seg in road_segs] for x in xs]
b_sl = [x for xs in [[seg[1]]*seg[0] for seg in bessie_segs] for x in xs]
answer = 0
for i in range(100):
    max(r_sl[i],b_sl[i])
    if b_sl[i] > r_sl[i]:
        score = b_sl[i] - r_sl[i]
        answer = max(answer, score)

print(answer)