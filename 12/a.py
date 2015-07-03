MAX = 100
INF = float('inf')
WHITE = 0
GRAY = 1
BLACK = 2

n = 0
M = [[INF for j in xrange(MAX)] for i in xrange(MAX)]


def prim():
    color = [WHITE] * n
    d = [INF] * n
    p = [-1] * n

    d[0] = 0

    while 1:
        minv = INF
        u = -1
        for i in xrange(n):
            if color[i] != BLACK and d[i] < minv:
                u = i
                minv = d[i]
        if u == -1:
            break
        color[u] = BLACK
        for v in xrange(n):
            if color[v] != BLACK and M[u][v] != INF:
                if M[u][v] < d[v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = GRAY
    ans = 0
    for i in xrange(n):
        if p[i] != -1:
            ans += M[i][p[i]]
    return ans


def main():
    global n
    n = input()
    for i in xrange(n):
        e = map(int, raw_input().split())
        for j in xrange(n):
            if e[j] != -1:
                M[i][j] = e[j]
    print prim()

if __name__ == '__main__':
    main()
