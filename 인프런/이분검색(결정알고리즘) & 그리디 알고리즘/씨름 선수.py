import sys

sys.stdin = open('input.text')

n = int(input())

# 키가 크거나 무게가 더 나가는 지원자
# A 의 키와 무게 모두 더 높은 지원자가 있으면 탈락
players = []

for i in range(n):
    height, weight = map(int, input().split())

    players.append((height, weight))

players.sort(reverse=True)

print(players)
tmp = 0
cnt = 0
for h, w in players:
    print(h,w)
    if w >= tmp:
        tmp = w
        cnt +=1

print(cnt)



