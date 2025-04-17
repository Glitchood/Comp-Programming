# gym/102951/problem/A
N = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
maximum = 0
for i in range(N):
    for j in range(i + 1, N):
        print(i, j)
        res = abs(xs[j] - xs[i]) ** 2 + abs(ys[j] - ys[i]) ** 2
        maximum = max(res, maximum)

print(maximum)
