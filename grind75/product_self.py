# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
Problem:
- We have a array nums e.g., [1,2,3,4]
- For each index in the array we want to find the product of all the elements
except the current one
- We need to do it in O(n) time; without using the division operation

Approaches:
- Iterate over array with a pointer skipping the current index;
multiply all of the values and add them to a new array; once
done with each iteration increase the index by 1 -- O(N)

Follow-ups:
- Can we solve this problem in O(1)

Edge cases:
- Empty array
- Only 1 value in the array
- All negative
"""

test_1 = [1, 2, 3, 4]
test_2 = [-1, 1, 0, -3, 3]
result1 = [24, 12, 8, 6]
result2 = [0, 0, 9, 0, 0]

from typing import List

# 1 * 2 * 3 * 4

# O(N) with O(1)


def productExceptSelf(self, nums: List[int]) -> List[int]:
    """Calculate an array of the products for every element
    in the array except the one at the same index.
    Args:
        nums (List[int]): Array of ints
    Returns:
        List[int]: Array of products
    """
    array_length = len(nums)
    prefix = 1
    suffix = 1
    result = [1] * array_length

    for i in range(1, array_length):  # start, stop, step
        prefix *= nums[i - 1]
        result[i] *= prefix

        suffix_i = array_length - i - 1
        suffix *= nums[suffix_i + 1]
        result[suffix_i] *= suffix

    return result


# O(N) with O(N) space


def get_product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    print(n)
    resp = [0] * n

    left_prod = 1
    left_prods = [1] * n
    left_prods[0] = 1
    for i in range(1, n):
        left_prods[i] = nums[i - 1] * left_prods[i - 1]

    right_prod = 1
    right_prods = [1] * n
    right_prods[n - 1] = 1

    i = n - 2
    while i >= 0:
        right_prods[i] = nums[i + 1] * right_prods[i + 1]
        i -= 1

    for i in range(n):
        resp[i] = left_prods[i] * right_prods[i]

    print(left_prods)
    print(right_prods)
    print(resp)
    return resp


got = get_product_except_self(test_1)
expected = got
