# 전화 번호 문자 조합

# 2 에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라


# 2는 abc, 3은 def가 가능하므로 각각 한 문자씩 9개의 문자로 조합가능하다.


# 모든 조합 탐색
from typing import List

digits = "23"


def solve(digits:str) -> List[str]:

    graph = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def dfs(index,path):
        # 끝까지 탐색하면 백트래킹

        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in graph[digits[i]]:
                print(j)
                dfs(i+1, path +j)

        if (len(path) == len(digits)):
            result.append(path)
            return


    if not digits:
        return []



    result = []


    dfs(0, "")

    return result

print(solve(digits))