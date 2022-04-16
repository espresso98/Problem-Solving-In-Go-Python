# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.(Constraints: 0 <= index, val <= 1000) 
# Choice: Doubly Linked List 

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        # forward search from the head
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        # backward forward search from the tail    
        else: 
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val
            
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
  
    def addAtIndex(self, index: int, val: int) -> None:        
        if index > self.size:
            return

        # find predecessor and successor of the node to be adde
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next   
        else: 
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        # insertion itself
        self.size += 1
        new_node = Node(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node
            
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next   
        else: 
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        # delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Doubly Linked List 
# TC : O(1) for addAtHead, addAtTail
#    : O(min(k, N-k)) for get, addAtIndex, deleteAtIndex (k: index)
# SC : O(1)
