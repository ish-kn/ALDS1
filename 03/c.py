def main():
    n = input()
    a = []
    for i in xrange(n):
        com = raw_input()
        if com[0] == 'i':
            com, d = com.split()
            a.append(d)
        elif com[len(com) - 3] == 'e':
            com, d = com.split()
            for i in xrange(len(a) - 1, -1, -1):
                if a[i] == d:
                    a.pop(i)
                    break
        elif com[6] == 'F':
            a.pop()
        elif com[6] == 'L':
            a.pop(0)

    print ' '.join(reversed(a))

if __name__ == '__main__':
    main()
