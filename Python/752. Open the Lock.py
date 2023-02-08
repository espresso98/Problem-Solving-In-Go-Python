# BFS
# return the minimum total number of turns required to open the lock
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def neighbors(node:str) -> List[str]:
            res = []
            for i in range(4):
                up = (int(node[i]) + 9) % 10    # (10) -1
                down = (int(node[i]) + 1) % 10  # +1 
                res.append(node[:i] + str(up) + node[i+1:])
                res.append(node[:i] + str(down) + node[i+1:])
            return res

        q = collections.deque([("0000", 0)]) # [lock, turns]
        visited = {"0000"}
        deadends = set(deadends)
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            if lock in deadends: continue
            for next in neighbors(lock):
                if next not in visited:
                    q.append((next, turns+1))
                    visited.add(next)
        return -1

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# '0000': ['1000', '9000', '0100', '0900', '0010', '0090', '0001', '0009']
# '1000': ['2000', '0000', '1100', '1900', '1010', '1090', '1001', '1009']  turns = 1
# '1100': ['2100', '0100', '1200']                                          turns = 2
# '1200': ['2200', '0200', '1300', '1100', '1210', '1290', '1201', '1209']  turns = 3
# '1201': ['2201', '0201', '1301', '1101', '1211', '1291', '1202', '1200']  turns = 4
# '1202': ['2202', '0202', '1302', '1102', '1212', '1292', '1203', '1201']  turns = 5
# '2202': ['3202', '1202', '2302', '2102', '2212', '2292', '2203', '2201']  turns = 6 (target found)
