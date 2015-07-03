N = 100
WHITE = 0
GRAY = 1
BLACK = 2

n = tt = 0
M = [[0 for j in xrange(N)] for i in xrange(N)]
color = [WHITE] * N
nt, d, f = [0] * N, [0] * N, [0] * N


def next(u):
    for v in xrange(nt[u], n):
        nt[u] = v + 1
        if M[u][v]:
            return v
    return -1


def dfs_visit(u):
    global nt, tt
    nt = [0] * N
    S = []  # stack
    S.append(u)
    color[u] = GRAY
    tt += 1
    d[u] = tt

    while len(S):
        u = S[len(S) - 1]
        v = next(u)
        if v != -1:
            if color[v] == WHITE:
                color[v] = GRAY
                tt += 1
                d[v] = tt
                S.append(v)
        else:
            S.pop()
            color[u] = BLACK
            tt += 1
            f[u] = tt


def dfs():
    for u in xrange(n):
        if color[u] == WHITE:
            dfs_visit(u)
    for i in xrange(n):
        print i + 1, d[i], f[i]


def main():
    global n
    n = input()
    for i in xrange(n):
        t = map(int, raw_input().split())
        u, k, vA = t[0], t[1], t[2:]
        u -= 1
        for v in vA:
            v -= 1
            M[u][v] = 1
    dfs()

if __name__ == '__main__':
    main()
