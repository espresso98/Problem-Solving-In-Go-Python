//  Solution1
func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	i, j := 0, len(s)-1
	for i < j {
		a, b := rune(s[i]), rune(s[j])
		if !isValid(a) {
			i++
			continue
		}
		if !isValid(b) {
			j--
			continue
		}
		if a != b {
			return false
		}
		i++
		j--
	}
	return true
}

func isValid(b rune) bool {
	if ('a' <= b && b <= 'z') || ('0' <= b && b <= '9') {
		return true
	}
	return false
}

// TC: O(n), SC: O(1)
//  Solution2

func isPalindrome(s string) bool {
	reg, _ := regexp.Compile("[^a-z0-9]+")
	s = reg.ReplaceAllString(strings.ToLower(s), "")

	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}
