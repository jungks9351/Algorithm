import sys
from typing import List

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# 메모제이션
def maxSubArray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)


print(maxSubArray(nums))

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# 카데인 알고리즘
def maxSubArray2(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)

print(maxSubArray2(nums))