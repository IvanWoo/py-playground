from dataclasses import dataclass
from functools import wraps


# cannot be used for yield from
def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


# closure
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def test_averager():
    coro_avg = averager()
    next(coro_avg)
    for i in range(4, 7):
        print(coro_avg.send(i))
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        print(exc.value)


@dataclass
class Result:
    count: int
    average: float


# the subgenerator
def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# the delegating generator
def grouper(results, key):
    while True:
        results[key] = yield from averager()


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print(
            "{:2} {:5} averaging {:.2f}{}".format(
                result.count, group, result.average, unit
            )
        )


# the client code, a.k.a. the caller
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)
    report(results)


data = {
    "girls;kg": [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    "girls;m": [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    "boys;kg": [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    "boys;m": [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == "__main__":
    main(data)
