# Program 5 — Banking Management System — Inheritance and Abstraction

## 1. Problem Statement

Develop a Banking Management System demonstrating inheritance and abstraction with full type hints.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 5 |
| Topic | Banking Management System — Inheritance and Abstraction |
| Main concept | Banking Management System — Inheritance and Abstraction |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** A SavingsAccount and CurrentAccount inherit common account data and deposit behavior from Account while implementing their own withdrawal rules.

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
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number: str, holder: str, balance: float = 0.0) -> None:
        self.account_number: str = account_number
        self.holder: str = holder
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def account_type(self) -> str:
        pass


class SavingsAccount(Account):
    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal")
        self.balance -= amount

    def account_type(self) -> str:
        return "Savings Account"


class CurrentAccount(Account):
    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance + 1000:
            raise ValueError("Withdrawal exceeds allowed limit")
        self.balance -= amount

    def account_type(self) -> str:
        return "Current Account"


def show_account(account: Account) -> None:
    print(f"{account.account_type()}: {account.account_number}")
    print(f"Holder: {account.holder}")
    print(f"Balance: {account.balance:.2f}")


def main() -> None:
    savings: Account = SavingsAccount("S001", "Ravi", 5000.0)
    current: Account = CurrentAccount("C001", "Priya", 3000.0)

    savings.deposit(1000.0)
    savings.withdraw(1500.0)
    current.withdraw(3500.0)

    show_account(savings)
    print()
    show_account(current)


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

The design uses OOP abstraction and inheritance. Individual deposit/withdraw operations are O(1), excluding external storage.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Banking Management System — Inheritance and Abstraction** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
