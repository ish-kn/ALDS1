from collections import deque

N = 100
INF = float('inf')

M = [[0 for j in xrange(N)] for i in xrange(N)]
d = [INF] * N
n = 0


def bfs(s):
    q = deque([])
    q.append(s)
    d[s] = 0
    while len(q):
        u = q.popleft()
        for v in xrange(n):
            if M[u][v] and d[v] == INF:
                d[v] = d[u] + 1
                q.append(v)
    for i in xrange(n):
        print i + 1, -1 if d[i] == INF else d[i]


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
    bfs(0)

if __name__ == '__main__':
    main()
