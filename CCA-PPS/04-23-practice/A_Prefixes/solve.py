import sys

sys.stdin = open("test.in", "r")
n = int(input())
s = list(input())
edits = 0
for i in range(0, n, 2):
    if s[i] == s[i + 1]:
        s[i + 1] = "a" if s[i + 1] == "b" else "b"
        edits += 1

print(edits)
print("".join(s))
