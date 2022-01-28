import sys

sys.stdin = open('input.txt')

n,m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

len = len(a)
lt = 0
rt = len -1


while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] ==m:
        print(mid+1)
        break

    elif a[mid] > m:
        rt = mid -1
    else:
        lt = mid + 1




