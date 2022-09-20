import random
from math import sqrt

from task_1 import decorator_1
from task_2 import decorator_2
from task_3 import Decorator3
from task_4 import Decorator4


@decorator_1
def funx(n=2, m=5):
    """
    Dummy function from example for tests
    """
    max_val = float("-inf")
    n = random.randint(10, 20)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    print(f"funx max value: {max_val}")


@decorator_1
def pascal(n=3, sep=""):
    """
    Function prints Pascal's Triangle
    :param n: depth of triangle
    :param sep: separator for output
    """
    print(f"Pascal triangle for n = {n}")
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(" ", end="")
        b_c = 1
        for j in range(1, i + 1):
            print(" ", b_c, sep=sep, end=sep)
            b_c = b_c * (i - j) // j
        print("")


def sqr_eq(a=1, b=1, c=1):
    """
    Quadratic equation solver printer
    :param a: coef for x^2
    :param b: coef for x
    :param c: free variable

    """
    D = b ** 2 - 4 * a * c

    if D == 0:
        x = -b / (2 * a)
        print(f"x = {x} for {a}x^2 + ({b})x + ({c}) = 0 quadratic equation")
    elif D < 0:
        print(f"No real roots for {a}x^2 + ({b})x + ({c}) = 0 quadratic equation")
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(
            f"x1 = {x1}\nx2 = {x2}\nFor {a}x^2 + ({b})x + ({c}) = 0 quadratic equation"
        )


def test_task_1():
    pascal(n=1)
    funx()
    pascal(n=2, sep="*")
    funx()
    pascal(n=3)


@decorator_2
def funh(bar1, bar2=""):
    """
    Function to test decorator_2
    Multiline output to test proper io hijacking
    """
    print("Hello\nInnopolis\nUniversity")


def test_task_2():
    funh(None, bar2="")


sqr = lambda x: x ** 2
qube = lambda x: x ** 3


@Decorator3
def fsqr(n=2, m=5):
    """
    Function for testing Decorator3
    """
    max_val = float("-inf")
    n = sqr(random.randint(10, 20))
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    print(max_val)


@Decorator3
def fqub(n=2, m=5):
    """
    Function for testing Decorator3
    """
    max_val = float("-inf")
    n = qube(random.randint(10, 20))
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    print(max_val)


@Decorator3
def fsq1(n=2, m=5):
    """
    Function for testing Decorator3
    """
    max_val = float("-inf")
    n = sqr(random.randint(10, 20)) + 1
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    print(max_val)


@Decorator3
def fqu2(n=2, m=5):
    """
    Function for testing Decorator3
    """
    max_val = float("-inf")
    n = qube(random.randint(10, 20)) - 1
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    print(max_val)


def test_task_3():
    fsqr()
    fqub()
    fsq1()
    fqu2()
    Decorator3.print_rank()


@Decorator4
def fun_err(x=1, y=0):
    """
    Function for testing Decorator4.
    Raises a division by zero exception
    """
    return x / y


@Decorator4
def fqu3(n=2, m=5):
    """
    Function for testing Decorator4
    """
    max_val = float("-inf")
    n = qube(random.randint(10, 20)) - 1
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    print(max_val)


def test_task_4():
    fun_err()
    fqu3()


if __name__ == "__main__":
    print(f'{"=" * 20}')
    print(f"Testing Task 1")
    print(f'{"=" * 20}')
    test_task_1()
    print(f'{"=" * 20}')
    print(f"Testing Task 2")
    print(f'{"=" * 20}')
    test_task_2()
    print(f'{"=" * 20}')
    print(f"Testing Task 3")
    print(f'{"=" * 20}')
    test_task_3()
    print("Check output_task_3.txt for decorator output")
    print(f'{"=" * 20}')
    print(f"Testing Task 4")
    print(f'{"=" * 20}')
    test_task_4()
    print(
        "Check output_task_4.txt for decorator output and error_log_task_4.txt for errors"
    )
    print(f'{"="*20}')
