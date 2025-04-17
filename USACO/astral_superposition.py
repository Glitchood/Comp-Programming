#cpid=1467
# import sys #
# sys.stdin = open("USACO/astral.in", "r") #

T = int(input())

def isInGrid(coords,N):
    i,j=coords
    if i<0 or j<0 or i>=N or j>=N:
        return False
    else:
        return True
    
def getColorFromCoords(coords,N):
    global starGrid
    i,j=coords
    if isInGrid((i,j),N):
        return starGrid[i][j]
    else:
        return 0

for j in range(T):
    # print("\nNEW TESTCASE")
    N, A, B = map(int, input().split())
    starGrid = []
    for i in range(N):
        inp = input()
        replace = str.maketrans({"W":"0","G":"1","B":"2"})
        res = inp.translate(replace)
        starGrid.append(list(map(int, res)))
    
    count = 0
    if (A,B) == (0,0):
        gridd = [x for xs in starGrid for x in xs]
        for term in gridd:
            if term:
                count+=1
    else:
        for i in reversed(range(len(starGrid))):
            for j in reversed(range(len(starGrid[i]))):
                color = starGrid[i][j]
                coords = (i,j)
                previousCoords = (i-B,j-A)
                if color:
                    previousColor = getColorFromCoords(previousCoords,N)
                    if color == 2: 
                        starGrid[i][j]-= 1
                        count+=1
                    elif not previousColor:
                        starGrid[i][j]-=1
                        count+=1
                    if previousColor:
                        starGrid[i][j]-=1
                        starGrid[i-B][j-A] -=1
                        count+=1
        if sum([x for xs in starGrid for x in xs]) != 0:
            count = -1
            
                
    print(count)
