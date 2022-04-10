// TC: O(n), SC: O(1)

func runningSum(nums []int) []int {
	result := make([]int, len(nums))
	result[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		result[i] = result[i-1] + nums[i]
	}
	return result
}

// func runningSum(nums []int) []int {
//     for i := 1; i < len(nums); i++ {
//         nums[i] += nums[i-1]
//     }
//     return nums
// }
