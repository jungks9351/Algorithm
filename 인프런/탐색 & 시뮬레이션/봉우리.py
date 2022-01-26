# 봉우리

n = 5

arr = [
    [5, 3, 7, 2, 3],
    [3, 7, 1, 6, 1],
    [7, 2, 5, 3, 4],
    [4, 3, 6, 4, 1],
    [8, 7, 3, 5, 2]
]

# n = int(input())
# arr = list(list(map(int, input().split())) for _ in range(n))


arr.insert(0, [0] * n)
arr.append([0] * n)
for x in arr:
    x.insert(0, 0)
    x.append(0)

# for x in arr:
#     print(x)

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(arr[i][j] > arr[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
