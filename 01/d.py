def main():
    n = input()
    r0 = input()
    maxv = -10**9
    minv = r0

    for j in range(1, n):
        r = input()
        maxv = max(maxv, r - minv)
        minv = min(minv, r)

    print maxv

if __name__ == '__main__':
    main()
