from functools import update_wrapper


class Count:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'Current count: {self.count}')
        result = self.func(*args, **kwargs)
        return result


@Count
def fibonacci(num: int) -> int:
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci(20)
