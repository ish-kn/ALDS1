cnt = 0
G = []


def insertionSort(A, n, g):
    global cnt
    for i in xrange(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v


def shellSort(A, n):
    h = 1
    while 1:
        if h > n:
            break
        G.append(h)
        h = 3 * h + 1

    for i in range(len(G) - 1, -1, -1):
        insertionSort(A, n, G[i])


def main():
    n = input()
    A = [0] * n
    for i in xrange(n):
        A[i] = input()

    shellSort(A, n)

    print len(G)
    print ' '.join(map(str, reversed(G)))
    print cnt
    for a in A:
        print a

if __name__ == '__main__':
    main()
