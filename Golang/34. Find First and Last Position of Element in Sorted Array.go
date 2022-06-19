// O(log n) / O(1)

func searchPosition(nums []int, target int, searchLeft bool) int {
	idx := -1
	lo, hi := 0, len(nums)-1

	for lo <= hi {
		mid := lo + (hi-lo)/2

		if nums[mid] > target {
			hi = mid - 1
		} else if nums[mid] < target {
			lo = mid + 1
		} else { // nums[mid] == target
			idx = mid
			if searchLeft {
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		}
	}
	return idx
}

// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]

// func searchRange(nums []int, target int) []int {
//     l := sort.Search(len(nums), func(i int) bool {
//         return nums[i] >= target
//     })
//     if l >= len(nums) || nums[l] != target {
//         return []int{-1, -1}
//     }
//     r := sort.Search(len(nums), func(i int) bool {
//         return nums[i] >= target+1
//     })
//     return []int{l, r-1}
// }