#1083
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
for i in range(n):
    try:
        if numbers[i] != i+1:
            print(i+1)
            break
    except:
        print(n)
    # try-except to get cases 11,13 since they are the last ones