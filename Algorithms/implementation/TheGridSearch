t = int(input())


def checkMatch2(G, P, R, C, r, c):
    i = j = 0
    x = y = 0
    foundIndex = 0
    while i < r:
        x = i
        j = y = 0
        while j < c:
            if P[i][j] == G[x][y]:
                foundIndex = j

def findMatch(G, P, startIndex):
    foundIndex = G[startIndex:].find(P[0][:])

def checkMatch(G, P, R, C, r, c):
    i = 0
    x = 0
    result = True
    while i < R:
        j = 0
        while j < C:
            foundIndex = G[i].find(P[x][:], j)
            if foundIndex != -1:
                y = i + 1
                x += 1
                result = True
                while y < R and x < r:
                    nextIndex = G[y].find(P[x][:], foundIndex)
                    if nextIndex == foundIndex:
                        result = True
                    else:
                        result = False
                        j = foundIndex + 1
                        y = 0
                        x = 0
                        break
                    y += 1
                    x += 1
                if x == r and result:
                    break
                else:
                    result = False
            else:
                j += 1
                result = False
            x = 0
        if result:
            break
        i += 1
    if result:
        print("YES")
    else:
        print("NO")


for a0 in range(t):
    R, C = [int(a_temp) for a_temp in input().strip().split(' ')]
    G = []
    for _ in range(R):
        G_j = input().strip()
        G.append(G_j)
    r, c = [int(a_temp) for a_temp in input().strip().split(' ')]
    P = []
    for _ in range(r):
        P_j = input().strip()
        P.append(P_j)
    checkMatch(G, P, R, C, r, c)
