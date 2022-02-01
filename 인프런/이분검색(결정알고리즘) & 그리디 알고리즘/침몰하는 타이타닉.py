import sys
from collections import deque

sys.stdin = open('input.text')

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

arr = deque(arr)

cnt = 0

while arr:
    if len(arr) == 1:
        break

    if arr[0] + arr[-1] > m:
        arr.pop()
        cnt += 1
    else:
        arr.popleft()
        arr.pop()
        cnt += 1

print(cnt)

## 다른 사람 풀이

a, b = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
cnt = 0
lt = 0
rt = a - 1

while (lt <= rt):
    if num[lt] + num[rt] <= b:
        cnt += 1
        lt += 1
        rt -= 1
    elif num[lt] + num[rt] > b:
        cnt += 1
        rt -= 1

print(cnt)
