# Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

# There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.
# If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.
# If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.

# a Semaphore -- trying to acquire it, is possible if there are tokens left. Otherwise the thread that tried is asked to wait until a different thread returns the tokens it was using.
# a Barrier -- if a thread reaches it, it can cross it, only if a predefined number of other threads have also arrived.
# Logic
# The solution creates 1 Semaphore for Hydrogen, and allows 2 threads to aquire it concurrently. Likewise, we create one for Oxygen, but this one only allows 1 thread.
# To ensure the molecule is generated at once, we use a barrier, which can only be crossed when 3 atoms have gathered.
# After each function completes, we release the token on the Semaphore.

from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.bar.wait()
            # releaseHydrogen() outputs "H". 
            releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.bar.wait()
            # releaseOxygen() outputs "O". 
            releaseOxygen()
        

# from threading import Barrier, Semaphore
# class H2O:
#     def __init__(self):
#         self.b = Barrier(3)
#         self.h = Semaphore(2)
#         self.o = Semaphore(1)

#     def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
#         self.h.acquire()
# 		  self.b.wait()
#         # releaseHydrogen() outputs "H". Do not change or remove this line.
#         releaseHydrogen()
#         self.h.release()

#     def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
#         self.o.acquire()
# 		  self.b.wait()
#         # releaseOxygen() outputs "O". Do not change or remove this line.
#         releaseOxygen()
#         self.o.release()