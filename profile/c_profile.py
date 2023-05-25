import cProfile, pstats, io
from pstats import SortKey
from functools import cache


@cache
def fib(x):
    if x < 2:
        return x
    return fib(x - 1) + fib(x - 2)


with cProfile.Profile() as pr:
    fib(30)

    sortby = SortKey.CUMULATIVE
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
