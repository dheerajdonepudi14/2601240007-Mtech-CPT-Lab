import time
import tracemalloc
from typing import Iterable


def list_processing(n: int) -> int:
    values = [number * number for number in range(n)]
    return sum(values)


def generator_processing(n: int) -> int:
    values = (number * number for number in range(n))
    return sum(values)


def measure(function, n: int) -> tuple[int, float, int]:
    tracemalloc.start()
    start = time.perf_counter()

    result = function(n)

    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, elapsed, peak


def main() -> None:
    n = int(input("Enter dataset size: "))

    list_result, list_time, list_memory = measure(list_processing, n)
    gen_result, gen_time, gen_memory = measure(generator_processing, n)

    print("\nList processing")
    print("Result:", list_result)
    print(f"Time: {list_time:.6f} seconds")
    print(f"Peak memory: {list_memory / 1024:.2f} KB")

    print("\nGenerator processing")
    print("Result:", gen_result)
    print(f"Time: {gen_time:.6f} seconds")
    print(f"Peak memory: {gen_memory / 1024:.2f} KB")

    print("\nBoth methods compute the same result.")
    print("Generators avoid storing the complete intermediate list.")


if __name__ == "__main__":
    main()
