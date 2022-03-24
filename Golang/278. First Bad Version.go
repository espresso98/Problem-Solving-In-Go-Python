/* You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.*/ 

// The isBadVersion API is already defined for you.
// def isBadVersion(version: int) -> bool:

// Approach: Binary Search
// TC: O(logn), SC: O(1)

func firstBadVersion(n int) int {
    low, high := 1, n
    for low < high {
        mid := low + (high-low)/2
        if isBadVersion(mid) {
            high = mid
        } else {
            low = mid + 1
        }
    }
    return low
}


// Input: n = 5, bad = 4
// Output: 4
// Explanation:
//  call isBadVersion(3) -> false
//  call isBadVersion(5) -> true
//  call isBadVersion(4) -> true
//  Then 4 is the first bad version.