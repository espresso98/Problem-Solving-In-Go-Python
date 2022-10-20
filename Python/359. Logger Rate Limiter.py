# TC: O(1), SC: O(N) where N is the size of unique msgs.

class Logger:
    def __init__(self):
        self.log_dict = {}  # {message: timestamp}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log_dict:  # doesn't need to limit rate
            self.log_dict[message] = timestamp
            return True
        # doesn't need to limit rate, update the timestamp of the msg
        if timestamp - self.log_dict[message] >= 10: 
            self.log_dict[message] = timestamp   # update the log_dict with the current timestamp
            return True
        else: 
            return False
            
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)