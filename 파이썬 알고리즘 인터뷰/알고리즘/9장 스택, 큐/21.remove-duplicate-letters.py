# 중복 문자 제거

# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# input "bcabc"
# ouput "abc"

# input "cbacdcbc"
# output "acdb" ? 'abcd'가 왜 아니지..

# 사전식 순서란 사전에서 가장 먼저 찾을 수 있는 순서
# O(n^2) 밖에 생각이 안난다...

# c b a c d c b c => a b b c c c c d d (X)

# def remove_duplicate_letters(str):
#     list = []
#     strs = sorted(str)
#     # print(a)
#
#     for str in strs:
#         # print(str)
#         if str not in list:
#             list.append(str)
#             # print(list)
#     return ''.join(list)


import collections
# 파이썬의 범용 내장 컨테이너 dict, list, set 및 tuple에
# 대한 대안을 제공하는 특수 컨테이너 데이터형을 구현합니다.

def remove_duplicate_letters(s:str):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거

        # print(char)
        # 스택에서 원소를 제거하지 않고 가져오기만 할 때에는
        # [-1]을 이용하도록 한다.
        # top = stack[-1]

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        print(char < stack[-1])

    return ''.join(stack)


if __name__ == "__main__":

    print(remove_duplicate_letters("bcabc"))
    print(remove_duplicate_letters("cbacdcbc"))

