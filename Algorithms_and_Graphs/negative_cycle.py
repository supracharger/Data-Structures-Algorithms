#Uses python3

import sys

def check_cycle(adj, cost, possible, prev):
    for p in possible:
        start = p
        last = nxt = p
        sumCost = 0
        while True:
            nxt = prev[nxt]
            sumCost += cost[nxt][adj[nxt].index(last)]
            last = nxt
            if nxt == None: break
            elif nxt == start: 
                if sumCost < 0: return 1
                else: break
    return 0

def negative_cycle_old(adj, cost):
    possibleCycles = []
    prev = [None] * len(adj)
    dist = [float('inf')] * len(adj)
    for c in range(len(adj)):
        didRelax = False
        for u, edges in enumerate(adj):
            if dist[u] == float('inf'):
                dist[u] = 0
            for i,v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    prev[v] = u
                    didRelax = True
                    if c == 1: possibleCycles.append(v)
        if not didRelax: break
    return check_cycle(adj, cost, possibleCycles, prev)

def negative_cycle(adj, cost):
    dist = [float('inf')] * len(adj)
    dist[0] = 0
    length = len(adj)
    while length > 0:
        ctr = 0
        for u, edges in enumerate(adj):
            for i,v in enumerate(edges):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    ctr += 1
        if ctr == 0:
            for i in range(len(adj)):
                if dist[i] == float('inf'):
                    dist[i] = 0
                    length = len(adj)
                    break
        length -= 1
    if ctr > 0: return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    # data = '4 4;1 2 -5;4 1 2;2 3 2;3 1 1'
    # data = [list(map(int, d.split())) for d in data.split(';')]
    # n, m = data[0]
    # edges = data[1:]

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # data = data[3 * m:]

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
