import sys

sys.stdin = open('input.text')

L = int(input())

arr = list(map(int, input().split()))

m = int(input())

# arr.sort()
#
# for _ in range(m):
#     arr[0] += 1
#     arr[-1] -= 1
#     arr.sort()
#
# print(arr[-1]-arr[0])

# 리스트를 이용한 해쉬방법

cnt = [0] * 101
maxH = float('-inf')
minH = float('inf')
for x in arr:
    cnt[x] += 1
    if x > maxH: maxH = x
    if x < minH: minH = x

for _ in range(m):
    if cnt[maxH] == 1:
        cnt[maxH] -= 1
        maxH -= 1
        cnt[maxH] += 1
    else:
        cnt[maxH] -= 1
        cnt[maxH - 1] += 1

    if cnt[minH] == 1:
        cnt[minH] -= 1
        minH += 1
        cnt[minH] += 1
    else:
        cnt[minH] -= 1
        cnt[minH + 1] += 1

print(maxH - minH)