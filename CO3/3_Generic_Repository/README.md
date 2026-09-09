# 3. Generic Repository for Customer, Product and Employee

## 1. Problem Statement

An enterprise application needs repositories for different objects such as **Customer, Product, and Employee**. The same repository logic should be reused. Apply **generic types** to create a reusable repository.

The program creates one generic `Repository[T]` class and reuses it for different object types.

---

## 2. Algorithm Identification

| Item | Description |
|---|---|
| Concept | Generic Types |
| Generic Variable | `T` |
| Generic Class | `Repository[T]` |
| Purpose | Reuse the same repository logic for different object types |
| Supported Objects | Customer, Product, Employee |

### Generic Type Used

```python
T = TypeVar("T")

class Repository(Generic[T]):
```

The same class can then be specialized as:

```python
Repository[Customer]
Repository[Product]
Repository[Employee]
```

---

## 3. Step-by-Step Example

### Given Data

| Repository | Object | Example Value |
|---|---|---|
| `customer_repo` | Customer | `Customer(101, 'Arun')` |
| `product_repo` | Product | `Product(201, 'Laptop')` |
| `employee_repo` | Employee | `Employee(301, 'Priya')` |

### Execution

1. Define a generic type variable `T`.
2. Create the reusable `Repository[T]` class.
3. Store items in a list of type `T`.
4. Create a customer repository.
5. Create a product repository.
6. Create an employee repository.
7. Add objects to their respective repositories.
8. Retrieve all objects using the same `get_all()` method.

### Result

```text
Customers: [Customer(101, 'Arun')]
Products: [Product(201, 'Laptop')]
Employees: [Employee(301, 'Priya')]
```

### Second Example

A `Repository[Product]` can store multiple products using exactly the same `add()` and `get_all()` logic used by `Repository[Customer]`.

---

## 4. Algorithm

1. Start the program.
2. Import `Generic` and `TypeVar`.
3. Define a type variable `T`.
4. Create `Repository(Generic[T])`.
5. Initialize an empty list for repository items.
6. Define `add(item: T)` to insert an object.
7. Define `get_all() -> list[T]` to retrieve objects.
8. Create repositories for Customer, Product, and Employee.
9. Add the corresponding objects.
10. Display all stored objects.
11. Stop.

### Why Generics Are Used

Without generics, separate repository classes could be written for each entity. Generics allow one reusable repository implementation while preserving the intended item type in the type annotation.

---

## 5. Implementation

```python
# 3. Generic Repository for Customer, Product and Employee

from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items


class Customer:
    def __init__(self, customer_id: int, name: str) -> None:
        self.customer_id = customer_id
        self.name = name

    def __repr__(self) -> str:
        return f"Customer({self.customer_id}, '{self.name}')"


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
    print("\n--- GENERIC REPOSITORY ---")

    customer_repo: Repository[Customer] = Repository()
    product_repo: Repository[Product] = Repository()
    employee_repo: Repository[Employee] = Repository()

    customer_repo.add(Customer(101, "Arun"))
    product_repo.add(Product(201, "Laptop"))
    employee_repo.add(Employee(301, "Priya"))

    print("Customers:", customer_repo.get_all())
    print("Products:", product_repo.get_all())
    print("Employees:", employee_repo.get_all())


if __name__ == "__main__":
    main()
```

### Function and Class Explanation

| Function / Class | Purpose |
|---|---|
| `Repository[T]` | Reusable generic repository |
| `TypeVar("T")` | Represents an arbitrary object type |
| `add()` | Adds an object to the repository |
| `get_all()` | Returns all stored objects |
| `Customer` | Represents a customer entity |
| `Product` | Represents a product entity |
| `Employee` | Represents an employee entity |

---

## 6. Input and Output

This implementation uses predefined objects instead of interactive input.

### Sample Data

```text
Customer(101, 'Arun')
Product(201, 'Laptop')
Employee(301, 'Priya')
```

### Sample Output

```text
--- GENERIC REPOSITORY ---
Customers: [Customer(101, 'Arun')]
Products: [Product(201, 'Laptop')]
Employees: [Employee(301, 'Priya')]
```

---

## 7. Complexity Comparison Table

| Operation | Time Complexity | Space Complexity |
|---|---:|---:|
| Create repository | O(1) | O(1) |
| `add()` | O(1) amortized | O(1) auxiliary |
| `get_all()` | O(1) for returning the list reference | O(1) auxiliary |
| Overall for `n` stored objects | O(n) to create/add all objects | O(n) |

---

## Important Point

Generics mainly provide **static type information and reusable design**. They do not create separate runtime implementations of `Repository` for Customer, Product, and Employee.

---

## Conclusion

A generic repository eliminates repeated repository logic. `Repository[T]` can be reused for Customer, Product, Employee, and other entity types while providing clear type information to developers and static type-checking tools.
