# 5. Inventory Item Using Dataclass

## 1. Problem Statement

An inventory system stores **product ID, product name, quantity, and price**. The class mainly stores data and requires little custom initialization logic. Apply **Dataclass** to model the inventory item.

The `@dataclass` decorator automatically provides useful methods such as an initializer and a readable representation for this data-focused class.

---

## 2. Algorithm Identification

| Item | Description |
|---|---|
| Concept | Python Dataclass |
| Decorator | `@dataclass` |
| Class | `InventoryItem` |
| Fields | Product ID, Product Name, Quantity, Price |
| Purpose | Reduce boilerplate code for data-holding classes |

### Dataclass Used

```python
@dataclass
class InventoryItem:
    product_id: int
    product_name: str
    quantity: int
    price: float
```

---

## 3. Step-by-Step Example

### Given Data

| Field | Value | Type |
|---|---|---|
| Product ID | `101` | `int` |
| Product Name | `Laptop` | `str` |
| Quantity | `10` | `int` |
| Price | `55000.00` | `float` |

### Execution

1. Import `dataclass` from the `dataclasses` module.
2. Apply `@dataclass` to `InventoryItem`.
3. Declare the four data fields with type annotations.
4. Create an inventory item object.
5. Dataclass-generated initialization stores the field values.
6. Print the object using its generated representation.

### Result

```text
Item 1: InventoryItem(product_id=101, product_name='Laptop', quantity=10, price=55000.0)
```

### Second Example

```text
Item 2: InventoryItem(product_id=102, product_name='Keyboard', quantity=25, price=1200.0)
```

---

## 4. Algorithm

1. Start the program.
2. Import `dataclass`.
3. Define `InventoryItem` using `@dataclass`.
4. Declare `product_id` as `int`.
5. Declare `product_name` as `str`.
6. Declare `quantity` as `int`.
7. Declare `price` as `float`.
8. Create inventory item objects.
9. Display the objects.
10. Stop.

### Why Dataclass Is Used

A dataclass is appropriate when a class mainly stores data and does not require extensive custom initialization or behavior. Python generates common methods automatically, reducing repetitive boilerplate.

---

## 5. Implementation

```python
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
```

### Class and Field Explanation

| Class / Field | Purpose |
|---|---|
| `InventoryItem` | Represents an inventory item |
| `product_id` | Stores the product identifier |
| `product_name` | Stores the product name |
| `quantity` | Stores available quantity |
| `price` | Stores product price |
| `@dataclass` | Generates common data-oriented methods |

---

## 6. Input and Output

This implementation uses predefined inventory objects instead of interactive input.

### Sample Output

```text
--- INVENTORY ITEM USING DATACLASS ---
Item 1: InventoryItem(product_id=101, product_name='Laptop', quantity=10, price=55000.0)
Item 2: InventoryItem(product_id=102, product_name='Keyboard', quantity=25, price=1200.0)
```

---

## 7. Complexity Comparison Table

| Operation | Time Complexity | Space Complexity |
|---|---:|---:|
| Create one inventory item | O(1) | O(1) |
| Store `n` inventory items | O(n) | O(n) |
| Display one item | O(1) | O(1) auxiliary |
| Overall for `n` items | O(n) | O(n) |

---

## Important Point

`@dataclass` does not mean that every class needs to be a dataclass. It is especially useful when the class is primarily a structured collection of data and benefits from automatically generated methods.

---

## Conclusion

The `InventoryItem` class is a suitable use case for Python's dataclass because it mainly stores product information. Using `@dataclass` reduces boilerplate and makes the model concise and readable.
