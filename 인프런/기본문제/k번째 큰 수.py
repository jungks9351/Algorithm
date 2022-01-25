
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

n, k = 10, 3
a = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]

res = set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res = list(res)
res.sort(reverse=True)

print(res[k-1])