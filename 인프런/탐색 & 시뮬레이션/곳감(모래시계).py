# 곳감(모래시계)

# n = 5
#
# arr = [
#     [10, 13, 10, 12, 15],
#     [12, 39, 30, 23, 11],
#     [11, 25, 50, 53, 15],
#     [19, 27, 29, 37, 27],
#     [19, 13, 30, 13, 19],
# ]
# m = 3


# for x in arr:
#     print(x)

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    # h, t, k = 2, 0, 3

    if t == 0:
        for _ in range(k):
            x = arr[h - 1].pop(0)
            arr[h - 1].append(x)

    else:
        for _ in range(k):
            x = arr[h - 1].pop()
            arr[h - 1].insert(0, x)

res = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e + 1):
        res += arr[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
