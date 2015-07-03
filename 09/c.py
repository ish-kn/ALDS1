from heapq import *


def main():
    q = []
    while 1:
        com = raw_input()
        if com[0] == 'i':
            com, k = com.split()
            heappush(q, int(k))
        elif com[1] == 'x':
            print nlargest(1, q)[0]
            q = sorted(q)
            q.pop()
            heapify(q)
        else:
            break

if __name__ == '__main__':
    main()
