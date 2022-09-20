from time import time


def decorator_1(func):
    def wrap_func(*args, **kwargs):
        wrap_func.counter += 1

        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()

        print(
            f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s.\nNumber of calls: {wrap_func.counter}."
        )
        return result

    wrap_func.counter = 0

    return wrap_func
