# 두 수의 합

# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
from typing import List

nums = [2,7,11,15]
target =9

# 브루트 포스로 계산
# 시간 복잡도가 O(n^2) 문제는 풀리지만 브루트 포스 방식은 지나치게 느리다.
# 좀 더 최적화 하는 방법을 찾아야 한다

def solve(nums:List[int], target) -> List[List[int]]:
    # result =[]
    for i in range(len(nums)):
        # print(i)
        for j in range(i+1, len(nums)):
            # print(j)
            if nums[i]+nums[j] == target:
                # result.append([i,j])
                return [i,j]

    # return result

print(solve(nums, target))
# in 을 이용한 탐색
# target 에서 n을 뺀 값이 존재하는 지 여부를 탐색할 수 있다.

def solve2(nums:List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        # print(i, n)
        complement = target - n

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]


print(solve2(nums, target))

# 첫번째 수를 뺀 결과 키 조회

def solve3(nums:List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return [i, nums_map[target-num]]


print(solve3(nums, target))


# 조회 구조 개선
# 딕셔너리와 조회를 2개의 for 문으로 각각 처리했던 방식을 좀 더 개선해 보자
def solve4(nums:List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for문으로 통합

    for i, num in enumerate(nums):
        nums_map[num] = i
        if target-num in nums_map:
            return [nums_map[target-num], i]


print(solve4(nums,target))

# 투 포인터 이용

# 투 포인터란 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로
# 옮기면서 값을 조정하는 방식이다.

def solve5(nums:List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) -1

    while not left == right:
        if nums[left] + nums[right] < target:
            left +=1
        elif nums[left] + nums[right] > target:
            right -=1
        else:
            return [left,right]

print(solve5(nums,target))

# 그러나 이 문제는 투포인터로 풀 수 없다. 입력값인 nums는 정렬된 상태가 아니기 때문이다.
# 제대로 풀려면 sort하여 정렬이 필요하다.
# 하지만 정렬을 하면 값을 찾는 문제이면 문제가 없겠지만, 인덱스를 찾아내는 문제에서는
# 인덱스가 섞어 버리기 때문에 풀 수가 없다.
