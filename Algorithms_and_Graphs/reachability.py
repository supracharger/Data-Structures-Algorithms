#Uses python3

import sys

def reach(adj, x, y, visted):
    if x == y: return 1
    visted[x] = True
    for e in adj[x]:
        if not visted[e] and reach(adj, e, y, visted) == 1:
            return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [[v for v in map(int, input().split())] for _ in range(m+1)]

    #data = '4 4;1 2;3 2;4 3;1 4;1 4'
    #data = '4 2;1 2;3 2;1 4'
    #data = [[int(v) for v in l.split(' ')] for l in data.split(';')]
    #n, m = data[0]
    #data = data[1:]

    edges = data[:-1]
    x, y = data[-1]
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    #n, m = data[0:2]
    #data = data[2:]
    #edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    visted = [False] * n
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y, visted))
