# 백준 9012 괄호 문제
# 입력
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(
# 출력
# NO
# NO
# YES
# NO
# YES
# NO

# 일력
# 3
# ((
# ))
# ())(()
# 출력
# NO
# NO
# NO

# input() 함수로 사용자가 어떤 값을 입력하게 하고
# 그 값을 변수에 저장할 수 있습니다.



def solve(PS):
    # PS = input()
    stack = []
    # strs = input()
    # ( 일 때 push 하고
    # )일 땐 stack ( 가 없으면 실패
    # () 쌍을 이루면 pop

    for s in PS:
        # print(str)
        # ( 일 때 push 하고
        if s == '(':
            stack.append(s)
        # )일 땐 stack 마지막이 ( 이면 pop
        else:
            if len(stack) == 0:
                print("NO")
                return
            else:
                stack.pop()
    if len(stack) == 0:
        # return "YES"
        return print("YES")
    else:
        # return "NO"
        return print("NO")

num = int(input())

for i in range(num):
    solve()

# 백준 정답
# num = int(input())
#
# for i in range(num):
#     strs = input()
#     stack = []
#
#     for str in strs:
#         if str == '(':
#             stack.append(str)
#         elif str == ')' and stack[-1] == '(':
#             stack.pop()
#         else:
#             stack.append(')')
#
# if len(stack) == 0:
#     print("YES")
# else:
#     print("NO")

if __name__ == "__main__":
    # (, (, ), ) index[j]-index[i] % 2 ==1
    str ="(())())"
    str2 = "(()())((()))"
    str3 = "()()()()(()()())()"
    str4 = "())(()"
    VPS(str)  # NO
    VPS(str2) # YES
    VPS(str3) # YES
    VPS(str4) # NO
