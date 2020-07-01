# https://www.youtube.com/watch?v=5VCywjS8YEA
import time


def bar(func):
    def inner():
        print("in bar: before")
        func()
        print("in bar: end")

    return inner


def baz(func):
    def inner():
        print("in baz: before")
        func()
        print("in baz: end")

    return inner


@bar
@baz
def foo():
    print("foo!")


def timeit(func):
    def inner(*args):
        s = time.time()
        func(*args)
        e = time.time()
        print(f"{func.__name__} finished in {e - s} sec.")

    return inner


@timeit
def slow_method(a, b):
    time.sleep(2)
    print(f"{a} + {b} = {a + b}")
    print("done!")


class MyCache(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
        print(f"in MyCache __init__ {func.__name__}")

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@MyCache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@MyCache
def fib2(n):
    if n <= 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)


if __name__ == "__main__":
    # foo()
    # slow_method(1, 2)
    print(fib(330))
    print(fib2(330))
