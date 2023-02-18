# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# The digits are stored in reverse order
# Time and Space complexity : O(n)         
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2 and carry==0:
            return None

        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0   
        
        sum_val = l1_val + l2_val + carry
        next_carry, val = divmod(sum_val, 10)
        # 0,7 / 1,0 / 0,8
        l1_next = l1.next if l1 else None
        l2_next = l2.next if l2 else None
        # (2,5,0) (4,6,1) (3,4,0)
        digit = ListNode(val=val, next=self.addTwoNumbers(l1_next, l2_next, next_carry))
        # ListNode{val: 8, next: None}
        # ListNode{val: 0, next: ListNode{val: 8, next: None}}
        # ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}
        return digit # [7,0,8] 807
       

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
