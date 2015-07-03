N = 1000


def lcs(X, Y):
    c = [[0 for j in xrange(N + 1)] for i in xrange(N + 1)]
    m = len(X)
    n = len(Y)
    maxl = 0
    X = ' ' + X
    Y = ' ' + Y

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
            maxl = max(maxl, c[i][j])
    return maxl


def main():
    n = input()
    for i in xrange(n):
        X = raw_input()
        Y = raw_input()
        print lcs(X, Y)

if __name__ == '__main__':
    main()
