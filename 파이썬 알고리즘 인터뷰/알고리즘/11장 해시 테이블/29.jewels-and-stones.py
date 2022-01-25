# 보석 과 돌

# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇개나 있을까? 대소문자는 구분한다.

# J = "aA", S="aAAbbbb"

# 3

# 해시 테이블을 이용한 풀이
import collections


def solve(J:str, S:str) -> int:
    hash = {}

    count = 0

    # 돌(S)의 빈도 수 계산
    for char in S:
        if char not in hash:
            hash[char] = 1
        else:
            hash[char] += 1

    # 보석(J)의 빈도 수 합산
    for char in J:
        if char in hash:
            count+= hash[char]

    return count

# defaultdict를 이용한 비교 생략
def solve2(J:str, S:str) -> int:
    hash = collections.defaultdict(int)

    count = 0

    # 돌(S)의 빈도 수 계산
    for char in S:
        hash[char] += 1

    # 보석(J)의 빈도 수 합산
    for char in J:
        count+= hash[char]

    return count

# counter로 계산 생략
def solve3(J:str,S:str) ->int:
    hash = collections.Counter(S)
    count = 0
    for char in J:
        count += hash[char]

    return count

# 파이썬 다운 방식
def solve4(J:str, S:str) -> int:
    return sum(s in J for s in S)

if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(solve(J,S))
    print(solve2(J, S))
    print(solve3(J, S))
    print(solve4(J, S))




