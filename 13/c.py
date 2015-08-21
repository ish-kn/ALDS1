# -*- coding: utf-8 -*-

from copy import *

N = 4
N2 = 16
LIMIT = 100

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dir = ['r', 'u', 'l', 'd']
MDT = [[0 for j in xrange(N2)] for i in xrange(N2)]


class Puzzle:

    def __init__(self):
        self.f = [0] * N2
        self.space = 0
        self.MD = 0

state = Puzzle()
limit = 0
path = [0] * LIMIT


def getAllMD(pz):
    sum = 0
    for i in xrange(N2):
        if pz.f[i] == N2:
            continue
        sum += MDT[i][pz.f[i] - 1]
    return sum


def isSolved():
    for i in xrange(N2):
        if state.f[i] != (i + 1):
            return False
    return True


def dfs(depth, prev):
    global state, path
    if state.MD == 0:
        return True
    # 現在の深さにヒューリスティックを足して制限を超えたら枝を刈る
    if depth + state.MD > limit:
        return False

    sx = state.space / N
    sy = state.sapce % N
    tmp = Puzzle()

    for r in xrange(4):
        tx = sx + dx[r]
        ty = sy + dy[r]
        if tx < 0 or ty < 0 or tx >= N or ty >= N:
            continue
        if max(prev, r) - min(prev, r) == 2:
            continue
        tmp = copy(state)
        # マンハッタン距離の差分を計算しつつ、ピースをスワップ
        txy = tx * N + ty
        sxy = sx * N + sy
        state.MD -= MDT[txy][state.f[txy] - 1]
        state.MD += MDT[sxy][state.f[txy] - 1]
        state.f[txy], state.f[sxy] = state.f[sxy], state.f[txy]
        state.space = txy
        if dfs(depth + 1, r):
            path[depth] = r
            return True
        state = copy(tmp)

    return False


def iterative_deepening(pz):
    global state, limit
    pz.MD = getAllMD(pz)  # 初期状態のマンハッタン距離

    limit = pz.MD
    while limit <= LIMIT:
        state = copy(pz)
        if dfs(0, -100) and isSolved():
            ans = ''
            for i in xrange(limit):
                ans += dir[path[i]]
            return ans
        limit += 1

    return 'unsolvable'


def main():
    for i in xrange(N2):
        for j in xrange(N2):
            MDT[i][j] = abs(i / N - j / N) + abs(i % N - j % N)

    pz = Puzzle()

    for i in xrange(N):
        t = map(int, raw_input().split())
        for j in xrange(N):
            k = N * i + j
            pz.f[k] = t[j]
            if pz.f[k] == 0:
                pz.f[k] = N2
                pz.sapce = k
    ans = iterative_deepening(pz)
    print len(ans)
    print ans
    print limit
    print pz.f
    print state.f
    for m in MDT:
        print ' '.join(map(str, m))

if __name__ == '__main__':
    main()
