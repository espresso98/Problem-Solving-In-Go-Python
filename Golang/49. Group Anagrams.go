// O(NK), O(NK)

func groupAnagrams(strs []string) [][]string {
	var res [][]string
	dict := make(map[[26]int][]string)
	for _, s := range strs {
		var count [26]int // key
		for _, ch := range s {
			count[ch-'a']++
		}
		dict[count] = append(dict[count], s) // value
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

/* key : value
map[[1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0]:[tan nat]
    [1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]:[eat tea ate]
	[1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]:[bat]]
*/ 
