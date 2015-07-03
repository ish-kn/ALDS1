pos = 0
pre = []
ind = []
post = []


def rec(l, r):
    global pos
    if l >= r:
        return
    root = pre[pos]
    pos += 1
    m = ind.index(root)
    rec(l, m)
    rec(m + 1, r)
    post.append(root)


def main():
    global pre, ind
    n = input()
    pre = map(int, raw_input().split())
    ind = map(int, raw_input().split())

    rec(0, n)
    print ' '.join(map(str, post))

if __name__ == '__main__':
    main()
