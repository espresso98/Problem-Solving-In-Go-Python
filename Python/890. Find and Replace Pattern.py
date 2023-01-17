# O(N*len(word)), O(len(word))
class Solution1:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def is_matched(word):              # word: 'deq', pattern = 'abb'
            word_dic, patt_dic = {}, {}
            for a, b in zip(word, pattern):     
                if a not in word_dic: 
                    word_dic[a] = b    # {'d': 'a', 'e': 'b', 'q': 'b'} 
                if b not in patt_dic:
                    patt_dic[b] = a    # {'a': 'd', 'b': 'e'}
                if (word_dic[a], patt_dic[b]) != (b, a):  # 'e' != 'q'
                    return False
            return True

        return filter(is_matched, words)

class Solution2:   
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        is_replaced = lambda word: len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern)))
        return filter(is_replaced, words)
        