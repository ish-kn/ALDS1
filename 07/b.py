import sys

p = sys.stdout.write
MAX = 10000
NIL = -1


class Node:

    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL

T = [None] * MAX
D = [0] * MAX
H = [0] * MAX


def setDepth(u, d):
    global D
    if u == NIL:
        return
    D[u] = d
    setDepth(T[u].left, d + 1)
    setDepth(T[u].right, d + 1)


def setHeight(u):
    global H
    h1 = h2 = 0
    if T[u].right != NIL:
        h1 = setHeight(T[u].right) + 1
    if T[u].left != NIL:
        h2 = setHeight(T[u].left) + 1
    H[u] = max(h1, h2)
    return H[u]


def getSibling(u):
    p = T[u].parent
    if p == NIL:
        return NIL
    if T[p].left != u and T[p].left != NIL:
        return T[p].left
    if T[p].right != u and T[p].right != NIL:
        return T[p].right
    return NIL


def printInfo(u):
    p('node ' + str(u) + ': parent = ' +
      str(T[u].parent) + ', sibling = ' + str(getSibling(u)))
    deg = 0
    if T[u].left != NIL:
        deg += 1
    if T[u].right != NIL:
        deg += 1
    p(', degree = ' + str(deg) + ', depth = ' +
      str(D[u]) + ', height = ' + str(H[u]) + ', ')
    if T[u].parent == NIL:
        p('root')
    elif T[u].left == NIL and T[u].right == NIL:
        p('leaf')
    else:
        p('internal node')
    p('\n')


def main():
    global T
    n = input()
    for i in xrange(n):
        T[i] = Node()

    for i in xrange(n):
        id, l, r = map(int, raw_input().split())
        T[id].left = l
        T[id].right = r
        if l != NIL:
            T[l].parent = id
        if r != NIL:
            T[r].parent = id

    root = 0
    for i in xrange(n):
        if T[i].parent == NIL:
            root = i
    setDepth(root, 0)
    setHeight(root)

    for i in xrange(n):
        printInfo(i)

if __name__ == '__main__':
    main()
