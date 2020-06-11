from traceback import print_exc
from concurrent.futures import ProcessPoolExecutor, wait
from multiprocessing import Event, RLock
from multiprocessing.shared_memory import ShareableList
from multiprocessing.managers import SharedMemoryManager, SyncManager
from ctypes import c_int64


def worker(
    lock: RLock, evt: Event, i: int, normal_v: int, shared_v: ShareableList
) -> None:
    try:
        # make sure all tasks start at the same time
        evt.wait()
        # isolated memroy between processes, so every process will get 1
        normal_v += 1
        with lock:
            # shared memory, so will get continued increasing value
            shared_v[0] += 1

        print(f"worker[{i}] got normal_v {normal_v}, shared_v {shared_v[0]}")
    except Exception:
        print_exc()
        raise


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    with SharedMemoryManager() as smm, SyncManager() as sm:
        evt = sm.Event()
        shared_v = smm.ShareableList([0])
        normal_v = 0
        workers = [
            executor.submit(worker, sm.RLock(), evt, i, normal_v, shared_v)
            for i in range(10)
        ]

        evt.set()
        wait(workers)
        [f.result() for f in workers]
        print("all done")


if __name__ == "__main__":
    main()
