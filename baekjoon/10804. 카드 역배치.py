
arr = list(range(21))

for _ in range(10):
    # s, e = map(int, input().split())

    for i in range((e-s+1)//2):
        arr[s+i], arr[e-i] = arr[e-i], arr[s+i]
arr.pop(0)

for x in arr:
    print(x, end=' ')


