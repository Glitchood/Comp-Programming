#cpid=617
import sys
sys.stdin = open("balancing.in","r")
sys.stdout = open('balancing.out','w')
N,B=map(int,input().split())
coords = [tuple(map(int, input().split())) for _ in range(N)]

x_vals = sorted(set(x for x,y in coords))
y_vals = sorted(set(y for x,y in coords))

answer = float('inf')

for a in x_vals:
    a+=1
    upper=[]
    lower=[]
    for x,y in coords:
        if x<a:
            lower.append(y)
        else:
            upper.append(y)
    lower.sort()
    upper.sort()

    BL = BR = i = j = 0
    TL = len(lower)
    TR = len(upper)

    for b in y_vals:
        b+=1
        while i < len(lower) and lower[i] < b:
            i+=1
            BL+=1
            TL-=1
        while j < len(upper) and upper[j] < b:
            j+=1
            BR+=1
            TR-=1

        answer = min(answer, max(TL, TR, BL, BR))

print(answer)

