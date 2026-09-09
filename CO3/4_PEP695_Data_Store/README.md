# 4. Generic Data Store Using PEP 695 Syntax

## 1. Problem Statement

A product engineering team uses Python's newer generic syntax to create a reusable container. Apply **PEP 695 syntax** to create a generic `DataStore` class.

The program uses the modern class declaration `class DataStore[T]:` so that the same container can store different types of objects.

---

## 2. Algorithm Identification

| Item | Description |
|---|---|
| Concept | PEP 695 Generic Syntax |
| Generic Class | `DataStore[T]` |
| Type Parameter | `T` |
| Purpose | Create a reusable type-safe container |
| Python Version | Python 3.12+ |

### PEP 695 Syntax Used

```python
class DataStore[T]:
```

This syntax declares `T` directly in the class definition without using `TypeVar` and `Generic`.

---

## 3. Step-by-Step Example

### Given Data

| Store | Type | Data |
|---|---|---|
| `product_store` | `Product` | Laptop, Keyboard |
| `employee_store` | `Employee` | Arun, Priya |

### Execution

1. Define `DataStore[T]` using PEP 695 syntax.
2. Create a list to store values of type `T`.
3. Define `add()` to insert values.
4. Define `get_all()` to retrieve the stored values.
5. Create a `DataStore[Product]`.
6. Create a `DataStore[Employee]`.
7. Add products and employees to their corresponding stores.
8. Display all stored objects.

### Result

```text
Products: [Product(101, 'Laptop'), Product(102, 'Keyboard')]
Employees: [Employee(201, 'Arun'), Employee(202, 'Priya')]
```

### Second Example

The same `DataStore[T]` class can also be used as `DataStore[int]` or `DataStore[str]` without rewriting the container class.

---

## 4. Algorithm

1. Start the program.
2. Declare `class DataStore[T]`.
3. Initialize an empty list of type `list[T]`.
4. Define `add(item: T)`.
5. Define `get_all() -> list[T]`.
6. Create specialized stores for Product and Employee.
7. Add objects to each store.
8. Retrieve and display the stored data.
9. Stop.

### Why PEP 695 Is Used

PEP 695 introduces a cleaner syntax for declaring type parameters. It reduces the boilerplate required by older generic syntax such as `TypeVar` and `Generic`.

Old-style approach:

```python
T = TypeVar("T")
class DataStore(Generic[T]):
    ...
```

PEP 695 approach:

```python
class DataStore[T]:
    ...
```

---

## 5. Implementation

```python
# 4. Generic Data Store using PEP 695 Syntax

class DataStore[T]:
    def __init__(self) -> None:
        self.data: list[T] = []

    def add(self, item: T) -> None:
        self.data.append(item)

    def get_all(self) -> list[T]:
        return self.data


class Product:
    def __init__(self, product_id: int, name: str) -> None:
        self.product_id = product_id
        self.name = name

    def __repr__(self) -> str:
        return f"Product({self.product_id}, '{self.name}')"


class Employee:
    def __init__(self, employee_id: int, name: str) -> None:
        self.employee_id = employee_id
        self.name = name

    def __repr__(self) -> str:
        return f"Employee({self.employee_id}, '{self.name}')"


def main() -> None:
    print("\n--- GENERIC DATA STORE USING PEP 695 ---")

    product_store: DataStore[Product] = DataStore()
    employee_store: DataStore[Employee] = DataStore()

    product_store.add(Product(101, "Laptop"))
    product_store.add(Product(102, "Keyboard"))

    employee_store.add(Employee(201, "Arun"))
    employee_store.add(Employee(202, "Priya"))

    print("Products:", product_store.get_all())
    print("Employees:", employee_store.get_all())


if __name__ == "__main__":
    main()
```

### Function and Class Explanation

| Function / Class | Purpose |
|---|---|
| `DataStore[T]` | Reusable generic container |
| `add()` | Adds an item to the store |
| `get_all()` | Returns all stored items |
| `Product` | Represents product data |
| `Employee` | Represents employee data |
| `main()` | Creates stores and displays results |

---

## 6. Input and Output

This implementation uses predefined objects instead of interactive input.

### Sample Output

```text
--- GENERIC DATA STORE USING PEP 695 ---
Products: [Product(101, 'Laptop'), Product(102, 'Keyboard')]
Employees: [Employee(201, 'Arun'), Employee(202, 'Priya')]
```

---

## 7. Complexity Comparison Table

| Operation | Time Complexity | Space Complexity |
|---|---:|---:|
| Create store | O(1) | O(1) |
| Add one item | O(1) amortized | O(1) auxiliary |
| Get all items | O(1) for returning the list reference | O(1) auxiliary |
| Store `n` items | O(n) | O(n) |

---

## Important Point

PEP 695 syntax requires a modern Python version that supports the new generic syntax. The code should be run using **Python 3.12 or later**.

---

## Conclusion

PEP 695 provides a concise and modern way to create generic classes. `DataStore[T]` allows one reusable container implementation to work with Product, Employee, and other data types while keeping the intended type information clear.
