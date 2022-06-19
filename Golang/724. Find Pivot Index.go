// The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
// TC: O(N), SC: O(1)

func pivotIndex(nums []int) int {
	var leftSum, sum int
	for _, num := range nums {
		sum += num
	}
	for idx, val := range nums {
		if leftSum == sum-leftSum-val {
			return idx
		}
		leftSum += val
	}
	return -1
}

/*
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
*/