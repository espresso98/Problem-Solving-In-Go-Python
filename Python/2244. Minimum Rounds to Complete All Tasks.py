# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
# O(N), O(N)
# 1:-1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:8, 9:3, 10:4
import collections

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # task_freqs = collections.Counter(tasks)
        # rounds = 0
        # for count in task_freqs.values():
        #     if count == 1:
        #         return -1
        #     if count % 3 == 0:
        #         rounds += count // 3
        #     else:
        #         rounds += count // 3 + 1
        # return rounds

        task_freqs = collections.Counter(tasks)
        rounds = 0
        for freq in task_freqs.values():
            if freq  == 1:
                return -1
            rounds += (freq + 2) // 3
        return rounds
