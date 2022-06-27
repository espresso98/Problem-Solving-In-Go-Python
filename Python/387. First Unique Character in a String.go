func firstUniqChar(s string) int {
	m := [26]int{}
	for _, ch := range s {
		m[ch-'a']++
	}
	// fmt.Println(m)
	for i, ch := range s {
		if m[ch-'a'] == 1 {
			return i
		}
	}
	return -1
}

