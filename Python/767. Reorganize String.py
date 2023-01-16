# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Hint: Alternate placing the most common letters.
# O(NlogK), O(K) where N is the length of s and K is the number of unique characters
import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        s_cnts = collections.Counter(s)    #  {'a': 3, 'b': 1}

        max_heap = [(-cnt, ch) for ch, cnt in s_cnts.items()]  
        heapq.heapify(max_heap)

        res = []  # Reorganized
        prev_cnt, prev_ch = 0, ''
        while max_heap:
            cur_cnt, cur_ch = heapq.heappop(max_heap)  #  -3, 'a' / -1, 'b' / -2, 'a'
            res += [cur_ch]                            # 'a'   'b'   'a'
            if prev_cnt < 0:   # -prev_cnt > 0
                 heapq.heappush(max_heap, (prev_cnt, prev_ch)) # heappush (-2, 'a')
            cur_cnt += 1       # decrease the count by 1   -2   -1  
            prev_cnt, prev_ch = cur_cnt, cur_ch    # prev : -2, 'a' /  0, 'b' / -1, 'a'

        res = ''.join(res)
        return res if len(res) == len(s) else ''   # 'aba' != 'aaab'
