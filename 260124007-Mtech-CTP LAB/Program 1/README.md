# Program 1 — Merge Sort — Divide and Conquer

## 1. Problem Statement

Implement Divide-and-Conquer algorithms for Merge Sort and calculate their time complexities.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 1 |
| Topic | Merge Sort — Divide and Conquer |
| Main concept | Merge Sort — Divide and Conquer |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** Input: 38 27 43 3 9 82 10. Split into smaller lists, sort them recursively, then merge them.

### Working

1. Accept or define the required data.
2. Apply the concept specified in the exercise.
3. Validate important conditions and edge cases.
4. Display the result and relevant analysis.
5. Use the stated complexity/tooling/testing information where applicable.

## 4. Algorithm / Procedure

1. Start the Python program.
2. Prepare the required input or sample data.
3. Execute the main operation for the selected concept.
4. Handle invalid or exceptional conditions where appropriate.
5. Display the result.
6. Verify the behavior using the relevant complexity, testing, typing, concurrency or development workflow.

## 5. Implementation

~~~python
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
~~~

## 6. Input and Output

### Sample Input

The exact input depends on the program. Use the prompts displayed by the Python program.

### Sample Output

The program prints the calculated result and/or demonstration of the requested concept.

## 7. Complexity / Engineering Analysis

| Aspect | Analysis |
|---|---|
| Primary operation | Depends on the program's algorithm or workflow |
| Space | Depends on stored data, recursion, buffers or generated objects |
| Verification | Output, tests, type checking or timing as appropriate |

### Program-specific Notes

Merge Sort performs O(n log n) time in best, average and worst cases and uses O(n) auxiliary space in this implementation.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Merge Sort — Divide and Conquer** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
