import sys

sys.stdin = open("A.in")


def get_min(i, j, k, R, C):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_val = float("inf")
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            min_val = min(min_val, k[ni][nj])
    return min_val


R, C, d = map(int, input().split())

# Read A matrix (raw depths)
A = []
for _ in range(R):
    A.append(list(map(int, input().split())))

# Compute k matrix
k = [[A[i][j] // d for j in range(C)] for i in range(R)]

# Generate and print the output grid
for i in range(R):
    row = ""
    for j in range(C):
        m = get_min(i, j, k, R, C)
        x = k[i][j]
        if x <= m:
            row += " "
        elif x == m + 1:
            row += "+"
        elif x == m + 2:
            row += "x"
        elif x >= m + 3:
            row += "#"
    print(row)
