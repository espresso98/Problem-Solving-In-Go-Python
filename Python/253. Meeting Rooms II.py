# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
# O(NlogN), O(N) 
class Solution:
    # Solution1
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals)==1: 
            return len(intervals)
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        # print(start)
        # print(end)
        res = 0
        i = 0
        for s in start:
            if s < end[i]:
                res += 1
            else: 
                i += 1
        return res

    # Solution2
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals)==1: 
            return len(intervals)
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        # print(starts)
        # print(ends)
        i = 0 
        num_of_rooms = 0
        for s in starts:
            if s < ends[i]:
                num_of_rooms += 1
            else:
                i += 1
            # print(s, ends[i], i,num_of_rooms)
        return num_of_rooms
       
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2