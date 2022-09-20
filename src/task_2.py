import io
from contextlib import redirect_stdout
from inspect import *
from time import time


def decorator_2(func):
    def get_output(func, args, kwargs):
        def tabulation(output):
            str = ""
            for line in output:
                str += "\t" + line + "\n"
            return str

        with io.StringIO() as buf, redirect_stdout(buf):
            func(args, kwargs)
            return tabulation(buf.getvalue().splitlines())

    def print_info(func, args, kwds):
        print(f"Name:    {func.__name__}")
        print(f"Type:    {type(func)}")
        print(f"Sign:    {signature(func)}")
        print(f"Args:    positional {args}\n\t\t key-worded {kwds}")
        print(f"Doc:     {func.__doc__}")
        print(f"Source:\n{getsource(func)}")
        print(f"Output:\n{get_output(func, args, kwds)}")

    # You can use the already existing function decorator in task 1
    def wrapper(*args, **kwds):
        wrapper.counter += 1

        t1 = time()
        result = func(*args, **kwds)
        t2 = time()

        print(
            f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s.\nNumber of calls: {wrapper.counter}."
        )
        print_info(func, args, kwds)

        return result

    wrapper.counter = 0

    return wrapper
