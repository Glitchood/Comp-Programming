# import sys
# sys.stdin=open('hoof.in','r')
n, m = map(int, input().split())

# Initialize beat matrix
beat = [[False] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    line = input().strip()
    for j in range(1, x + 1):
        y = j
        c = line[j - 1]
        if x == y:
            beat[x][y] = False
        else:
            if c == "W":
                beat[x][y] = True
                beat[y][x] = False
            elif c == "L":
                beat[x][y] = False
                beat[y][x] = True
            else:  # 'D'
                beat[x][y] = False
                beat[y][x] = False

for _ in range(m):
    s1, s2 = map(int, input().split())
    count = 0
    for x in range(1, n + 1):
        if beat[x][s1] and beat[x][s2]:
            count += 1
    print(count * (2 * n - count))
