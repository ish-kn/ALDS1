import sys

p = sys.stdout.write


class Node:

    def __init__(self, k, l, r, p):
        self.key = k
        self.left = l
        self.right = r
        self.parent = p

NIL = Node(None, None, None, None)
root = NIL


def insert(k):
    global root
    y = NIL
    x = root
    z = Node(k, NIL, NIL, NIL)

    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y

    if y == NIL:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def preParse(u):
    if u == NIL:
        return
    p(' ' + str(u.key))
    preParse(u.left)
    preParse(u.right)


def inParse(u):
    if u == NIL:
        return
    inParse(u.left)
    p(' ' + str(u.key))
    inParse(u.right)


def printKey():
    inParse(root)
    print ''
    preParse(root)
    print ''


def main():
    n = input()
    for i in xrange(n):
        com = raw_input()
        if com[0] == 'i':
            t, k = com.split()
            insert(int(k))
        else:
            printKey()

if __name__ == '__main__':
    main()
