from heapq import *

MAX = 10000
INF = float('inf')
WHITE = 0
GRAY = 1
BLACK = 2
FST = 0
SEC = 1

n = 0
adj = [[] for i in xrange(MAX)]


def dijkstra():
    PQ = []
    d = [INF] * n
    color = [WHITE] * n

    d[0] = 0
    heappush(PQ, (0, 0))
    color[0] = GRAY
    while len(PQ):
        f = heappop(PQ)
        u = f[SEC]
        color[u] = BLACK
        # if d[u] < f[FST]:
        # continue
        for j in xrange(len(adj[u])):
            v = adj[u][j][FST]
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + adj[u][j][SEC]:
                d[v] = d[u] + adj[u][j][SEC]
                heappush(PQ, (d[v], v))
                color[v] = GRAY

    for i in xrange(n):
        print i, d[i]


def main():
    global n
    n = input()
    for i in xrange(n):
        t = map(int, raw_input().split())
        u, k, t = t[0], t[1], t[2:]
        for j in xrange(0, 2 * k, 2):
            v, c = t[j], t[j + 1]
            adj[u].append((v, c))

    dijkstra()

if __name__ == '__main__':
    main()
