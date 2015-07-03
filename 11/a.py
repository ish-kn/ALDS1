def main():
    n = input()
    for i in xrange(n):
        adj = map(int, raw_input().split())
        m = [0] * (n + 1)
        for j in xrange(adj[1]):
            m[adj[2 + j]] = 1
        print ' '.join(map(str, m[1:]))

if __name__ == '__main__':
    main()
