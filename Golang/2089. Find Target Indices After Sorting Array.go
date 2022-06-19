// TC: O(n), SC: O(1)

func targetIndices(nums []int, target int) []int {
    res := []int{}   
    smallCnt := 0
    targetCnt := 0
    
    for _, n := range nums {
        if n < target {
            smallCnt++
        } else if n == target {
            targetCnt++    
        }
    }
    
    for i := 0; i < targetCnt ; i++ {
        res = append(res, smallCnt + i)
    }
    return res
}
    

// TC: O(nlogn), SC: O(1)

import "sort"

func targetIndices(nums []int, target int) []int {
    res := []int{}
    sort.Ints(nums)
    
    for i, n := range nums {
        if n == target {
            res = append(res, i)
        }
    }
    return res
}

// Input: nums = [1,2,5,2,3], target = 2
// Output: [1,2]
// Explanation: After sorting, nums is [1,2,2,3,5].