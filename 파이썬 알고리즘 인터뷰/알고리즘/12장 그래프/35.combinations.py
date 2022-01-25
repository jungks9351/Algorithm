# 조합

# 전체 수 n을 입력 받아 k개의 조합을 리턴하라
import itertools
from typing import List

n =4
k =2

# DFS k개 조합 생성

def solve(n:int,k:int)-> List[List[int]]:
    result = []

    def dfs(elements, start: int, k:int):
        if k == 0:
            result.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출

        for i in range(start, n +1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
    dfs([],1,k)
    return result

print(solve(n,k))

# itertools 모듈 사용

def solve2(n:int,k:int)-> List[List[int]]:
    return list(map(list,itertools.combinations(range(1,n+1), k)))

print(solve2(n,k))