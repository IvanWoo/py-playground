from concurrent.futures import ThreadPoolExecutor, as_completed


def fib(x):
    if x < 2:
        return x
    return fib(x - 1) + fib(x - 2)


def main():
    numbers = range(30, 36)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fib, num): num for num in numbers}

        for future in as_completed(futures):
            num = futures[future]
            try:
                result = future.result()
                print(f"fib({num}) = {result}")
            except Exception as e:
                print(f"fib({num}) generated an exception: {e}")


if __name__ == "__main__":
    main()
