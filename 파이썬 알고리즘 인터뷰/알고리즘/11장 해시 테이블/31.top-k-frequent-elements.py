# 상위 K 빈도 요소

# 상위 k번 이상 등장하는 요소를 추출하라

# nums = [1,1,1,2,2,3], k =2
# [1,2]
import collections
import heapq


def solve(nums, k):
    counter = collections.Counter(nums)

    answer = []
    for i, num in enumerate(counter):
        # print(nums[i+1])
        if counter[i+1] >= k:
            # print(nums[i+1], num)
            answer.append(num)

    return answer

# Counter를 이용한 음수 순 추출

def solve2(nums,k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

    return topk

# 파이썬 다운 방식

def solve3(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]




if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solve(nums,k))
    print(solve2(nums, k))
    print(solve3(nums, k))