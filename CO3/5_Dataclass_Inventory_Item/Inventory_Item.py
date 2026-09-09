# 5. Inventory Item Using Dataclass

from dataclasses import dataclass


@dataclass
class InventoryItem:
    product_id: int
    product_name: str
    quantity: int
    price: float


def main() -> None:
    print("\n--- INVENTORY ITEM USING DATACLASS ---")

    item1 = InventoryItem(101, "Laptop", 10, 55000.00)
    item2 = InventoryItem(102, "Keyboard", 25, 1200.00)

    print("Item 1:", item1)
    print("Item 2:", item2)


if __name__ == "__main__":
    main()
