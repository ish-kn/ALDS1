def main():
    n = input()
    S = raw_input().split()
    q = input()
    T = raw_input().split()
    c = 0
    for t in T:
        if t in S:
            c += 1
    print c

if __name__ == '__main__':
    main()
