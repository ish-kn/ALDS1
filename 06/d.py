VMAX = 10000

n = s = 0
A = []


def solve():
    ans = 0

    B = list(A)
    V = [False for i in xrange(n)]
    B.sort()
    T = [0] * (VMAX + 1)
    for i in xrange(n):
        T[B[i]] = i
    for i in xrange(n):
        if V[i]:
            continue
        cur = i
        S = 0
        m = VMAX
        an = 0
        while 1:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]:
                break
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)

    return ans


def main():
    global n, A, s
    n = input()
    A = map(int, raw_input().split())
    s = min(A)
    print solve()

if __name__ == '__main__':
    main()
