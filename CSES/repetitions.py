# 1069
s = str(input())
current = ""
count = 0
ans = 0
for i in range(len(s)):
    if s[i] != current:
        current = s[i]
        count = 0
    if s[i] == current:
        count += 1

    ans = max(ans, count)

print(ans)
