# 그룹 애너그램

# 문자열 배열을 받아 애너그램 단위로 그룹핑하라
import collections
from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# 정렬하여 딕셔너리에 추가

def solve(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        print(''.join(sorted(word)))
        print(anagrams)
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


print(solve(strs))