#Uses python3

import sys
import queue

def BFS(adj, s):
    dist = [-1] * len(adj)
    visted = [False] * len(adj)
    dist[s] = 0
    que = [s]
    while len(que) > 0:
        u = que[0]
        del que[0]
        for v in adj[u]:
            if not visted[v]:
                que.append(v)
                dist[v] = dist[u] + 1
                visted[v] = True
    return dist

def distance(adj, s, t):
    dist = BFS(adj, s-1)
    return dist[t-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s, t = map(int, input().split())

    # data = '4 4;1 2;4 1;2 3;3 1;2 4'
    # data = '5 4;5 2;1 3;3 4;1 4;3 5'
    # data = [list(map(int, d.split())) for d in data.split(';')]
    # n, m = data[0]
    # s, t = data[-1]
    # edges = data[1:-1]

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
