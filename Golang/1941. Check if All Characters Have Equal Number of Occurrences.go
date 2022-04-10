//  Given a string s, return true if s is a good string, or false otherwise.
// A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

func areOccurrencesEqual(s string) bool {
	seen := map[rune]int{}

	for _, val := range s {
		seen[val]++
	}
	// fmt.Println(seen)
	ref := seen[rune(s[0])]

	for _, v := range seen {
		if v != ref {
			return false
		}
	}
	return true
}

// TC: O(n), SC: O(1)