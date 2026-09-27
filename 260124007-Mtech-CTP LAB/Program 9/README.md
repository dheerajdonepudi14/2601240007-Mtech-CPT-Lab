# Program 9 — Testing — Pytest and Hypothesis

## 1. Problem Statement

Write comprehensive unit and integration tests for a Python application using Pytest and Hypothesis.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 9 |
| Topic | Testing — Pytest and Hypothesis |
| Main concept | Testing — Pytest and Hypothesis |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** A cart with prices 100 and 50 has total 150. A 10% discount produces 135. Pytest checks examples and Hypothesis can check properties over many generated inputs.

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
from dataclasses import dataclass
from typing import List


@dataclass
class ShoppingCart:
    items: List[float]

    def total(self) -> float:
        return round(sum(self.items), 2)

    def add_item(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append(price)


def apply_discount(total: float, percentage: float) -> float:
    if not 0 <= percentage <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return round(total * (1 - percentage / 100), 2)


def checkout(cart: ShoppingCart, discount: float) -> float:
    return apply_discount(cart.total(), discount)


def main() -> None:
    cart = ShoppingCart([])
    cart.add_item(100.0)
    cart.add_item(50.0)

    print("Cart total:", cart.total())
    print("Checkout total after 10% discount:", checkout(cart, 10.0))
    print("\nRun tests with:")
    print("pytest -q")
    print("Install testing tools with:")
    print("pip install pytest hypothesis")


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

The application operations are O(n) for summing n cart items. Test complexity depends on the number of generated examples and test cases.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Testing — Pytest and Hypothesis** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
