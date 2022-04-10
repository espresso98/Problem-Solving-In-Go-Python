/* Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character. */

func isIsomorphic(s string, t string) bool {
	stmap := make([]byte, 256)
	tsmap := make([]byte, 256)

	for i := 0; i < len(s); i++ {
		a, b := s[i], t[i]
		if stmap[a] != 0 && stmap[a] != b {
			return false
		}
		if tsmap[b] != 0 && tsmap[b] != a {
			return false
		}
		stmap[a] = b
		tsmap[b] = a
	}
	return true
}

// TC: O(N), SC: O(1)