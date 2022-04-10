# Constraints:
# 2000 <= Year <= 2017
# 1 <= Month <= 12
# 1 <= Day <= 31
# 0 <= Hour <= 23
# 0 <= Minute, Second <= 59
# granularity is one of the values ["Year", "Month", "Day", "Hour", "Minute", "Second"].

class LogSystem:

    def __init__(self):
        self.log = {}
        self.gran = {"Year": 4, 'Month': 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19 }

    def put(self, id: int, timestamp: str) -> None:
        self.log[id] = timestamp
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        # print(self.log)
        idx = self.gran[granularity]
        for k, v in self.log.items():
            # print(start[:idx])
            if start[:idx] <= v[:idx] <= end[:idx]:
                res.append(k)
        return res 


# Input
# ["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
# [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
# Output
# [null, null, null, null, [3, 2, 1], [2, 1]]

# Explanation
# LogSystem logSystem = new LogSystem();
# logSystem.put(1, "2017:01:01:23:59:59");
# logSystem.put(2, "2017:01:01:22:59:59");
# logSystem.put(3, "2016:01:01:00:00:00");

# // return [3,2,1], because you need to return all logs between 2016 and 2017.
# logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");

# // return [2,1], because you need to return all logs between Jan. 1, 2016 01:XX:XX and Jan. 1, 2017 23:XX:XX.
# // Log 3 is not returned because Jan. 1, 2016 00:00:00 comes before the start of the range.
# logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");