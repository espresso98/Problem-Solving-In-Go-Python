# get the balance of each account
# backtrack to get global minimum number of transaction
# once current_account * next_account < 0, we perform 1 transaction in order to get settle up.

from collections import defaultdict
import math
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = defaultdict(int)
        for sender, receiver, amount in transactions:
            balances[sender] -= amount
            balances[receiver] += amount
        debts = [b for b in balances.values() if b != 0] 
        print(balances, debts)
        n = len(debts)
        
        def dfs(curr_id):
            while curr_id < n and debts[curr_id] == 0:
                curr_id += 1
            
            if curr_id == n:
                return 0
            
            res, visited = math.inf, set()
            
            for next_id in range(curr_id + 1, n):
                if debts[curr_id] * debts[next_id] < 0 and debts[next_id] not in visited:
                    debts[next_id] += debts[curr_id]
                    res = min(res, dfs(curr_id+1) + 1)
                    debts[next_id] -= debts[curr_id]
                    visited.add(debts[next_id])
            return res
                
        return dfs(0) # account_id