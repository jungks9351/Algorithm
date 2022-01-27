import sys

sys.stdin = open('input.text')


def DFS(x, sum):
    global res

    if sum > m or x>res:
        return

    if sum == m:
        if x < res:
            res = x

    else:
        for i in range(n):
            DFS(x + 1, sum + a[i])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)
