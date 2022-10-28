from time import perf_counter_ns
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        duration = end - start
        # arg = str(*args)
        print(duration)
        return result
    return wrapper

@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(func.__name__)
fib(5)
