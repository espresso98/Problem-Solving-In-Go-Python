# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}

# rotate the list to the right by k places.
# O(N), O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return  

        # get the last node and size of list
        last = head   
        length = 1
        while last.next:
            last = last.next
            length += 1

        k = k % length         # k = k % n (k >= n)
        if k == 0: 
            return head

        # make the list circular  
        last.next = head

        # move to the new tail: (n - k - 1)th node 
        tail = head
        # In the position n - k, the new tail is just before, in the position n - k - 1
        to_rotate = length - k - 1
        for _ in range(to_rotate):
            tail = tail.next

        # make the list uncircular
        new_head = tail.next
        tail.next = None
        return new_head
