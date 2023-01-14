# TC: O((N+M)*logK), SC: 0(26) -> O(1)
# N is the length of strings s1 and s2, M is the length of string baseStr
# K is the number of unique characters in s1 or s2, 26 here
import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {i: i for i in string.ascii_lowercase}

        # Get the root element recursively    
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]  # Returns the root representative of the component

        # Perform union if x and y aren't in the same component.
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:       # If their root are not same, combine them
                if rootX < rootY:    # Make the smaller character representative
                    root[rootY] = rootX
                else: 
                    root[rootX] = rootY    
        
        # Union the two equivalent characters
        for a, b in zip(s1,s2):
            union(a, b)
        
        res = ''
        # Convert baseStr with the lexicographically smallest equivalent string
        for ch in baseStr:
            res += find(ch)
        return res

# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# {'a': 'a', ..., 'i': 'e', 'o': 'a', 'p': 'm', 'r': 'k', 's': 'k', ..., 'z': 'z'}