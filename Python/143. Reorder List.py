# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(n), O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        
        # find middle
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half (prev-curr-tmp)
        second = curr = slow.next
        prev = None
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]