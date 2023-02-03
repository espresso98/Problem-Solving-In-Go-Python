import collections

# O(n*m), O(n*m): hashmap and count array, Categorize by Count
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            cnts = [0] * 26   # key
            for ch in s:
                cnts[ord(ch) - ord('a')] += 1
            dic[tuple(cnts)].append(s)
        return list(dic.values())

# {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], ...} 



# sorted() will treat a str like a list and iterate through each element.
# O(n*mlogm) / O(n*m): hashmap & sort, Categorize by Sorted String
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))  # sorted("eat") -> ['a', 'e', 't'], key: aet, ant, abt
            dic[key].append(s)
        return list(dic.values())

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# "eat" -> ['a', 'e', 't'] aet
# "tea" -> ['a', 'e', 't'] aet
# "tan" -> ['a', 'n', 't'] ant
# "ate" -> ['a', 'e', 't'] aet
# "nat" -> ['a', 'n', 't'] ant
# "bat" -> ['a', 'b', 't'] abt
# dic = {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
