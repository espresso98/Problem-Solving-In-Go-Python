// TC: O(n) / SC: O(1)

func twoSum(numbers []int, target int) []int {
	currSum, lo, hi := 0, 0, len(numbers)-1

	for lo < hi {
		currSum = numbers[lo] + numbers[hi]
		if currSum == target {
			return []int{lo + 1, hi + 1}
		}
		if currSum < target {
			lo++
		} else {
			hi--
		}
	}
	return []int{-1, -1}
}

// Input: numbers = [2,3,4], target = 6
// Output: [1,3]