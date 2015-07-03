from bisect import *


def find(A, x):
    i = bisect_left(A, x)
    if i != len(A) and A[i] == x:
        return True
    else:
        return False


def main():
    n = input()
    S = map(int, raw_input().split())
    q = input()
    T = map(int, raw_input().split())

    c = 0
    for t in T:
        if find(S, t):
            c += 1
    print c

if __name__ == '__main__':
    main()
