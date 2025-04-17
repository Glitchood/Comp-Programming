#cpid=736
import sys
sys.stdin = open("cownomics.in","r")
sys.stdout = open("cownomics.out","w")

N, M = map(int,input().split())
s_g = [list(input()) for _ in range(N)]
p_g = [list(input()) for _ in range(N)]

count = 0
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            s_ = { (s_g[n][i],s_g[n][j],s_g[n][k]) for n in range(N) }
            p_ = { (p_g[n][i],p_g[n][j],p_g[n][k]) for n in range(N) }
            if s_.isdisjoint(p_):
                count+=1
print(count)