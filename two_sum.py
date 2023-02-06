from typing import List

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(self, nums: List[int], target: int) -> List[int]:
    """My solution, 2nd in memory usage"""
    for i, n in enumerate(nums):
        if target - n in nums and i != nums.index(target - n):
            return [i, nums.index(target - n)]


def two_sum_runtime(self, nums: List[int], target: int) -> List[int]:
    """Best runtime and memory solution"""
    seen = {}

    for idx, num in enumerate(nums):
        remainder = target - num
        if remainder in seen:
            return [seen[remainder], idx]
        else:
            seen[num] = idx
