#Uses python3
# import sys
import math

def CreateEdges(x, y):
    adjCost = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j: continue
            euc = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            adjCost.append((i, j, euc))
    return adjCost

def Union(u, v, theSet):
    old, new = theSet[v], theSet[u]
    theSet[v] = new
    for k,v in theSet.items():
        if v == old:
            theSet[k] = new

def minimum_distance(x, y):
    theSet = {i:i for i in range(len(x))}
    X = []
    adjCost = CreateEdges(x, y)
    ensum = 0
    for u,v,cst in sorted(adjCost, key=lambda a: a[2]):
        if theSet[v] != theSet[u]:
            ensum += cst
            Union(u, v, theSet)
    return ensum
    # adjFlat = [(i, j) for i in range(len(x)) for j in adj[i]]
    # costFlat = [(i, j) for i in range(len(x)) for j in range(len(cost[i]))]
    # def ToCost(ix):
    #     i, j = costFlat[ix]
    #     return cost[i][j]
    # index = sorted(range(len(adjFlat)), key=ToCost)




if __name__ == '__main__':
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n)]

    # data = '4;0 0;0 1;1 0;1 1'
    # data = '5;0 0;0 2;1 1;3 0;3 2'
    # data = '9;0 0;1 1;2 -3;3 6;4 -4;5 8;6 -7;7 12;8 -11'
    # data = [list(map(int, d.split())) for d in data.split(';')]
    # n = data[0]
    # edges = data[1:]

    x, y = zip(*edges)
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
