import sys
sys.stdin=open('test.in','r')
def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    x_left = max(x1, x3)
    y_bottom = max(y1, y3)
    x_right = min(x2, x4)
    y_top = min(y2, y4)
    if x_left < x_right and y_bottom < y_top:
        return [x_left, y_bottom, x_right, y_top]
    else:
        return None

def area(rect):
    if rect is None:
        return 0
    return (rect[2] - rect[0]) * (rect[3] - rect[1])


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())


w = [x1, y1, x2, y2]
b_1 = [x3, y3, x4, y4]
b_2 = [x5, y5, x6, y6]


A = intersect(w[0], w[1], w[2], w[3], b_1[0], b_1[1], b_1[2], b_1[3])
B = intersect(w[0], w[1], w[2], w[3], b_2[0], b_2[1], b_2[2], b_2[3])


if A is not None and B is not None:
    C = intersect(A[0], A[1], A[2], A[3], B[0], B[1], B[2], B[3])
else:
    C = None

O = area(A) + area(B) - area(C)

if O >= area(w):
    print("NO")
else:
    print("YES")