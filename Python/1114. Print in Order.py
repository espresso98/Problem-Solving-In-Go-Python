# Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

from threading import Lock

class Foo:
    def __init__(self):
        self.lock1 = Lock()  # firstJobDone
        self.lock2 = Lock()  # secondJobDone
        self.lock1.acquire()
        self.lock2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". 
        printFirst()
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        # printSecond() outputs "second". 
        with self.lock1:
            printSecond()
            self.lock2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for the second job to be done.
        with self.lock2:
            printThird()