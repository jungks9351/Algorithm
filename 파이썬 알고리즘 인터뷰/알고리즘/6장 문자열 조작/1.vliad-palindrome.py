# 유효한 팰린드룸

# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# "A man, a plan, a canal: Panama"
# true

# "race a car"
# false
import collections

import re

# 리스트로 변환 풀이

def useList(s):
    strs = []
    for char  in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

# 데크 자료형을 이용한 최적화
# pop(0) 은 O(n)인 데 반해 데크의 popleft()는 O(1)이다.
# 리스트 쿠현은 O(n^2), 데크 구현은 O(n)으로 성능 차이가 크다.

def useDeque(s: str)-> bool:
    # 자료형 데크로 선언

    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

def useSlicing(s: str) -> bool:
    s = s.lower()
    print(s)
    s = re.sub('[^a-z0-9]', '', s)
    print(s[::-1])
    return s == s[::-1]  # 슬라이싱


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(useList(s))
    print(useDeque(s))
    useSlicing(s)