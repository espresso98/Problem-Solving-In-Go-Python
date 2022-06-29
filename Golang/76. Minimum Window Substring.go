func minWindow(s string, t string) string {
	if len(t) > len(s) {
		return ""
	}

	have, need := make(map[byte]int), make(map[byte]int)
	for i := range t {
		need[t[i]]++
	}

	minStr, minLen := "", len(s)+1
	l, r, match := 0, 0, 0
	for r < len(s) {
		c := s[r]
		if _, ok := need[c]; ok {
			have[c]++
			if need[c] == have[c] {
				match++
			}
		}

		for match == len(need) {
			// update the minLen and minStr
			if r-l+1 < minLen {
				minLen = r - l + 1
				minStr = s[l : r+1]
			}
			// pop from the left of window
			d := s[l]
			if _, ok := need[d]; ok {
				have[d]--
				if have[d] < need[d] {
					match--
				}
			}
			l++
		}
		r++
	}
	if minLen == len(s)+1 {
		return ""
	}
	return minStr
}

// Input: s = "ADOBECODEBANC", t = "ABC"
// Output: "BANC"