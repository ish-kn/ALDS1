def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def main():
    n = input()
    A = map(int, raw_input().split())
    q = partition(A, 0, n - 1)
    A = map(str, A)
    A[q] = '[' + A[q] + ']'
    print ' '.join(A)

if __name__ == '__main__':
    main()
