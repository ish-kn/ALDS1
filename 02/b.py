def selectionSort(A, N):
    cnt = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
        if i != minj:
            cnt += 1
    return cnt


def main():
    N = input()
    A = map(int, raw_input().split())

    cnt = selectionSort(A, N)

    print " ".join(map(str, A))
    print cnt

if __name__ == '__main__':
    main()
