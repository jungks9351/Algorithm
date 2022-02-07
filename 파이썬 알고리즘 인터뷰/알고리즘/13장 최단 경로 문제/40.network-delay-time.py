import heapq
import collections
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # print(graph)
    q = []
    dist = collections.defaultdict(int)

    heapq.heappush(q, (0, k))

    # print(dist)

    while q:
        acc, cur = heapq.heappop(q)
        # print(acc,cur)

        if cur not in dist:
            dist[cur] = acc

            for adj, d in graph[cur]:
                cost = acc + d
                heapq.heappush(q, (cost, adj))

    if len(dist) == n:
        return max(dist.values())
    return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

print(networkDelayTime(times, n, k))
