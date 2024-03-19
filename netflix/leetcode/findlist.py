# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

"""
Given:
- Array of ints in ascending order
- We may have repated ints; we need to find the starting and ending range of the indices
- If we don't find them, return -1,-1; if its empty also return -1,-1

Naive Approach:
- Iterate through array; once we find the number, store the starting index
and keep iterating until we hit the ending number (start, end) 
    - If the array is N this will be a O(N) approach. We need
    to iterate over all the array.

FasterApproach:
- Use binary search to find the target IDX, then look left and right until we 
find the remaining values. This will split the array in half each look-up
achieving O(logN)
"""

from typing import List


def binary_search(lst: List[int], target: int, low: int = 0, high=None) -> int:
    if high is None:
        high = len(lst) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    mid_val = lst[mid]

    if mid_val > target:  # take left side (e.g target (2) < 4)
        return binary_search(lst, target, low, mid - 1)
    elif mid_val < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return mid


def searchRange(nums: List[int], target: int) -> List[int]:
    match_idx = binary_search(nums, target)
    if match_idx == -1:
        return [-1, -1]

    # Now we need to find the starting and ending indices;
    # we can't really tell if we're at the start or end of the
    # sequence so the best we can do is walk both indices to
    # the left and right until we receive a diff number
    # than the target
    start, end = match_idx, match_idx
    while True:
        while (start-1) >= 0 and nums[start-1] == target:
            start -= 1
        while (end+1) < len(nums) and nums[end+1] == target:
            end += 1
        break
    return [start, end]


nums = [5, 7, 7, 8, 8, 10]
target = 8
output = [3, 4]

result = searchRange(nums, target)
assert result == output

nums2 = [2,2]
target2 = 2
expected = [0,1]
result = searchRange(nums2, target2)
assert result == expected
