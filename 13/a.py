# -*- coding: utf-8 -*-

import sys
p = sys.stdout.write

N = 8
FREE = -1
NOT_FREE = 1

row = [FREE] * N
col = [FREE] * N
dpos = [FREE] * (2 * N - 1)
dneg = [FREE] * (2 * N - 1)
X = [[False for j in xrange(N)] for i in xrange(N)]


def printBoard():
    for i in xrange(N):
        for j in xrange(N):
            if X[i][j]:
                if row[i] != j:
                    return
    for i in xrange(N):
        for j in xrange(N):
            p('Q' if row[i] == j else '.')
        print


def recursive(i):
    if i == N:  # クイーンの配置に成功
        printBoard()
        return

    for j in xrange(N):
        # (i, j) が他のクイーンに襲撃されている場合は無視
        if NOT_FREE == col[j] \
                or NOT_FREE == dpos[i + j] \
                or NOT_FREE == dneg[i - j + N - 1]:
            continue
        # (i, j) にクイーンを配置する
        row[i] = j
        col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE
        # 次の行を試す
        recursive(i + 1)
        # (i, j) に配置されているクイーンを取り除く
        row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE
    # クイーンの配置に失敗


def main():
    k = input()
    for i in xrange(k):
        r, c = map(int, raw_input().split())
        X[r][c] = True

    recursive(0)

if __name__ == '__main__':
    main()
