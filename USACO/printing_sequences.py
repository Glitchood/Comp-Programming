# cpid=1481
def can_generate_sequence(N, K, sequence):
    # If K is 1, the sequence must consist of only one unique number
    if K == 1:
        unique_numbers = set(sequence)
        if len(unique_numbers) > 1:
            return False
        return True

    # If K is greater than 1, we need to find repeating patterns
    # We can try to find the smallest repeating unit and see if the sequence can be built using it
    for length in range(1, N + 1):
        if N % length != 0:
            continue
        pattern = sequence[:length]
        repeats = N // length
        if pattern * repeats == sequence:
            # Check if the pattern can be generated with at most K PRINT statements
            unique_numbers_in_pattern = set(pattern)
            if len(unique_numbers_in_pattern) <= K:
                return True
    return False


def main():
    import sys

    sys.stdin = open("printing_sequences.in", "r")
    T = int(input())
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx + 1])
        idx += 2
        sequence = list(map(int, data[idx : idx + N]))
        idx += N
        if can_generate_sequence(N, K, sequence):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
