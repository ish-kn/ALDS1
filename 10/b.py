N = 100
INF = float('inf')
m = [[0 for j in xrange(N + 1)] for i in xrange(N + 1)]
p = [0] * (N + 1)


def solve(n):
    for l in xrange(2, n + 1):
        for i in xrange(1, n - l + 2):
            j = i + l - 1
            m[i][j] = INF
            for k in xrange(i, j):
                m[i][j] = min(
                    m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j])
    return m[1][n]


def main():
    n = input()
    for i in xrange(n):
        p[i], p[i + 1] = map(int, raw_input().split())
    print solve(n)

if __name__ == '__main__':
    main()
