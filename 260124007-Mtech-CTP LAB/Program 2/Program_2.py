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
