from typing import List
import time


def merge(left: List[int], right: List[int]) -> List[int]:
    result: List[int] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(values: List[int]) -> List[int]:
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    return merge(left, right)


def main() -> None:
    values = list(map(int, input("Enter integers separated by spaces: ").split()))

    start = time.perf_counter()
    sorted_values = merge_sort(values)
    elapsed = time.perf_counter() - start

    print("Sorted data:", sorted_values)
    print(f"Execution time: {elapsed:.8f} seconds")
    print("Time complexity: O(n log n)")
    print("Space complexity: O(n)")


if __name__ == "__main__":
    main()
