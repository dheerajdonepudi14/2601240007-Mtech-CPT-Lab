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
