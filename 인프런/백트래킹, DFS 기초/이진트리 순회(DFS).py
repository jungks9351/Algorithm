# 깊이탐색은 왼쪽으로 뻗으면 왼쪽으로 쭉 탐색하고
# 백해서 안간 곳 탐색 반복

# 너비탐색은 레벨로 탐색

# 전위 순회 : 부모 왼쪽 자식 오른쪽 자식 탐색
# 중위 순회 : 왼쪽 자식 부모 오른쪽 자식 탐색
# 후위 순회 : 왼쪽 자식 오른쪽 자식 자식 부모 탐색

import sys

sys.stdin = open('input.text')


# 전위 순회
def dfs(v):
    if v > 7:
        return

    print(v, end=" ")
    dfs(v * 2)
    dfs(v * 2 + 1)


# 중위 순회
def dfs2(v):
    if v > 7:
        return

    dfs2(v * 2)
    print(v, end=" ")
    dfs2(v * 2 + 1)

# 후위 순회
def dfs3(v):
    if v > 7:
        return

    dfs3(v * 2)
    dfs3(v * 2 + 1)
    print(v, end=" ")

if __name__ == '__main__':
    dfs(1)
    print()
    dfs2(1)
    print()
    dfs3(1)
