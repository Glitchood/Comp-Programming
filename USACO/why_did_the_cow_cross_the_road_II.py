#cpid=712
import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")
ans = 0
cs = input().strip()
for a in range(len(cs)):
    for b in range(a+1,len(cs)):
        for c in range(b+1,len(cs)):
            for d in range(c+1,len(cs)):
                ans+=(cs[a]==cs[c] and cs[b]==cs[d])
print(ans)