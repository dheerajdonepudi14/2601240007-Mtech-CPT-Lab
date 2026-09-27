# Program 2 — 0/1 Knapsack — Dynamic Programming

## 1. Problem Statement

Implement Dynamic Programming for 0/1 Knapsack and analyze time and space complexity.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 2 |
| Topic | 0/1 Knapsack — Dynamic Programming |
| Main concept | 0/1 Knapsack — Dynamic Programming |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** Items: weights [2,3,4], values [4,5,7], capacity 5. The DP table chooses the maximum value without selecting an item more than once.

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
from typing import List, Tuple


def knapsack(
    weights: List[int],
    values: List[int],
    capacity: int
) -> Tuple[int, List[int]]:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for current_capacity in range(capacity + 1):
            if weights[i - 1] <= current_capacity:
                include = values[i - 1] + dp[i - 1][current_capacity - weights[i - 1]]
                exclude = dp[i - 1][current_capacity]
                dp[i][current_capacity] = max(include, exclude)
            else:
                dp[i][current_capacity] = dp[i - 1][current_capacity]

    selected_items: List[int] = []
    current_capacity = capacity

    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            selected_items.append(i)
            current_capacity -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items


def main() -> None:
    n = int(input("Enter number of items: "))
    weights = list(map(int, input("Enter weights: ").split()))
    values = list(map(int, input("Enter values: ").split()))
    capacity = int(input("Enter knapsack capacity: "))

    if len(weights) != n or len(values) != n:
        print("Error: number of weights and values must match n.")
        return

    maximum_value, selected = knapsack(weights, values, capacity)

    print("Maximum value:", maximum_value)
    print("Selected item numbers:", selected)
    print("Time complexity: O(n * capacity)")
    print("Space complexity: O(n * capacity)")


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

0/1 Knapsack uses O(n × capacity) time and O(n × capacity) space because the full DP table is stored.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **0/1 Knapsack — Dynamic Programming** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
