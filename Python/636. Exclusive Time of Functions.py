# O(N), O(N)
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        for log in logs:
            id, status, time = log.split(':')
            if status == 'start':
                stack.append((int(id), int(time)))
            else:  # status = 'end'
                cur_id, cur_start = stack.pop()
                delta = int(time) - cur_start + 1
                res[cur_id] += delta
                if stack:
                    prev_id = stack[-1][0]
                    res[prev_id] -= delta
        return res
        