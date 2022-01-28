import sys

sys.stdin = open('input.text')

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

targets = list(map(int, sys.stdin.readline().split()))

a.sort()

for target in targets:
    lt = 0
    rt = m - 1

    while lt <= rt:

        mid = (lt + rt) // 2

        if a[mid] == target:
            print(1)
            break

        elif a[mid] > target:
            rt = mid - 1

        elif a[mid] < target:
            lt = mid + 1

    if lt > rt:
        print(0)
