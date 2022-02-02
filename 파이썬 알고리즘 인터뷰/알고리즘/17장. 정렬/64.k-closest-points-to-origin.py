import heapq

points = [[3, 3], [5, -1], [-2, 4]]

k = 2

arr = []

while points:
    pop = points.pop(0)
    distance = pop[0] ** 2 + pop[1] ** 2
    arr.append((pop, distance))

arr.sort(key=lambda x: x[1])

result = []

for i in range(k):
    result.append(arr[i][0])

print(result)

# heap = []
# for (x, y) in points:
#     dist = x ** 2 + y ** 2
#     heapq.heappush(heap, (dist, x, y))

# result = []
# for _ in range(k):
#     (dist, x, y) = heapq.heappop(heap)
#     result.append((x, y))
# print(result)
