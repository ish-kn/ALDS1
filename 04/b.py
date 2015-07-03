def binarySearch(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) / 2
        if A[mid] == key:
            return True
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return False


def main():
    n = input()
    S = map(int, raw_input().split())
    q = input()
    T = map(int, raw_input().split())

    c = 0
    for t in T:
        if binarySearch(S, t):
            c += 1
    print c

if __name__ == '__main__':
    main()
