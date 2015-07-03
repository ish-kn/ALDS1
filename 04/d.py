MAX = 100000
T = [None] * MAX
n = k = 0


def check(P):
    i = 0
    for j in xrange(k):
        s = 0
        while (s + T[i]) <= P:
            s += T[i]
            i += 1
            if i == n:
                return n
    return i


def solve():
    left = 0
    right = MAX * 10000
    while (right - left) > 1:
        mid = (left + right) / 2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right


def main():
    global n, k, T
    n, k = map(int, raw_input().split())
    for i in xrange(n):
        T[i] = input()
    print solve()

if __name__ == '__main__':
    main()
