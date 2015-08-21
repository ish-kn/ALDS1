def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def main():
    cnt = 0
    n = input()
    for i in xrange(n):
        if isPrime(input()):
            cnt += 1

    print cnt

if __name__ == '__main__':
    main()
