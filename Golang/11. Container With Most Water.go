// TC: O(n), SC: O(1)

func maxArea(height []int) int {
	l, r := 0, len(height)-1
	maxArea, h := 0, 0

	for l < r {
		if height[l] < height[r] {
			h = height[l]
		} else {
			h = height[r]
		}
		curArea := (r - l) * h
		if maxArea < curArea {
			maxArea = curArea
		}
		if height[l] <= height[r] {
			l++
		} else {
			r--
		}
	}
	return maxArea
}

