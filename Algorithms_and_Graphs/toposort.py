#Uses python3

import sys

def dfs(adj, used, order, x):
    used[x] = True
    for e in adj[x]:
        if not used[e]:
            dfs(adj, used, order, e)
    order.append(x)

def toposort(adj):
    used = [False] * len(adj)
    order = []
    for x in range(len(adj)):
        if not used[x]:
            dfs(adj, used, order, x)
    return order[::-1]

def toposort_old(adj):
    #used = [0] * len(adj)
    order = []
    while len(order) != len(adj):
        found = FindAllSinks(adj)
        for ix in found:
            Remove(ix, adj)
        order.extend(found)
    return order[::-1]

def Remove(idx, adj):
    adj[idx] = None
    for a in adj:
        if a is None: continue
        if idx in a:
            a.remove(idx)

def FindAllSinks(adj):
    return [i for i,a in enumerate(adj) if a!=None and len(a)==0]

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    #data = '4 3;1 2;4 1;3 1'
    #data = '4 1;3 1'
    #data = '5 7;2 1;3 2;3 1;4 3;4 1;5 2;5 3'
    #data = [list(map(int, l.split())) for l in data.split(';')]
    #n, m = data[0]
    #edges = data[1:]

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

