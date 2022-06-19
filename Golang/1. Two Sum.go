// O(N), O(N)
// h[num] = idx, num:idx {2:0, 7:1, ...}

func twoSum(nums []int, target int) []int {
	hashMap := make(map[int]int, len(nums))
	var complement int

	for currIdx, num := range nums {
		complement = target - num                    // 9-2= 7, 9-7 = 2
		if complIdx, ok := hashMap[complement]; ok { // h[2] = 0
			return []int{complIdx, currIdx} // {0, 1}
		}
		hashMap[num] = currIdx // h[2] = 0
	}
	return []int{-1, -1}
}

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]