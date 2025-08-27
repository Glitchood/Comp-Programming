import sys
sys.stdin=open('expectedSolve.in','r')

def mex(arr):
    seen = set()
    for x in arr:
        seen.add(x)
    mex = 0
    while mex in seen:
        mex += 1
    return mex
T=int(input())
for _ in range(T):
    n,x=map(int, input().split())
    arr=list(map(int,input().split()))
    mex_values = []
    for i in range(len(arr)):
        mex_values.append(mex(arr[:i+1]))
    print(f"Input: {arr} \n MEXes: {mex_values} \n {x} count: {mex_values.count(x)}\n")