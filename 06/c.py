INF = float('inf')


class Card:

    def __init__(self, s, v):
        self.suit = s
        self.value = v


def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left + i] for i in xrange(n1)] + [Card('', INF)]
    R = [A[mid + i] for i in xrange(n2)] + [Card('', INF)]
    i = j = 0
    for k in xrange(left, right):
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) / 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


def partition(A, p, r):
    x = A[r].value
    i = p - 1
    for j in range(p, r):
        if A[j].value <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def main():
    n = input()
    A = [None] * n
    for i in xrange(n):
        s, v = raw_input().split()
        A[i] = Card(s, int(v))
    B = list(A)

    quickSort(A, 0, n - 1)
    mergeSort(B, 0, n)

    if A == B:
        print 'Stable'
    else:
        print 'Not stable'
    for a in A:
        print a.suit, a.value

if __name__ == '__main__':
    main()
