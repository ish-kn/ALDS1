def fib(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in xrange(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def main():
    n = input()
    print fib(n)

if __name__ == '__main__':
    main()
