import sys

sys.stdin = open('input.text')


def DFS(x, sum, tsum):
    global result

    if sum+(total-tsum) < result:
        return

    if sum > c:
        return
    if x == n:
        if sum > result:
            result = sum
    else:
        DFS(x+1, sum+a[x], tsum+a[x])
        DFS(x+1, sum, tsum+a[x])


if __name__ == '__main__':
    c, n = map(int, input().split())

    a = [0] * n

    result = -2147000000
    for i in range(5):
        a[i] = int(input())

    total = sum(a)

    DFS(0, 0,0)
    print(result)
