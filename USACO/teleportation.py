# cpid=807
import sys

sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")

a, b, x, y = map(int, input().split())

if a > b:
    a, b = b, a
if x > y:
    x, y = y, x

base = b - a

teleport = abs(x - a) + abs(y - b)

print(min(base, teleport))
