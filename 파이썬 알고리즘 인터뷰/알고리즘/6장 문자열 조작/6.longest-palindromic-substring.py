# 가장 긴 팰린드롬 부분 문자열

# 가장 긴 팰린드롬 부분 문자열을 출력하라

strs1 = "babad"
strs2 = "cbbd"

# "bab"
# "bb"

#
def solve(s:str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    def expnad(left: int, right:int) -> str:
        while left >=0 and right < len(s) and s[left] == s[right]:
            # print(s[left], s[right])
            left -= 1
            right +=1
            # print(left, right)
            # print(s[left + 1:right])
        return s[left + 1:right]

    result =''
    # 0 , 1, 2, 3, 4
    for i in range(len(s)-1):
        result = max(result, expnad(i, i), expnad(i,i+1), key=len)

    return result

solve(strs1)
# print(solve(strs1))

