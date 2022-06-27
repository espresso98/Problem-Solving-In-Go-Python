// O(n), O(n)

func longestConsecutive(nums []int) int {
	set := make(map[int]bool)
	for _, n := range nums {
		set[n] = true
	}
	longest := 0
	for n := range set {
		if set[n-1] {
			continue
		}
		length := 1
		for set[n+length] {
			length++
		}
		if length > longest {
			longest = length
		}
	}
	return longest
}

// Input: nums = [100,4,200,1,3,2]
// Output: 4
// The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.