from bisect import bisect_left, bisect_right

def main():
    # Read inputs
    N, Q = map(int, input().split())
    s = input().strip()
    
    # Precompute pos: positions where each letter occurs (1-indexed)
    pos = {chr(97 + i): [] for i in range(26)}
    for idx, ch in enumerate(s, start=1):
        pos[ch].append(idx)
    
    # Precompute non: positions where s[i] != letter.
    # Instead of iterating 26 times per character, we can compute for each letter by subtracting.
    full = list(range(1, N+1))
    non = {}
    for c in pos:
        # merge difference between full and pos[c]
        res = []
        # pos[c] is sorted and full is sorted.
        i, j = 0, 0
        m, n_full = len(full), len(pos[c])
        while i < m and j < n_full:
            if full[i] < pos[c][j]:
                res.append(full[i])
                i += 1
            elif full[i] == pos[c][j]:
                i += 1
                j += 1
            else:
                j += 1
        # add the remaining elements
        if i < m:
            res.extend(full[i:])
        non[c] = res

    out_lines = []
    # Process each query
    for _ in range(Q):
        l, r = map(int, input().split())
        best = -1
        # For each letter c, try to get a valid (i,j,k) triple
        for c in pos:
            # Find candidate i from non[c]: the smallest index in [l, r] where s[i] != c.
            arr_non = non[c]
            pos_i = bisect_left(arr_non, l)
            if pos_i == len(arr_non) or arr_non[pos_i] > r:
                continue
            candidate_i = arr_non[pos_i]
            
            # For the occurrences of letter c in [l, r]:
            arr_pos = pos[c]
            # We need j and k with j > candidate_i and k in [l, r]
            # j must be > candidate_i so we search for first index greater than candidate_i.
            j_left = bisect_left(arr_pos, candidate_i + 1)
            # k must be in [l, r]: get the last occurrence in arr_pos that is <= r.
            j_right = bisect_right(arr_pos, r) - 1
            
            # If not at least 2 occurrences exist or j_left is out of range, skip.
            if j_left > j_right:
                continue
            
            candidate_k = arr_pos[j_right]  # best candidate for k (largest index)
            # The product is (j - candidate_i) * (candidate_k - j) for a chosen j in arr_pos[j_left:j_right+1].
            # The maximum is achieved when j is as close as possible to the midpoint of candidate_i and candidate_k.
            mid = (candidate_i + candidate_k) // 2
            idx = bisect_left(arr_pos, mid, j_left, j_right + 1)
            # Check candidates: one at index idx and one at idx-1 if available.
            for candidate_j_index in (idx - 1, idx):
                if j_left <= candidate_j_index <= j_right:
                    candidate_j = arr_pos[candidate_j_index]
                    # Ensure ordering: candidate_i < candidate_j < candidate_k
                    if candidate_i < candidate_j < candidate_k:
                        val = (candidate_j - candidate_i) * (candidate_k - candidate_j)
                        if val > best:
                            best = val
        out_lines.append(str(best))
    
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
