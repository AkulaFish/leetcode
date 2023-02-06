from typing import List

"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


def shuffle(self, nums: List[int], n: int) -> List[int]:
    array = []
    for i in range(n):
        array.append(nums[i])
        array.append(nums[i + n])
    return array
