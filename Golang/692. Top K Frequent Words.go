// TC: O(nlgn) SC: O(n)
import "sort"

func topKFrequent(words []string, k int) []string {
	var set []string
	freq := make(map[string]int)

	for _, w := range words {
		freq[w]++
		if freq[w] == 1 {
			set = append(set, w)
		}
	}
	sort.Slice(set, func(i, j int) bool {
		if freq[set[i]] == freq[set[j]] {
			return set[i] < set[j]
		}
		return freq[set[i]] > freq[set[j]]
	})
	return set[:k]
}

// Input: words = ["i","love","leetcode","i","love","coding"], k = 2
// Output: ["i","love"]
