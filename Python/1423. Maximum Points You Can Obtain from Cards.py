# TC: O(n), SC: O(1)
def maxScore(self, cardPoints: List[int], k: int) -> int:
    cur_sum = sum(cardPoints[:k])
    res = cur_sum
    for i in range(1, k+1):
        cur_sum += cardPoints[-i] - cardPoints[k-i]
        res = max(res, cur_sum)
    return res
    