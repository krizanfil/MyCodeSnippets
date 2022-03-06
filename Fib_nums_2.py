from functools import cache, wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f'{func.__name__}({str(*args)}) = {result} -> {duration:.8f}s')
        return result
    return wrapper


@cache
@timer
def fibonacci(num: int) -> int:
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci(20)
