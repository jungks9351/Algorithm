import sys

sys.stdin = open('input.txt')

n = int(input())

hash = dict()


for i in range(n):
    word = input()
    hash[word] = 1

for i in range(n-1):
    word = input()
    hash[word] = 0

for key, val in hash.items():
    # print(key,val)
    if val == 1:
        print(key)
        break
