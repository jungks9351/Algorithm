import sys

from collections import deque

sys.stdin = open('input.text')

n, m = map(int, input().split())

q = [(pos, val) for pos, val in enumerate(list((map(int, input().split()))))]

q = deque(q)

cnt = 0

while q:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q):
        q.append(cur)
    else:
        cnt += 1
        if cur[0] ==m:
            break

print(cnt)
