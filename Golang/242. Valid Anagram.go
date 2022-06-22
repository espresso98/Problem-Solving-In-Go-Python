// TC: O(n), SC: O(1)

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	var count [26]int
	for _, ch := range s {
		count[ch-'a']++
	}
	// fmt.Println(count)
	for _, ch := range t {
		count[ch-'a']--
	}
	for _, v := range count {
		if v != 0 {
			return false
		}
	}
	return true
}

// Input: s = "anagram", t = "nagaram"
// Output: true
// "anagram" -> [3 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0]