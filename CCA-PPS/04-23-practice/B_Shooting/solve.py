import sys
sys.stdin=open('test.in','r')
n = int(input())
a = list(map(int, input().split()))

cans = []
for i in range(n):
    cans.append((a[i], i + 1))

cans.sort(reverse=True)

total_shots = 0
order = []
for i in range(n):
    total_shots += cans[i][0] * i + 1
    order.append(cans[i][1])

print(total_shots)
print(*order)