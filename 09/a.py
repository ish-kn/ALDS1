import sys

p = sys.stdout.write


def parent(i):
    return i / 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def main():
    H = input()
    A = [0] + map(int, raw_input().split())

    for i in xrange(1, H + 1):
        p("node " + str(i) + ": ")
        p("key = " + str(A[i]) + ", ")
        if parent(i) >= 1:
            p("parent key = " + str(A[parent(i)]) + ", ")
        if left(i) <= H:
            p("left key = " + str(A[left(i)]) + ", ")
        if right(i) <= H:
            p("right key = " + str(A[right(i)]) + ", ")
        print ""

if __name__ == '__main__':
    main()
