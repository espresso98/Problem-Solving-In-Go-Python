// TC: O(nlgn) SC: O(n)
import "sort"

func topKFrequent(nums []int, k int) []int {
	var set []int
	freq := make(map[int]int)
	for _, n := range nums {
		freq[n]++
		if freq[n] == 1 {
			set = append(set, n)
		}
	}
	sort.Slice(set, func(i, j int) bool {
		return freq[set[i]] > freq[set[j]]
	})
	return set[:k]
}

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]