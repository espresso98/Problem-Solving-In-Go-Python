#  ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
# O(N*M), O(N*M)
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        word_map = collections.defaultdict(set) # {first char: [suffixes]}
        for word in ideas:
            word_map[word[0]].add(word[1:])
        # {'c': {'offee'}, 'd': {'onuts'}, 't': {'offee', 'ime'}}

        res = 0
        for ch1 in word_map:
            for ch2 in word_map:
                if ch1 == ch2:
                    continue
                intersect = len(word_map[ch1] & word_map[ch2])
                # for suffix in word_map[ch1]:
                #     if suffix in word_map[ch2]:
                #         intersect += 1
                dist1 = len(word_map[ch1]) - intersect
                dist2 = len(word_map[ch2]) - intersect
                res += dist1 * dist2

        return res
        