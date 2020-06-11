"""
shared value
=============

Output:
::
    worker[0] got normal_v 1, shared_v 1
    worker[1] got normal_v 1, shared_v 2
    all done
"""

from concurrent.futures import ProcessPoolExecutor, wait
from multiprocessing import Manager
from ctypes import c_int64


def worker(i: int, normal_v: int, shared_v) -> None:
    # isolated memroy between processes, so every process will get 1
    normal_v += 1
    # shared memory, so will get 1 and 2 respectively
    shared_v.value += 1

    print(f"worker[{i}] got normal_v {normal_v}, shared_v {shared_v.value}")


def main():
    executor = ProcessPoolExecutor(max_workers=2)
    with Manager() as manager:
        lock = manager.Lock()
        shared_v = manager.Value(c_int64, 0, lock=lock)
        normal_v = 0

        workers = [executor.submit(worker, i, normal_v, shared_v) for i in range(2)]
        wait(workers)
        print("all done")


if __name__ == "__main__":
    main()
