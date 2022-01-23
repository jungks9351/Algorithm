# 자신을 제외한 배열의 곱

# 배열을 입력받아 ouput[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과를 되도록 출력하라

# 나눗셈을 하지 않고 O(n)으로 풀이하라
from typing import List

nums = [1,2,3,4]

def solve(nums: List[int]) -> List[int]:
    out = []
    p = 1

    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        print(i, p)
        out.append(p)
        p = p * nums[i]

    p = 1

    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

    for i in range(len(nums) -1, 0 -1, -1):
        print(i, p)
        out[i] = out[i] * p
        p = p *nums[i]

    return out

print(solve(nums))
