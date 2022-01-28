# 배열의 k번째 큰 요소

"""
최대 힙 삽입

                3
        2               3
    1       2       4
-------------------------------------------------
                4
        2               3
    1       2       3       5
-------------------------------------------------
                5
        2               4
    1       2       3       3
-------------------------------------------------
                5
        5               4
    2       2       3       3
1
-------------------------------------------------
최대힙 삽입 완성 및 추출 시작
                6
        5               4

    5       2       3       3

1       2
-------------------------------------------------
                5
        5               3

    4       2       3       2

1
-------------------------------------------------
                5
        4               3

    3       2       2       1
-------------------------------------------------
                4
        3               1

    2       2
-------------------------------------------------
                3
        2

    2       1
-------------------------------------------------

"""

# heaq 모듈 이용
from typing import List

import heapq


def solve(self, nums: List[int], k: int) -> int:
    # heap = []
    heap = list()

    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(1,k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)

# nlargest 이용
def solve2(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

# 정렬

def solve3(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]

# heapify 이용
def solve4(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums)-k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

