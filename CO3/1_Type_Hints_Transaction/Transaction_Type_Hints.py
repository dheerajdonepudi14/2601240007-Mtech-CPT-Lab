# 1. PEP 484-Style Type Hints for Banking Transactions


def process_transaction(account_number: str, amount: float, transaction_type: str) -> str:
    if amount <= 0:
        return "Transaction amount must be greater than 0."

    if transaction_type not in ("deposit", "withdraw"):
        return "Invalid transaction type."

    return (
        f"Transaction successful: {transaction_type.title()} of "
        f"₹{amount:.2f} for account {account_number}."
    )


def main() -> None:
    print("\n--- BANKING TRANSACTION PROCESSING ---")

    account_number: str = input("Enter account number: ")
    amount: float = float(input("Enter transaction amount: ₹"))
    transaction_type: str = input("Enter transaction type (deposit/withdraw): ").lower()

    result: str = process_transaction(account_number, amount, transaction_type)
    print(result)


if __name__ == "__main__":
    main()
