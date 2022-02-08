import collections
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())
# print(V,E,K)

INF = int(1e9)
# 2차원 리스트 생성 무한 초기화
dist = [[INF] * (V + 1) for _ in range(V + 1)]

# 자신의 경로 비용 0 초기화
for i in range(1, V + 1):
    dist[i][i] = 0

# 간선의 비용으로 초기화
for i in range(E):
    u, v, w = map(int, input().split())
    if w < dist[u][v]:
        dist[u][v] = w

# print(dist)

# 플로이드 워셀 알고리즘 수행
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# print(dist)

for i in range(1, V+1):
    if dist[K][i] == INF:
        print('INF')
    else:
        print(dist[K][i])
