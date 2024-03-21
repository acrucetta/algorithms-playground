"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

E.g., 1
Inout: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

E.g., 2
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Question:

We have a list of N intervals. We receive an new interval M.

We want to insert the interval M into N and ensure that the output doesn't overlap with
the list of existing intervals.

Approach:
- Grab newInterval and iterate over the intervals, if there's an overlap with the interval, grab the earliest interval, keep iterating until we find a start intervals that's higher than the end interval of our new interval; return the final list of intervals

e.g., [2,5]

Compare with [1,3]; 2 is less than 3 so we merge
New interval: [1,5]

Continue, check now with [6, 9], now we have [1,5] but the
current interval 5 is < 6 so we keep that interval.
"""

from typing import List


def merge_interval(
    intervals: List[List[int]], new_interval: List[int]
) -> List[List[int]]:
    resp = []
    for interval in intervals:
        if interval[1] < new_interval[0]: # No overlap; before new interval
            resp.append(interval)
        elif interval[0] > new_interval[1]: # No overlap; after new interval
            resp.append(new_interval)
            new_interval = interval
        else: # Overlap; merge
            new_interval = [min(interval[0], new_interval[0]), max(interval[1], new_interval[1])]

    print(f"Resp:{resp}")
    return resp


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
merge_interval(intervals, newInterval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
merge_interval(intervals, newInterval)
