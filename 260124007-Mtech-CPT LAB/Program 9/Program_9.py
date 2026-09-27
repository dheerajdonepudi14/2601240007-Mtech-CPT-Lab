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
