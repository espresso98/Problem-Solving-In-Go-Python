// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
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

// TC: O(nlogn), SC: O(1)
// import (
// 	"sort"
// 	"strings"
// )

// func isAnagram(s string, t string) bool {
// if len(s) != len(t) { return false }
// a := strings.Split(s, "")
// b := strings.Split(t, "")
// sort.Strings(a)
// sort.Strings(b)
// return strings.Join(a,"") == strings.Join(b,"")
// }