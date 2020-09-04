from inspect import getgeneratorstate


def simple_coro():
    print("-> coroutine started")
    x = yield
    print(f"-> coroutine received: {x}")


def main():
    my_coro = simple_coro()
    print(f"{getgeneratorstate(my_coro)=}")
    next(my_coro)
    print(f"{getgeneratorstate(my_coro)=}")
    try:
        my_coro.send(42)
    except StopIteration:
        print("-> coroutine stopped")
        print(f"{getgeneratorstate(my_coro)=}")


def simple_coro2(a):
    print(f"-> Started: {a=}")
    b = yield a
    print(f"-> Received: {b=}")
    c = yield a + b
    print(f"-> Received: {c=}")


def main2():
    my_coro = simple_coro2(14)
    print(f"{getgeneratorstate(my_coro)=}")
    next(my_coro)
    print(f"{getgeneratorstate(my_coro)=}")
    my_coro.send(28)
    print(f"{getgeneratorstate(my_coro)=}")
    try:
        my_coro.send(42)
    except StopIteration:
        print("-> coroutine stopped")
        print(f"{getgeneratorstate(my_coro)=}")


if __name__ == "__main__":
    main()
    print("-" * 20)
    main2()
