import sys

p = sys.stdout.write
MAX = 100005
NIL = -1


class Node:

    def __init__(self):
        self.p = NIL
        self.l = NIL
        self.r = NIL

T = [None] * MAX
D = [0] * MAX


def printC(u):
    p('node ' + str(u) + ': parent = ' +
      str(T[u].p) + ', depth = ' + str(D[u]) + ', ')
    if T[u].p == NIL:
        p('root, ')
    elif T[u].l == NIL:
        p('leaf, ')
    else:
        p('internal node, ')

    p('[')
    c = T[u].l
    i = 0
    while c != NIL:
        if i:
            p(', ')
        p(str(c))
        c = T[c].r
        i += 1
    p(']\n')


def getDepth(u):
    d = 0
    while T[u].p != NIL:
        u = T[u].p
        d += 1
    return d


def main():
    global T, D
    n = input()
    for i in xrange(n):
        T[i] = Node()

    for i in xrange(n):
        t = map(int, raw_input().split())
        id, k = t[0], t[1]
        l = 0
        for j in xrange(2, k + 2):
            c = t[j]
            if j == 2:
                T[id].l = c
            else:
                T[l].r = c
            l = c
            T[c].p = id

    for i in xrange(n):
        D[i] = getDepth(i)

    for i in xrange(n):
        printC(i)

if __name__ == '__main__':
    main()
