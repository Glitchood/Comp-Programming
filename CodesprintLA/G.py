import sys

sys.stdin = open("G.in")
N, M = map(int, input().split())
grid = [[0] * N for _ in range(N)]

if M % 2 == 1:  # Odd M
    # We want P-E = M.
    # Construct L-chain for M+1, then remove grid[0][0].
    # L-chain for P-E = M_even uses k = M_even/2 + 1.
    # Here M_even = M + 1.
    k = (M + 1) // 2 + 1

    # grid[j][j] = 1 for j = 0,...,k
    # grid[j][j+1] = 1 for j = 0,...,k-1
    # But skip grid[0][0]

    for j in range(k + 1):
        if j == 0:  # Skip setting grid[0][0]
            continue
        if j < N:  # Check bounds for grid[j][j]
            grid[j][j] = 1

    for j in range(k):  # 0 to k-1
        # grid[j][j+1]
        if j < N and j + 1 < N:  # Check bounds
            grid[j][j + 1] = 1

else:  # Even M
    # We want P-E = M.
    # L-chain for P-E = M uses k = M/2 + 1.
    k = M // 2 + 1

    for j in range(k + 1):  # 0 to k
        if j < N:  # Check bounds for grid[j][j]
            grid[j][j] = 1

    for j in range(k):  # 0 to k-1
        # grid[j][j+1]
        if j < N and j + 1 < N:  # Check bounds
            grid[j][j + 1] = 1

for i in range(N):
    print("".join(map(str, grid[i][0:N])))
