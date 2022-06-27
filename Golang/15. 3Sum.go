// O(N^2) / O(N)

import "sort"

func threeSum(nums []int) [][]int {
	res := [][]int{}
	N := len(nums)
	if N < 3 {
		return res
	}

	sort.Ints(nums)
	for i := 0; i < N-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		j, k := i+1, N-1
		for j < k {
			threeSum := nums[i] + nums[j] + nums[k]
			if threeSum < 0 {
				j++
			} else if threeSum > 0 {
				k--
			} else {
				res = append(res, []int{nums[i], nums[j], nums[k]})
				j++
				k--
				for j < k && nums[j] == nums[j-1] {
					j++
				}
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			}
		}
	}
	return res
}
    