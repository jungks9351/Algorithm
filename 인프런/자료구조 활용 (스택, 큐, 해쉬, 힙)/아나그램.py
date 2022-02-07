import collections
import sys

sys.stdin = open('input.txt')

word1 = input()
word2 = input()

## Counter 함수 사용

word1_cnt = collections.Counter(word1)
word2_cnt = collections.Counter(word2)

if word1_cnt == word2_cnt:
    print("YES")
elif len(word1) != len(word2):
    print("NO")
else:
    print("NO")

## 딕셔러니 해쉬 풀이
str1 = dict()
str2 = dict()

for x in word1:
    str1[x] = str1.get(x, 0) + 1

for y in word2:
    str2[y] = str2.get(y, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

## 개선 코드

hash = dict()

for x in word1:
    hash[x] = hash.get(x, 0) + 1

for y in word2:
    hash[y] = hash.get(y, 0) - 1


for x in word1:
    if hash.get(x) != 0:
        print("NO")
        break
else:
    print("YES")