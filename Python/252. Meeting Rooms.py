# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
# O(nlogn), O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool: 
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
        

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false