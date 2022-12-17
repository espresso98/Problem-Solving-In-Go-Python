from collections import defaultdict
from heapq import heappush, heappop

class StockPrice:
    # O(1), O(N) where N is the number of distinct timestamps
    def __init__(self):
        self.latest_time = 0
        self.stock_price = defaultdict(int)  # {timestamp: price}
        self.max_heap = []  
        self.min_heap = []  

    # O(logK), O(1)
    def update(self, timestamp: int, price: int) -> None:
        """
        Updates the price of the stock at a particular timestamp, 
        correcting the price from any previous records at the timestamp.
        """
        # Updates the price of the stock at the given timestamp
        self.stock_price[timestamp] = price 
        # Update latestTime to latest timestamp.
        self.latest_time = max(self.latest_time, timestamp)
        heappush(self.max_heap, (-price, timestamp))
        heappush(self.min_heap, (price, timestamp))
        
    # O(1), O(1)
    def current(self) -> int:
        """
        Finds the latest price of the stock based on the current records. 
        The latest price is the price at the latest timestamp recorded.
        """
        return self.stock_price[self.latest_time]

    # O(K*logK) where K = number of elements in heap, O(1)
    def maximum(self) -> int:
        # Finds the maximum price the stock has been based on the current records.
        print(self.stock_price)
        print(self.max_heap)
        price, timestamp = self.max_heap[0]
        while -price != self.stock_price[timestamp]:
            heappop(self.max_heap)
            print(self.max_heap)
            price, timestamp = self.max_heap[0]
        return -price

    # O(K*logK) where K = number of elements in heap, O(1)
    def minimum(self) -> int:
        # Finds the minimum price the stock has been based on the current records.
        price, timestamp = self.min_heap[0]
        while price != self.stock_price[timestamp]:
            heappop(self.min_heap)
            # print(self.min_heap)
            price, timestamp = self.min_heap[0]
        return price
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

"""
Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
"""