class P:

    def __init__(self, n, t):
        self.name = n
        self.time = t


def main():
    n, q = map(int, raw_input().split())
    p = [None] * n
    for i in xrange(n):
        name, time = raw_input().split()
        p[i] = P(name, int(time))

    ans = []
    t = 0
    while len(p):
        tmp = p.pop(0)
        if tmp.time <= q:
            t += tmp.time
            ans.append(P(tmp.name, t))
        else:
            t += q
            tmp.time -= q
            p.append(tmp)

    for x in ans:
        print x.name, x.time

if __name__ == '__main__':
    main()
