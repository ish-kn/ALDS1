INF = float('inf')
cnt = 0


def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left + i] for i in xrange(n1)] + [INF]
    R = [A[mid + i] for i in xrange(n2)] + [INF]
    global cnt
    i = j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
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


def main():
    n = input()
    S = map(int, raw_input().split())
    mergeSort(S, 0, n)
    print ' '.join(map(str, S))
    print cnt

if __name__ == '__main__':
    main()
