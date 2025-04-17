import sys
sys.stdin=open('vlad.in','r')

T = int(input())
for i in range(T):
    a,b,c=map(int, input().split())
    a_=abs(a-1)
    b_=abs(b-c)+abs(c-1)
    if a_ < b_:
        print(1)
    elif a_ == b_:
        print(3)
    else:
        print(2)