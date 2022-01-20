# 문자열 뒤집기


# ["h","e","l","l","o"]
# ['o', 'l', 'l', 'e', 'h']

s = ["h","e","l","l","o"]

# 투 포인터를 이용한 스왑

def solve(s):
    left, right = 0, len(s) -1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    return s
# print(solve(s))

# 파이썬 다운 방식
def solve2(s):
    s.reverse()
    return s

print(solve2(s))

