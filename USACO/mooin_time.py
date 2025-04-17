# cpid=1468
n = int(input())
a = list(map(int, input().split()))

moos = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[j] == a[k] and a[i] != a[j]:
                moos.add((a[i], a[j], a[k]))

print(len(moos))
