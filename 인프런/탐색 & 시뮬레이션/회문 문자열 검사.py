# 회문 문자열 검사

# n = int(input())
n = 5

for i in range(n):
    s = input()
    s = s.lower()
    size = len(s)

    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' % (i + 1))

for i in range(n):
    s = input()
    s = s.lower()

    if s == s[::-1]:
        print('#%d YES' % (i + 1))

    else:
        print('#%d NO' %(i + 1))



