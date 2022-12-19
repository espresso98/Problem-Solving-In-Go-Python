# The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.
# Return the pattern with the largest score.
# 1 <= website[i].length <= 10
# O(N^3*log(N^3)), O(N)

from collections import defaultdict, Counter
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_hist = collections.defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key = lambda x: x[1]):
            user_hist[user].append(web)
        
        patterns = Counter()
        for user, web in user_hist.items():
            pattern = set(combinations(web, 3))    
            patterns.update(pattern)    
        # print(patterns.most_common(1) # [(('home', 'about', 'career'), 2)]
        return max(sorted(patterns), key = patterns.get)
        

        """
        print(user_hist)
        defaultdict(<class 'list'>, {'joe': ['home', 'about', 'career'], 
                                     'james': ['home', 'cart', 'maps', 'home'], 
                                     'mary': ['home', 'about', 'career']})

        print(patterns)
        Counter({('home', 'about', 'career'): 2, ('home', 'cart', 'home'): 1, ('cart', 'maps', 'home'): 1, 
                 ('home', 'maps', 'home'): 1, ('home', 'cart', 'maps'): 1})


        # A Python program to demonstrate update()
        from collections import Counter
        coun = Counter()
        
        coun.update([1, 2, 3, 1, 2, 1, 1, 2])
        print(coun)
        
        coun.update([1, 2, 4])
        print(coun)
        
        ------------------------------------------
        Counter({1: 4, 2: 3, 3: 1})
        Counter({1: 5, 2: 4, 3: 1, 4: 1})
        """
