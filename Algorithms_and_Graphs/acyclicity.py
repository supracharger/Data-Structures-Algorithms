#Uses python3

import sys


def acyclic(adj):
    visted = [False] * len(adj)
    for find in range(len(adj)):
        # If there is a cycle
        if DFS(adj, adj[find], find, list(visted)):
            return 1
    return 0

def DFS(adj, edges, find, visted):
    for e in edges:
        if visted[e]: continue
        visted[e] = True
        if e == find or DFS(adj, adj[e], find, visted): 
            return True
    return False
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    #data = '4 4;1 2;4 1;2 3;3 1'
    #data = '5 7;1 2;2 3;1 3;3 4;1 4;2 5;3 5'
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
    print(acyclic(adj))
