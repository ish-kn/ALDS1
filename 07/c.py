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


def preParse(u):
    if u == NIL:
        return
    p(' ' + str(u))
    preParse(T[u].left)
    preParse(T[u].right)


def inParse(u):
    if u == NIL:
        return
    inParse(T[u].left)
    p(' ' + str(u))
    inParse(T[u].right)


def postParse(u):
    if u == NIL:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    p(' ' + str(u))


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
            break

    print 'Preorder'
    preParse(root)
    print '\nInorder'
    inParse(root)
    print '\nPostorder'
    postParse(root)
    print ''

if __name__ == '__main__':
    main()
