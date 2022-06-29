// valid : windowLen - maxFreq <= k
func characterReplacement(s string, k int) int {
	count := make(map[byte]int)
	maxLen, maxFreq, l := 0, 0, 0

	for r := range s {
		count[s[r]]++
		maxFreq = max(maxFreq, count[s[r]])

		if (r-l+1)-maxFreq > k {
			count[s[l]]--
			l++
		}
		maxLen = max(maxLen, r-l+1)
	}
	return maxLen
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.