import sys

sys.stdin = open("I.in")


def solve():
    N = int(input())
    A_str = list(map(int, input().split()))
    B_str = list(map(int, input().split()))

    MOD = 10**9 + 7

    # Using 0-indexed node labels from 0 to N-1 for convenience
    # Node 0 in code corresponds to location 1 in problem
    # Node 1 in code corresponds to location 2 in problem

    # d1[i] = distance from node i to node 0
    # d2[i] = distance from node i to node 1
    d1 = [0] * N
    d2 = [0] * N
    for i in range(N):
        d1[i] = int(A_str[i])
        d2[i] = int(B_str[i])

    # Basic checks for fixed points (node 0 and node 1)
    if d1[0] != 0:  # Distance from node 0 to itself must be 0
        print(0)
        return
    if d2[1] != 0:  # Distance from node 1 to itself must be 0
        print(0)
        return

    # D is the distance between node 0 and node 1
    D = d1[1]

    # D must be positive (nodes 0 and 1 are distinct)
    # Problem constraints say N > 2, implying N >= 3.
    if D == 0:
        print(0)
        return

    # Distances must be symmetric: dist(0,1) == dist(1,0)
    if d2[0] != D:
        print(0)
        return

    # X[i] stores x_i, H[i] stores h_i for node i
    X = [0] * N
    H = [0] * N

    # coords maps (x_val, h_val) to list of node_indices having these coordinates
    coords = {}

    for i in range(N):
        # Calculate terms for h_i and x_i formulas
        # h_i = (d1[i] + d2[i] - D) / 2
        # x_i = (d1[i] - d2[i] + D) / 2
        sum_dist_term = d1[i] + d2[i] - D
        diff_dist_term = d1[i] - d2[i] + D

        # Numerators must be non-negative and even
        if sum_dist_term < 0 or sum_dist_term % 2 != 0:
            print(0)
            return
        if diff_dist_term < 0 or diff_dist_term % 2 != 0:
            print(0)
            return

        h_i = sum_dist_term // 2
        x_i = diff_dist_term // 2

        # x_i must be in range [0, D]
        # This is usually implied by triangle inequalities if distances are metric,
        # but good to check if inputs can be arbitrary.
        if x_i < 0 or x_i > D:
            print(0)
            return

        X[i] = x_i
        H[i] = h_i

        coord_pair = (x_i, h_i)
        if coord_pair not in coords:
            coords[coord_pair] = []
        coords[coord_pair].append(i)

    # Validate the main path P_01 (between node 0 and node 1)
    # P_k denotes the node on path P_01 at distance k from node 0.
    # For each k from 0 to D, there must be exactly one node P_k with (x=k, h=0).
    for k in range(D + 1):
        path_nodes_at_k = coords.get((k, 0), [])  # Nodes with (x=k, h=0)
        if len(path_nodes_at_k) != 1:
            print(0)
            return

        # P_0 must be node 0, and P_D must be node 1.
        # This check is technically redundant if d1[0]=0, d2[0]=D etc. were processed correctly,
        # as (x,h) for node 0 would be (0,0) and for node 1 would be (D,0).
        if k == 0 and path_nodes_at_k[0] != 0:
            print(0)
            return
        if k == D and path_nodes_at_k[0] != 1:
            print(0)
            return

    # Calculate total number of ways W
    W = 1
    for i in range(N):
        # Nodes on the main path (H[i]==0) have their connections fixed by the path structure.
        # Nodes with H[i]==1 must attach to P_{X[i]} (node on main path at x-coord X[i]).
        # This means their parent is uniquely determined (1 choice).
        # Only nodes with H[i] > 1 contribute choices to W.
        if H[i] > 1:
            # Parent of node i must be a node p with coordinates (X[i], H[i]-1).
            # Count how many such candidate parents exist.
            num_potential_parents = len(coords.get((X[i], H[i] - 1), []))

            if (
                num_potential_parents == 0
            ):  # Node i needs a parent, but no candidates exist.
                print(0)
                return

            W = (W * num_potential_parents) % MOD

    print(W)


solve()
