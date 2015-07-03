def trace(A):
    print " ".join(map(str, A))


def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        trace(A)


def main():
    N = input()
    A = map(int, raw_input().split())

    trace(A)
    insertionSort(A, N)

if __name__ == '__main__':
    main()
