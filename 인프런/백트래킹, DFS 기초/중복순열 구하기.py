import sys

sys.stdin = open('input.text')



def DFS(x):
    global cnt

    if x == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n + 1):
            res[x] = i
            DFS(x + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
