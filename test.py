num = 100
dp = [-1 for i in range(num + 1)]


def fib(n):
    if n < 2: return n
    if dp[n] != -1: return dp[n]
    else:
        dp[n] = fib(n-1) + fib(n-2)
        return dp[n]


print(fib(num))
