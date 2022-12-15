# O(N), O(1)
import collections

def numPairsDivisibleBy60(self, time: List[int]) -> int: 
    # Solution1   
    cnt = 0
    h = collections.defaultdict(int)
    for t in time:
        rem = t % 60
        pair = 60 - rem
        if pair in h:
            cnt += h[pair]
        if rem == 0:
            cnt += h[0]
        h[rem] += 1
    return cnt

    # Solution2
    cnt = 0
    h = collections.defaultdict(int)
    for t in time:
        rem = t % 60
        pair = 60 - rem if rem != 0 else 0
        cnt += h[pair]
        h[rem] += 1
    return cnt
