"""
Median = middle value in ordered stream
If size = even, median = middle of 2 mid vals

arr[2,3,4] = median -> 3
arr[2,3] = median -> (2+3) = 2.5

Fast way / slow way

- Median
    Sort values (merge sort / quick sort)
    Find middle value (use indices)
        Check if even; then get mid-1 mid +1
        else; get middle value
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    # We need to split the array until we have 1 element in each, then
    # we compare the two elements and feed them back
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


def merge(left: List[int], right: List[int]) -> List[int]:
    merged_lst = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_lst.append(left[left_idx])
            left_idx += 1
            continue
        merged_lst.append(right[right_idx])
        right_idx += 1

    merged_lst.extend(left[left_idx:])
    merged_lst.extend(right[right_idx:])

    return merged_lst


class MedianFinder:
    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)

    def findMedian(self) -> float:
        # Sort array
        sorted_arr = merge_sort(self.lst)
        arr_length = len(sorted_arr)
        mid = arr_length // 2
        if arr_length % 2 == 0:  # even array
            median = (self.lst[mid] + self.lst[mid + 1]) / 2
            return median
        median = self.lst[mid]
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
