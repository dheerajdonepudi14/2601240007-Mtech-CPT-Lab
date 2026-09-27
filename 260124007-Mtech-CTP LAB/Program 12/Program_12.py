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
