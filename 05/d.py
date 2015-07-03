INF = float('inf')


def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left + i] for i in xrange(n1)] + [INF]
    R = [A[mid + i] for i in xrange(n2)] + [INF]
    i = j = cnt = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            cnt += n1 - i
    return cnt


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) / 2
        v1 = mergeSort(A, left, mid)
        v2 = mergeSort(A, mid, right)
        v3 = merge(A, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0


def main():
    n = input()
    A = map(int, raw_input().split())
    print mergeSort(A, 0, n)

if __name__ == '__main__':
    main()
