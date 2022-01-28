import sys
import heapq

sys.stdin = open('input.text')


n = int(sys.stdin.readline())
heap = list()

for x in range(n):
    x = int(sys.stdin.readline())

    if x < 0:
        heapq.heappush(heap, (-x,x))
    elif x > 0:
        heapq.heappush(heap, (x,x))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

