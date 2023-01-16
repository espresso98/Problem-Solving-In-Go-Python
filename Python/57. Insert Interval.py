# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# O(N), O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        res = []
        left, right = [], []
        for interval in intervals:
            int_start, int_end = interval
            if int_end < new_start:    # non-overlapping boundary 
                left.append(interval)
            elif int_start > new_end:  # non-overlapping boundary
                right.append(interval)
            else:                      # overlapping
                new_start = min(new_start, int_start)
                new_end = max(new_end, int_end)
        return left + [[new_start, new_end]] + right
