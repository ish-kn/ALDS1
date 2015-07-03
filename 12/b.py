MAX = 100
INF = float('inf')
WHITE = 0
GRAY = 1
BLACK = 2

n = 0
M = [[INF for j in xrange(MAX)] for i in xrange(MAX)]


def dijkstra():
    d = [INF] * n
    color = [WHITE] * n

    d[0] = 0
    color[0] = GRAY
    while 1:
        minv = INF
        u = -1
        for i in xrange(n):
            if minv > d[i] and color[i] != BLACK:
                u = i
                minv = d[i]
        if u == -1:
            break
        color[u] = BLACK
        for v in xrange(n):
            if color[v] != BLACK and M[u][v] != INF:
                if d[v] > d[u] + M[u][v]:
                    d[v] = d[u] + M[u][v]
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
            M[u][v] = c

    dijkstra()

if __name__ == '__main__':
    main()
