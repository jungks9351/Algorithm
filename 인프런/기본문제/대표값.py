# n = int(input())
# score = list(map(int,input().split()))
import math

n = 10

a = [45,73,66,87,92,67,75,79,75,80]

# round는 round_half_even 방식을 택한다.
ave = round(sum(a)/n + 0.5)

min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1

    elif tmp == min:
        if x > score:
            score= x
            res = idx + 1

print(ave, res)






