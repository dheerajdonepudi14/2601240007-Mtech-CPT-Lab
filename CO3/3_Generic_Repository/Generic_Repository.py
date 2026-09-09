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
