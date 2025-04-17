def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        cows = list(map(int, input().split()))

        freq = [0] * (N + 2)
        for h in cows:
            freq[h] += 1

        has_two = [False] * (N + 2)
        for h in range(1, N + 1):
            if freq[h] >= 2:
                has_two[h] = True

        prefix = [0] * (N + 2)
        count = 0
        for h in range(1, N + 1):
            prefix[h] = count
            if has_two[h]:
                count += 1

        max_len = 0
        for h in range(1, N + 1):
            if freq[h] >= 1:
                current_len = 2 * prefix[h] + 1
                if current_len > max_len:
                    max_len = current_len
        print(max_len)


solve()
