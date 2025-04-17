# cpid=963
import sys

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")
K, N = map(int, input().split())


def compare(list1, list2):
    return list(set(list1) & set(list2))


def get_greater(integer, session):
    idx = session.index(integer)
    return list(session[idx + 1 :])


sessions = []
for _ in range(K):
    sessions.append(list(map(int, input().split())))
count = 0
for i in range(1, N + 1):
    greater_cows = [get_greater(i, sessions[0])]
    for j in range(K):
        greater_cows.append(get_greater(i, sessions[j]))
        greater_cows = [compare(*greater_cows)]
    count += len(*greater_cows)
print(count)
