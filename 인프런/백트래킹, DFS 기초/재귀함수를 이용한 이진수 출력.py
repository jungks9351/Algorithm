import sys

sys.stdin = open('input.text')

n = int(input())


def dfs(x):
    if x == 0:
        return
    dfs(x//2)
    print(x % 2, end='')

dfs(n)
