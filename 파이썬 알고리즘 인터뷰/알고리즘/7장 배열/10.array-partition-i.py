# 배열 파티션 I

# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰수를 출력하라.
from typing import List

nums = [1,4,3,2]

# 오름차순 풀이

def solve1(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair =[]

    return sum

print(solve1(nums))

# 짝수 번째 값 계산

def solve2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum +=n

    return sum

print(solve2(nums))

# 파이썬다운 방식

def solve3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

print(solve3(nums))
