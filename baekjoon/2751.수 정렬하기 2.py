import sys

sys.stdin = open('input.text')

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()
for x in arr:
    print(x)