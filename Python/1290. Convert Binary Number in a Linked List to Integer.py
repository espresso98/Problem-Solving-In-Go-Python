# O(N), O(1)
def getDecimalValue(self, head: ListNode) -> int:
        # num = head.val
        # while head.next:
        #     num = num * 2 + head.next.val
        #     head = head.next
        # return num 

        num = head.val
        while head.next:
            num = num << 1 | head.next.val
            head = head.next
        return num 
