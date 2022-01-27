#Uses python3

# import sys
# import queue


def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    # prev = [None] * len(adj)
    dist[s] = 0
    que = list(range(len(adj)))
    while len(que) > 0:
        u = min(que, key=lambda i:dist[i])
        for i,v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                # prev[v] = u
        que.remove(u)
    return dist[t] if dist[t]!=float('inf') else -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s, t = map(int, input().split())

    # data = '4 4;1 2 1;4 1 2;2 3 2;1 3 5;1 3'
    # data = '5 9;1 2 4;1 3 2;2 3 2;3 2 1;2 4 2;3 5 4;5 4 1;2 5 3;3 4 4;1 5'
    # data = '3 3;1 2 7;1 3 5;2 3 2;3 2'
    # data = [list(map(int, d.split())) for d in data.split(';')]
    # n, m = data[0]
    # s, t = data[-1]
    # edges = data[1:-1]

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
    # s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s-1, t-1))
