# Design a discipline of behaviour (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

from threading import Lock

class DiningPhilosophers:
    
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left = min(philosopher, (philosopher + 1) % 5)
        right = max(philosopher, (philosopher + 1) % 5)
        
        with self.locks[left]: 
            with self.locks[right]: 
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
