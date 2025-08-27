import sys
sys.stdin=open('test.in','r')

T = int(input())
for _ in range(T):
    n,x=map(int,input().split())
    p = []
    if x == 0:
        p=[0]
    else:
        pass