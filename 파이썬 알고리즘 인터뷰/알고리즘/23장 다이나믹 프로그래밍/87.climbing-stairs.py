import collections

n = 3


# 재귀구조 브루트포스
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n - 1) + climbStairs(n - 2)


print(climbStairs(n))

# 메모이제이션


n = 3
dp = collections.defaultdict(int)


def climbStairs2(n: int) -> int:
    if n <= 2:
        return n

    if dp[n]:
        return dp[n]
    dp[n] = climbStairs2(n - 1) + climbStairs2(n - 2)
    return dp[n]

print(climbStairs2(n))