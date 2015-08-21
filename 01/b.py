def gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        r = x % y
        x = y
        y = r

    return x


def main():
    x, y = map(int, raw_input().split())
    print gcd(x, y)

if __name__ == '__main__':
    main()
