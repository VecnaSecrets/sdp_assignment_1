import inspect
from time import time
from inspect import *


def decorator_2(func):
    def get_ouput(func, args, kwargs):
        def inner(output):
            str = ''
            for line in output:
                str += '\t' + line + '\n'
            return str

        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buf, redirect_stdout(buf):
            func(args, kwargs)
            return inner(buf.getvalue().splitlines())

    def print_info(func, args, kwargs):
        print(f'Name:    {func.__name__}')
        print(f'Type:    {type(func)}')
        print(f'Sign:    {signature(func)}')
        print(f'Args:    positional {args}\n\t\t key-worded {kwargs}')
        print(f'Doc:     {func.__doc__}')
        print(f'Source:\n{inspect.getsource(func)}')
        print(f'Output:\n{get_ouput(func, args, kwargs)}')

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        wrap_func.counter += 1
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s Number of calls: ', wrap_func.counter)
        print_info(func, args, kwargs)
        return result
    wrap_func.counter = 0
    return wrap_func
