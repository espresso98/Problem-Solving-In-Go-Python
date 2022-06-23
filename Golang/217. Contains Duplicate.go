// TC: O(n), SC: O(n)
func containsDuplicate(nums []int) bool {
	set := make(map[int]bool)
	for _, n := range nums {
		if _, ok := set[n]; ok {
			return true
		}
		set[n] = true
	}
	return false
}

// Input: nums = [1,2,3,1]
// Output: true