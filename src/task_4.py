import inspect
from time import time
from inspect import *
import io
from contextlib import redirect_stdout

ranks = {}


class Decorator4:
    counter = 0
    func = 0

    def __init__(self, func):
        self.func = func

    def get_output(self, args, kwargs):
        def inner(output):
            str = ''
            for line in output:
                str += '\t' + line + '\n'
            return str

        with io.StringIO() as buf, redirect_stdout(buf):
            self.func(args, kwargs)
            return inner(buf.getvalue().splitlines())

    def print_info(self, args, kwargs):
        print(f'Name:    {self.func.__name__}')
        print(f'Type:    {type(self.func)}')
        print(f'Sign:    {signature(self.func)}')
        print(f'Args:    positional {args}\n\t\t key-worded {kwargs}')
        print(f'Doc:     {self.func.__doc__}')
        print(f'Source:\n{inspect.getsource(self.func)}')
        print(f'Output:\n{self.get_output(args, kwargs)}')

    def __call__(self, *args, **kwargs):
        try:
            global ranks
            t1 = time()
            result = self.func(*args, **kwargs)
            t2 = time()
            self.counter += 1
            res = t2 - t1
            with io.StringIO() as buf, redirect_stdout(buf):
                with open('output_task_4.txt', 'a') as output_file:
                    print(f'Function {self.func.__name__!r} executed in {res:.4f}s Number of calls: ', self.counter)
                    self.print_info(args, kwargs)
                    for line in buf.getvalue().splitlines():
                        output_file.write(line + '\n')
            ranks[self.func.__name__] = [res]
            return result
        except Exception as e:
            with open('error_log_task_4.txt', 'a') as error_log:
                error_log.write(f'{time():.0f} -- Exception message: {e}\n')



    @staticmethod
    def print_rank():
        print('PROGRAM | RANK | TIME ELAPSED')
        for index, (k, v) in enumerate(sorted(ranks.items(), key=lambda item: item[1])):
            print(f'{k}\t\t{index+1}\t\t{v[0]:.9f}')

