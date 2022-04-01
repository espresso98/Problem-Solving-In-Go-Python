from threading import Semaphore, Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pushing = Semaphore(self.capacity)
        self.pulling = Semaphore(0)
        self.editing = Lock()
        self.queue = []
        

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()
        self.queue.append(element)
        self.editing.release()
        self.pulling.release() 
        

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        item = self.queue.pop(0)
        self.editing.release()
        self.pushing.release()
        return item
        
        
    def size(self) -> int:
        return len(self.queue)
        