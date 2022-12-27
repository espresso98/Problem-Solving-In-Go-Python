# 16: true (2^4), 24: false, 46: true (<- 64 = 2^8)
# 1 <= n <= 10^9, 2^30 = 1073741824
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = ["".join(sorted(list(str(1 << i)))) for i in range(31)]
        target = "".join(sorted(list(str(n))))
        return target in powers
        