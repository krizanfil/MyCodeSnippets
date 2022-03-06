from typing import List


def findMin(nums: List[int]) -> int:
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return nums[-1]

    left, right = 0, len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] < nums[middle - 1]:
            return nums[middle]
        if nums[middle] < nums[right]:
            right = middle - 1
        else:
            left = middle + 1

    return nums[left]
