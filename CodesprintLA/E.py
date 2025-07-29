n, k = map(int, input().split())
existing = []
blocked_n = [False] * (n + 2)  # 1-based to n, with 0 and n+1 as dummy
blocked_s = [False] * (n + 2)

for _ in range(k):
    a, b = map(int, input().split())
    existing.append((a, b))
    # Mark the existing seat as blocked
    if a == 1:
        blocked_n[b] = True
    else:
        blocked_s[b] = True
    # Mark adjacent seats
    if a == 1:
        if b - 1 >= 1:
            blocked_n[b - 1] = True
        if b + 1 <= n:
            blocked_n[b + 1] = True
        # Mark cross seat
        blocked_s[b] = True
    else:
        if b - 1 >= 1:
            blocked_s[b - 1] = True
        if b + 1 <= n:
            blocked_s[b + 1] = True
        # Mark cross seat
        blocked_n[b] = True

# Precompute available arrays
available_n = [not blocked_n[i] for i in range(n + 2)]
available_s = [not blocked_s[i] for i in range(n + 2)]

# DP arrays
INF = -(10**18)
dp_0 = [0] * (n + 1)
dp_1 = [INF] * (n + 1)
dp_2 = [INF] * (n + 1)
back_0 = [-1] * (n + 1)
back_1 = [-1] * (n + 1)
back_2 = [-1] * (n + 1)

# Initialize i=1
if available_n[1]:
    dp_1[1] = 1
    back_1[1] = 0  # previous state is 0 (nothing)
if available_s[1]:
    dp_2[1] = 1
    back_2[1] = 0

for i in range(2, n + 1):
    # State 0: neither taken
    max_prev = max(dp_0[i - 1], dp_1[i - 1], dp_2[i - 1])
    dp_0[i] = max_prev
    # Determine back_0[i]
    if max_prev == dp_0[i - 1]:
        back_0[i] = 0
    elif max_prev == dp_1[i - 1]:
        back_0[i] = 1
    else:
        back_0[i] = 2

    # State 1: north taken
    if available_n[i]:
        candidates = [dp_0[i - 1], dp_2[i - 1]]
        max_prev = max(candidates)
        dp_1[i] = max_prev + 1
        if max_prev == dp_0[i - 1]:
            back_1[i] = 0
        else:
            back_1[i] = 2

    # State 2: south taken
    if available_s[i]:
        candidates = [dp_0[i - 1], dp_1[i - 1]]
        max_prev = max(candidates)
        dp_2[i] = max_prev + 1
        if max_prev == dp_0[i - 1]:
            back_2[i] = 0
        else:
            back_2[i] = 1

max_total = max(dp_0[n], dp_1[n], dp_2[n])
total_M = k + max_total

# Backtrack to find selected seats
selected_n = set()
selected_s = set()
current_state = -1
max_val = max(dp_0[n], dp_1[n], dp_2[n])
if max_val == dp_0[n]:
    current_state = 0
elif max_val == dp_1[n]:
    current_state = 1
else:
    current_state = 2

i = n
while i >= 1:
    if current_state == 1:
        selected_n.add(i)
    elif current_state == 2:
        selected_s.add(i)
    # Get previous state
    if current_state == 0:
        prev_state = back_0[i]
    elif current_state == 1:
        prev_state = back_1[i]
    else:
        prev_state = back_2[i]
    current_state = prev_state
    i -= 1

# Prepare output
north = ["."] * n
south = ["."] * n

for a, b in existing:
    if a == 1:
        north[b - 1] = "X"
    else:
        south[b - 1] = "X"

for b in selected_n:
    north[b - 1] = "X"
for b in selected_s:
    south[b - 1] = "X"

print(total_M)
print("".join(north))
print("".join(south))
