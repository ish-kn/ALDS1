MAX = 100000
NIL = -1

n = 0
G = [[] for i in xrange(MAX)]
color = [NIL] * MAX


def dfs(r, c):
    S = []
    S.append(r)
    color[r] = c
    while len(S):
        u = S.pop()
        for i in xrange(len(G[u])):
            v = G[u][i]
            if color[v] == NIL:
                color[v] = c
                S.append(v)


def assignColor():
    id = 1
    for u in xrange(n):
        if color[u] == NIL:
            dfs(u, id)
            id += 1


def main():
    global n
    n, m = map(int, raw_input().split())
    for i in xrange(m):
        s, t = map(int, raw_input().split())
        G[s].append(t)
        G[t].append(s)

    assignColor()

    q = input()
    for i in xrange(q):
        s, t = map(int, raw_input().split())
        print 'yes' if color[s] == color[t] else 'no'

if __name__ == '__main__':
    main()
