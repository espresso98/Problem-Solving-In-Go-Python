// O(t), O(1)
func isSubsequence(s string, t string) bool {
	if s == "" {
		return true
	}
	i := 0
	for j := range t {
		if s[i] == t[j] {
			i++
			if i == len(s) {
				return true
			}
		}
	}
	return false
}
