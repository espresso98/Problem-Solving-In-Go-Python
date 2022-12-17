# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# store a (key, value) pair at a given timestamp
# get a key's value at a time equal to or just less than the given timestamp
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        # {'foo': [(1, 'bar'), (4, 'bar2')]})
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key  with the value at the given time timestamp
        """
        self.store[key].append((timestamp, value))

    # O(log n), where n is the length of timestamps with key given, O(1)
    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set was called previously, with timestamp_prev <= timestamp
        """
        res = ""
        value_list = self.store[key]
        if not value_list: 
            return ""
        if timestamp > value_list[-1][0]:
            return value_list[-1][1]     # the largest timestamp_prev
        if timestamp < value_list[0][0]:
            return ""
        # binary search
        l, r = 0, len(value_list) - 1
        while l <= r:
            m = l + (r - l) // 2
            if value_list[m][0] <= timestamp:
                res = value_list[m][1]
                l = m + 1
            elif value_list[m][0] > timestamp:
                r = m - 1
        return res 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
"""
