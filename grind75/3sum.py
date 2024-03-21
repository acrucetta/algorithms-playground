# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

"""
Problem:
- We receive a list of nums[int]
- We want to return the list of ints such that i != j != k
and l[i] + l[j] + l[k] == 0

Approach:
- We want to compare 3 elements at a time.
- We will need to ensure we don't repeat the same indices
when we compare them.
- We can take advantage of sorting the indices to make it
easier to compare them.
- We can use two pointers and keep moving them as we go along;
if the sum is more than 0 we reduce the right pointer, if its
less than 0 we increase the left pointer; we use 1 pointer for each
char ensuring that we compare all the elements of the list

This will give us approx O(n) assuming we compare 1 element at a time with
the other 2 pointers (l and r)
"""

test_cases = {
    "case1": ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    "case2": ([0, 1, 1], []),
}

def equals_zero(i,j,k):
    resp = i+j+k
    return resp == 0

def three_sum(nums):
    nums.sort()
    n = len(nums)
    triplets = set()

    for i in range(n-2):
        firstNum = nums[i]
        left = i+1
        right = n-1

        while left < right:
            curr_sum = firstNum + nums[left] + nums[right]
            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                triplets.add((firstNum, nums[left], nums[right]))
                left += 1
                right -= 1
    return triplets

three_sum([-1, 0, 1, 2, -1, -4])
