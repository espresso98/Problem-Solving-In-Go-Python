# TC: O(E) where E is the number of edges in trust
# SC: O(N) where N is the number of people
# vote: indegree - outdegree
# 1, [] => return 1
def findJudge(self, n: int, trust: List[List[int]]) -> int:
    if n == 1 and not trust: return 1
    if len(trust) < n - 1: return -1
    votes = [-1] + [0] * n 
    for a, b in trust:
        votes[a] -= 1
        votes[b] += 1
    for person, vote in enumerate(votes):
        if vote == n - 1:
            return person
    return -1