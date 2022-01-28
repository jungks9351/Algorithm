# 순열

# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라
import itertools
from typing import List

nums = [1,2,3]

# DFS를 활용한 순열 생성
def solve(nums: List[int])-> List[List[int]]:
    result = []

    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if (len(elements) == 0):
            result.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            # print(prev_elements[:])
            next_elements = elements[:]
            next_elements.remove(e)
            # print(next_elements)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result

print(solve(nums))

# itertools 모듈 사용

def solve2(nums:List[int]) -> List[List[int]]:
    return list(map(list,itertools.permutations(nums)))

print(solve2(nums))



