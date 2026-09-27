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
