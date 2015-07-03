def bubbleSort(A, N):
    flg = 1
    cnt = 0
    i = 0
    while flg:
        flg = 0
        for j in range(N - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                cnt += 1
                flg = 1
        i += 1
    return cnt


def main():
    N = input()
    A = map(int, raw_input().split())

    cnt = bubbleSort(A, N)

    print " ".join(map(str, A))
    print cnt

if __name__ == '__main__':
    main()
