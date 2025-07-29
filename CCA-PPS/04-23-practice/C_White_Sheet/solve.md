## STRATEGY:
Black Rectangle 1: b_1, Black Rectangle 2: b_2
White rectangle: w
intersect(x,y) ==> returns rectangle of intersection between two rectangles `x` and `y` -> [a,b,c,d] (four coordinates)
area(z) ==> Returns area of rectangle `z` -> int (area)

## STEPS:
A,B=intersect(w,b_1),intersect(w,b_2)
C=intersect(A,B) (This could be null)
overlapping area (O) = area(A)+area(B)-area(C)
if O>area(w):
  return "NO"
else:
  return "YES"