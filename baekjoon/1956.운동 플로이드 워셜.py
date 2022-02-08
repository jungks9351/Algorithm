import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())

INF = int(1e9)
dist = [[INF] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    if w < dist[u][v]:
        dist[u][v] = w

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

minimum = INF

for i in range(1, V + 1):
    minimum = min(minimum, dist[i][i])

if minimum == INF:
    print(-1)
else:
    print(minimum)
