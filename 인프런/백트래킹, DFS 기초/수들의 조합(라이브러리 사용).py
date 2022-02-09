import sys
import itertools as it

sys.stdin = open('input.txt')

n, k = map(int, input().split())

nums = list(map(int, input().split()))

m = int(input())

cnt = 0

for x in it.combinations(nums, k):
    if sum(x) % m == 0:
        cnt += 1
        
print(cnt)
