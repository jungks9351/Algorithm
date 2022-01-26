# 격자판 회문수


board = [
    [2, 4, 1, 5, 3, 2, 6],
    [3, 5, 1, 8, 7, 1, 7],
    [8, 3, 2, 7, 1, 3, 8],
    [6, 1, 2, 3, 2, 1, 1],
    [1, 3, 1, 3, 5, 3, 2],
    [1, 1, 2, 5, 6, 5, 2],
    [1, 2, 2, 2, 2, 1, 5]
]

# board = [list(map(int, input().split())) for _ in range(7)]
# s,e = i, i+4
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)

# 다른 사람 풀이

cnt = 0

for i in range(7):  # 행, 열
    start = 0
    for _ in range(3):

        if board[i][start] == board[i][start + 4] and board[i][start + 1] == board[i][start + 3]:
            cnt += 1
        if board[start][i] == board[start + 4][i] and board[start + 1][i] == board[start + 3][i]:
            cnt += 1

        start += 1
        if start == 3:
            break

print(cnt)