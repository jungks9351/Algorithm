import sys
import bisect
from typing import List


# print(numbers, target)

# lt = 0
# rt = len(numbers)-1
#
# while lt < rt and lt != rt:
#     if numbers[lt] + numbers[rt] < target:
#         lt += 1
#     elif numbers[lt] + numbers[rt] > target:
#         rt -= 1
#     else:
#         print(lt+1, rt+1)



def twoSum(numbers: List[int], target: int) -> List[int]:

    start = 0
    end = len(numbers)
    while start < end:
        index = bisect.bisect(numbers, target - numbers[start], start, end)
        if index <= end and numbers[index - 1] == target - numbers[start]:
            return [start + 1, index]
        else:
            start += 1
            end = index
            continue

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))