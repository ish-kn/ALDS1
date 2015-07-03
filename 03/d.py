import sys
p = sys.stdout.write


def main():
    s = raw_input()
    s1 = []
    s2 = []
    sum = 0
    for i in xrange(len(s)):
        if s[i] == '\\':
            s1.append(i)
        elif s[i] == '/' and len(s1) > 0:
            j = s1.pop()
            sum += i - j
            a = i - j
            while len(s2) > 0 and s2[len(s2) - 1][0] > j:
                a += s2.pop()[1]
            s2.append([j, a])

    print sum
    p(str(len(s2)))
    for i in xrange(len(s2)):
        p(' ' + str(s2[i][1]))
    print ''

if __name__ == '__main__':
    main()
