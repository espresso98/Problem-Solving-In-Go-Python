// O(N), O(1)
func maxProfit(prices []int) int {
	maxProf := 0
	min := prices[0]

	for i := 1; i < len(prices); i++ {
		if prices[i] < min {
			min = prices[i]
		} else if prices[i]-min > maxProf {
			maxProf = prices[i] - min
		}
	}
	return maxProf
}

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.