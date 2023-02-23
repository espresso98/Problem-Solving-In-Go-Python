/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// O(N), O(1)
func getDecimalValue(head *ListNode) int {
	var res int
	for head != nil {
		res = (res << 1) | head.Val
		head = head.Next
	}
	return res
}

func getDecimalValue(head *ListNode) int {
	var res int
	for head != nil {
		res <<= 1
		res |= head.Val
		head = head.Next
	}
	return res
}

func getDecimalValue(head *ListNode) int {
	res := head.Val
	for head.Next != nil {
		res = res*2 + head.Next.Val
		head = head.Next
	}
	return res
}
