VMAX = 10000


def countingSort(A, B):
    C = [0] * (VMAX + 1)

    for j in range(1, n + 1):
        C[A[j]] += 1

    for i in range(1, VMAX + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(1, n + 1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1


def main():
    global n
    n = input()
    A = [0] + map(int, raw_input().split())
    B = [0] * (n + 1)
    countingSort(A, B)
    print ' '.join(map(str, B[1:]))

if __name__ == '__main__':
    main()
