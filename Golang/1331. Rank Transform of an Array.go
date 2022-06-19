// TC: O(nlogn), SC: O(n)

func arrayRankTransform(arr []int) []int {
	sorted := make([]int, len(arr))
	copy(sorted, arr)
	sort.Ints(sorted)

	ranks, idx := make(map[int]int), 1

	for _, v := range sorted {
		if ranks[v] == 0 {
			ranks[v] = idx // ranks[10] = 1, ranks[20] = 2
			idx++
		}
	}

	for k, v := range arr {
		arr[k] = ranks[v] // arr[0] = ranks[40] = 4
	}

	return arr
}

// Input: arr = [40,10,20,30]
// Output: [4,1,2,3]