import collections
from typing import List

nums = [1, 2, 3, 1]


# 재귀구조 브루트포스
def rob(nums: List[int]) -> int:
    def _rob(i: int) -> int:
        if i < 0:
            return 0
        return max(_rob(i - 1), _rob(i - 2) + nums[i])

    return _rob(len(nums) - 1)


print(rob(nums))

nums = [2, 7, 9, 3, 1]


# 타뷸레이션

def rob2(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp.popitem()[1]


print(rob2(nums))
