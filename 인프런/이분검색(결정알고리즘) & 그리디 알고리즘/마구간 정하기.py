import sys

sys.stdin = open('input.text')

n, c = map(int, input().split())

a = [int(input()) for _ in range(n)]

a.sort()

lt = 0
rt = a[n - 1]


def count(len):
    cnt = 1
    ep = a[0]
    for i in range(1, n):
        if a[i] - ep >= len:
            cnt += 1
            ep = a[i]
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
