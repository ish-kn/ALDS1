from copy import *


class bar:

    def __init__(self, id, name):
        self.id = id
        self.name = name


def main():
    a = bar(0, 'k')
    b = copy(a)
    b.id = 1
    print a.id

if __name__ == '__main__':
    main()
