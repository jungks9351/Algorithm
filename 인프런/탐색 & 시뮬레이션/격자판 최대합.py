n = 5

arr = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19],
]

# n = int(input())
# arr = list(list(map(int, input().split())) for _ in range(n))

# for x in arr:
#     print(x)

largest = 0

for i in range(n):
    # sum1 행의 합 sum2 열의 합 sum3 대각 선 합
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# sum3 왼쪽부터 대각선 합 sum4 오른쪽에서 대각선 합
sum3 = sum4 = 0
for i in range(n):
    sum3 += arr[i][i]
    sum4 += arr[i][n - i - 1]
if sum3 > largest:
    largest = sum3
if sum4 > largest:
    largest = sum4

print(largest)
