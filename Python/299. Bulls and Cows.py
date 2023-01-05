# If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".
# secret.length == guess.length
# O(N), O(10)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, all_matches = 0, 0
        sec_dict = collections.Counter(secret)
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            if g in sec_dict and sec_dict[g] > 0:
                all_matches += 1
                sec_dict[g] -= 1
        return str(bulls) + "A" + str(all_matches - bulls) + "B"
