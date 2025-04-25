import sys
sys.stdin=open('test.in','r')



T=int(input())
for _ in range(T):
    k=int(input())
    sum_k = k * (k + 1) // 2
    if not sum_k % k:
        print("YES")
    else:
        print("NO")