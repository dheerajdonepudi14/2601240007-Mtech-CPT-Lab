# Program 12 — AI-Assisted Code Review, Refactoring and Testing

## 1. Problem Statement
Perform AI-assisted code review, refactoring and testing of a Python project and document where AI assistance succeeded and where manual intervention was required.

## 2. Algorithm / Concept Identification
| Item | Details |
|---|---|
| Topic | AI-assisted review and refactoring |
| Main operations | Total and discount calculation |
| Verification | Unit tests and manual review |
| Human role | Validate AI suggestions and edge cases |

## 3. Step-by-Step Example
1. Review the original requirements.
2. Inspect input validation.
3. Refactor duplicated or unclear logic.
4. Ask an AI assistant for review/test suggestions.
5. Run tests.
6. Manually verify the final changes.

## 4. Procedure
- Validate that prices are not negative.
- Validate discount percentage is between 0 and 100.
- Calculate the total.
- Apply the discount.
- Test normal and invalid inputs.
- Record AI suggestions and manually accepted/rejected changes.

## 5. Implementation
~~~python
from typing import List


def calculate_total(prices: List[float]) -> float:
    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative")
    return round(sum(prices), 2)


def calculate_discount(total: float, percentage: float) -> float:
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")
    return round(total - (total * percentage / 100), 2)


def main() -> None:
    prices = [100.0, 250.0, 50.0]
    total = calculate_total(prices)
    final_total = calculate_discount(total, 10.0)

    print("Total:", total)
    print("Final total after 10% discount:", final_total)
    print("Review: validate inputs, test edge cases, manually verify AI changes")


if __name__ == "__main__":
    main()
~~~

## 6. Input and Output
**Input:** `[100, 250, 50]`, discount `10%`

**Output:** Total = `400.0`; final total = `360.0`.

## 7. Complexity
| Operation | Complexity |
|---|---|
| Total calculation | O(n) |
| Discount calculation | O(1) |
| Extra space | O(1), excluding input |

## 8. AI Success vs Manual Intervention
**AI can assist with:** code review checklists, test-case generation, refactoring suggestions and documentation.

**Manual intervention remains necessary for:** confirming business requirements, validating security/correctness, deciding whether a suggested change is appropriate, and checking edge cases.

## 9. Conclusion
AI assistance can accelerate review and testing, but the final implementation must be verified by the developer.
