# O(m+n), O(m+n)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            if str1 + str2 != str2 + str1:
                return ""

            def gcd(a: int, b: int) -> int:
                while b:
                    a, b = b, a % b
                return a

            max_len = gcd(len(str1), len(str2))
            return str1[:max_len]
            