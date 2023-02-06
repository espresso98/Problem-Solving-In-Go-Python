# Return the earliest year with the maximum population.
# O(N), O(101)
from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101  # for 1950 ~ 2050
        conv_diff = 1950
        for b, d in logs:
            years[b-conv_diff] += 1
            years[d-conv_diff] -= 1

        num_peoples = 0
        max_population = 0

        for i, c in enumerate(years):
            num_peoples += c
            if num_peoples > max_population:
                max_population = num_peoples
                year = i + conv_diff 

        return year

# O(N), O(101)
from collections import defaultdict
class Solution2:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people = defaultdict(int)
        for st, end in logs:
            for year in range(st, end):
                people[year] += 1
        max_people = max(people.values())
        min_year = 2050
        for year, cnt in people.items():  
            if cnt == max_people:
                if year < min_year:
                    min_year = year
        return min_year
