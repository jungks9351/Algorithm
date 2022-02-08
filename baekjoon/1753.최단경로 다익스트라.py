import sys
import collections
import heapq

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())

K = 1

INF = int(1e9)
# graph
graph = collections.defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

dist = [INF] * (V + 1)

def dijkstra(graph, start):

    q = []
    # 첫 번째 방문 누적 비용은 0 초기화
    heapq.heappush(q, (0, start))
    dist[start] = 0

    # 큐에 원소가 없을 때 까지 반복
    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)
        # print(acc, cur)
        # 현재의 비용과 비교하여 비용이 더 크면 무시
        if dist[cur] < acc:
            continue

        # 다음 노드를 차례대로 살펴보며 비용을 업데이트할거다.
        for next, d in graph[cur]:
            # 다음 노드까지의 누적 비용
            cost = acc + d
            # 현재 비용보다 작으면 업데이트
            if cost < dist[next]:
                # 비용 업데이트
                dist[next] = cost
                # 다음 노드 까지의 비용을 튜플로 힙에 삽입
                heapq.heappush(q, (cost, next))

# print(dist)

dijkstra(graph, K)

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
