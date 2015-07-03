def main():
    d = {}
    n = input()
    for i in xrange(n):
        com, s = raw_input().split()
        if com[0] == 'i':
            d[s] = d.get(s, True)
        else:
            if d.get(s):
                print 'yes'
            else:
                print 'no'

if __name__ == '__main__':
    main()
