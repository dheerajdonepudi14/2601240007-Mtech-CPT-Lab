# Program 4 — List vs Generator Processing

## 1. Problem Statement

Compare list-based processing and generator-based processing for a large dataset in execution time and memory usage.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 4 |
| Topic | List vs Generator Processing |
| Main concept | List vs Generator Processing |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** For n = 100000, both methods calculate the same sum. The list stores all squares, while the generator produces values one at a time.

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

Both approaches are O(n) time. The list materializes all intermediate values, while the generator keeps lazy iteration state and therefore uses substantially less peak memory.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **List vs Generator Processing** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
