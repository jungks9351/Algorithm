# 중복 문자 없는 가장 긴 부분 문자열

# 중복 문자가 없는 가장 긴 부분 문자열의 길이을 리턴하라

# "abcabcbb"
# 3

# "bbbbb"
# 1

# "pwwkew"

# 3

def solve(s:str) ->int:
    used= {}
    maxLength = start = 0

    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 start 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            maxLength = max(maxLength, index -start +1)

        # 현재 문자의 위치 삽입

        used[char] = index
    return maxLength

if __name__ == "__main__":
    s1= "abcabcbb"
    s2 = "bbbbbb"
    s3 = "pwwkew"
    print(solve(s1))
    print(solve(s2))
    print(solve(s3))