A = []
n = 0
DP = [[None for j in range(2000)] for i in range(200)]


def solve(i, m):
    if m == 0:
        DP[i][m] = True
        return True
    if i >= n:
        DP[i][m] = False
        return False
    if DP[i][m] != None:
        return DP[i][m]
    DP[i][m] = solve(i + 1, m) or solve(i + 1, m - A[i])
    return DP[i][m]


def main():
    global n, A
    n = input()
    A = map(int, raw_input().split())
    q = input()
    M = map(int, raw_input().split())
    for m in M:
        if solve(0, m):
            print 'yes'
        else:
            print 'no'

if __name__ == '__main__':
    main()
