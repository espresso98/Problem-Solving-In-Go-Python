// O(NK), O(NK)

func groupAnagrams(strs []string) [][]string {
	var res [][]string
	dict := make(map[[26]int][]string)
	for _, s := range strs {
		var count [26]int
		for _, ch := range s {
			count[ch-'a']++
		}
		dict[count] = append(dict[count], s)
		fmt.Println(count)
	}

	for _, v := range dict {
		res = append(res, v)
	}
	fmt.Println(res)
	return res
}

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

/*
[1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]  <- "eat"
[1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]  <- "tea"
[1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0]  <- "tan"
[1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]  <- "ate"
[1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0]  <- "nat"
[1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]  <- "bat"
[[bat] [eat tea ate] [tan nat]]
*/ 
