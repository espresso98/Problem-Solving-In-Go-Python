// O(n), O(n)
func lengthOfLongestSubstring(s string) int {
	maxLen, start := 0, 0
	seen := map[rune]int{}

	for idx, ch := range s {
		// duplicate
		if _, ok := seen[ch]; ok && start <= seen[ch] {
			start = seen[ch] + 1 // skip a duplicate
		} else {
			maxLen = max(maxLen, idx-start+1)
		}
		seen[ch] = idx // update last seen index
		fmt.Println(start, seen, maxLen, idx-start+1)
	}
	return maxLen
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.