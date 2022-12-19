# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.
# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.
# The concatenation of all the chunks should result in a list of the sorted values.
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.ptr = 0
 
    def insert(self, idKey: int, value: str) -> List[str]:
        idx = idKey -1       
        self.stream[idx] = value  
        
        if self.ptr < idx: return [] 
        else:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                self.ptr += 1
        # print(idx, value, self.stream, self.stream[idx:self.ptr])   
        return self.stream[idx:self.ptr]


"""
Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
"""

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
