from collections import deque

N, M, K = map(int, input().split())
import sys

sys.stdin = open("H.in")
A_ops = [[] for _ in range(K + 1)]  # Machines are 1-based
B_ops = [[] for _ in range(K + 1)]

for _ in range(M):
    l = input().split()
    robot = int(l[0])
    machine = int(l[1])
    op = str(l[2])
    if op == "A":
        A_ops[machine].append(robot)
    else:
        B_ops[machine].append(robot)

total_nodes = N + K
adj = [[] for _ in range(total_nodes + 1)]  # 1-based indexing
indegree = [0] * (total_nodes + 1)

for machine in range(1, K + 1):
    a_list = A_ops[machine]
    b_list = B_ops[machine]
    virtual = N + machine
    # Add edges from A robots to virtual node
    for a in a_list:
        adj[a].append(virtual)
        indegree[virtual] += 1
    # Add edges from virtual node to B robots
    for b in b_list:
        adj[virtual].append(b)
        indegree[b] += 1

q = deque()
# Add real robots with indegree 0
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
# Add virtual nodes with indegree 0
for i in range(N + 1, total_nodes + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    u = q.popleft()
    if u <= N:
        result.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

if len(result) == N:
    print(" ".join(map(str, result)))
else:
    print(-1)
