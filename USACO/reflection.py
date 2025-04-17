#cpid=1479
import sys
sys.stdin = open("reflection.in", "r")

def main():
    N, U = map(int, input().split())
    
    # Read the canvas as a list of lists
    canvas = [list(input().strip()) for _ in range(N)]
    
    # Precompute group indices for each cell
    mid = N // 2
    group_index = {}
    group_counts = []
    
    for r in range(mid):
        for c in range(mid, N):
            cells = [(r, c), (r, N - c - 1), (N - r - 1, c), (N - r - 1, N - c - 1)]
            group_id = len(group_counts)
            group_counts.append(sum(canvas[x][y] == '#' for x, y in cells))
            for x, y in cells:
                group_index[(x, y)] = group_id
    
    # Compute the initial total operations
    total_ops = sum(min(count, 4 - count) for count in group_counts)
    print(total_ops)
    
    # Process updates
    for _ in range(U):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        
        if (r, c) in group_index:
            group_id = group_index[(r, c)]
            painted = group_counts[group_id]
            empty = 4 - painted
            total_ops -= min(painted, empty)
            
            if canvas[r][c] == '#':
                group_counts[group_id] -= 1
            else:
                group_counts[group_id] += 1
            
            painted = group_counts[group_id]
            empty = 4 - painted
            total_ops += min(painted, empty)
        
        # Toggle the cell
        canvas[r][c] = '.' if canvas[r][c] == '#' else '#'
        
        print(total_ops)

if __name__ == "__main__":
    main()
