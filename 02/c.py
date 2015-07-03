def bubbleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if C[j][1] < C[j - 1][1]:
                C[j], C[j - 1] = C[j - 1], C[j]


def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]


def isStable(C, D, N):
    for i in range(N):
        if C[i][0] != D[i][0]:
            return 'Not stable'
    return 'Stable'


def main():
    N = input()
    C = raw_input().split()
    D = list(C)

    bubbleSort(C, N)
    print ' '.join(C)
    print 'Stable'
    selectionSort(D, N)
    print ' '.join(D)
    print isStable(C, D, N)

if __name__ == '__main__':
    main()
