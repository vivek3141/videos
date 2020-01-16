#include <iostream>

using namespace std;

const int n = 100;
int dp[n + 1] = {0};

int fib(int n)
{
    if (n == 1)
    {
        return 1;
    }
    if (dp[n] != 0)
    {
        return dp[n];
    }
    else
    {
        dp[n] = fib(n - 1) + fib(n - 2);
        return dp[n];
    }
}

int main()
{    cout << fib(n) << '\n';
}