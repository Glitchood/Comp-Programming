import sys
sys.stdin=open('test.in','r')

T=int(input())
for _ in range(T):
    n=int(input())
    x=str(input())
    t=x[::-1]
    enc = []
    i=0
    while i < n:
        if t[i] == '0':
            add=(t[i+2]+t[i+1])
            i+=3
        else:
            add=t[i]
            i+=1
        enc.append(add)
    enc.reverse()
    ans = ""
    for k in enc:
        ans+=(chr(96+int(k)))
    print(ans)