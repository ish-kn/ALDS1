H = 0
A = []


def maxHeapify(i):
    l = 2 * i
    r = 2 * i + 1

    largest = 0
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(largest)


def buildMaxHeap():
    for i in xrange(H / 2, 0, -1):
        maxHeapify(i)


def main():
    global A, H
    H = input()
    A = [0] + map(int, raw_input().split())

    buildMaxHeap()
    print ' ' + ' '.join(map(str, A[1:]))

if __name__ == '__main__':
    main()
