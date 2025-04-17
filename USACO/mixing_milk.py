#cpid=855
import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

a,b,c = [[int(x) for x in input().split()] for _ in range(3)]

def pour(i1, i2):
    amt = min(i1[1],(i2[0]-i2[1]))
    i1[1] -= amt
    i2[1] += amt
    return i1, i2

loop = [a,b,c]

for i in range(100):
    i1, i2, i3 = loop[i%3], loop[(i+1)%3], loop[(i+2)%3]
    i1, i2 = pour(i1,i2)
print(i1[1], i2[1], i3[1], sep="\n")