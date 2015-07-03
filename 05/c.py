from math import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def koch(n, a, b):
    if n == 0:
        return
    th = pi * 60 / 180

    x = (2.0 * a.x + 1.0 * b.x) / 3
    y = (2.0 * a.y + 1.0 * b.y) / 3
    s = Point(x, y)
    x = (1.0 * a.x + 2.0 * b.x) / 3
    y = (1.0 * a.y + 2.0 * b.y) / 3
    t = Point(x, y)
    x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
    y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y
    u = Point(x, y)
    koch(n - 1, a, s)
    print s.x, s.y
    koch(n - 1, s, u)
    print u.x, u.y
    koch(n - 1, u, t)
    print t.x, t.y
    koch(n - 1, t, b)


def main():
    n = input()
    a = Point(0, 0)
    b = Point(100, 0)

    print a.x, a.y
    koch(n, a, b)
    print b.x, b.y

if __name__ == '__main__':
    main()
