//  Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
//  Specifically, ans is the concatenation of two nums arrays. Return the array ans.
// TC: O(n), SC: O(1)

//  Solution1
func getConcatenation(nums []int) []int {
     return append(nums, nums...)
}

//  Solution2
func getConcatenation(nums []int) []int {
     n := len(nums)
     ans := make([]int, n*2)
    
     for i, v := range nums {
         ans[i], ans[i+n] = v, v
     }
     return ans
}

//  Solution3
func getConcatenation(nums []int) []int {
    n := len(nums)
    res := make([]int, n*2)

    for i:=0; i< 2*n; i++ {
        res[i] = nums[i%n]
    }
    return res
} 
    
