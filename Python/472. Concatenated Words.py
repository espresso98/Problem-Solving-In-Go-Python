class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)  # {'catdog', 'cat', 'dog'}
        memo = {}
        def dfs(word):         # ["cat","dog","catdog"]
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:] # c at/ ca t/ d og / do g/ c atdog/ ca tdog/ cat dog
                if prefix in word_set and (suffix in word_set or dfs(suffix)): 
                    memo[word] = True  # {'cat': False, 'dog': False, 'catdog': True}
                    return True
            memo[word] = False         # {'cat': False} {'cat': False, 'dog': False}
            return False
        
        return [word for word in words if dfs(word)]
