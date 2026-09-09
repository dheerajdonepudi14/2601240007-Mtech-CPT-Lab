# 1. PEP 484-Style Type Hints for Banking Transactions

## 1. Problem Statement

A banking system processes transactions. Developers want static type checking to reduce errors. Apply **PEP 484-style type hints** to the transaction function.

The program accepts an account number, transaction amount, and transaction type. Type hints are used to clearly specify the expected input and return types.

---

## 2. Algorithm Identification

| Item | Description |
|---|---|
| Concept | PEP 484-style Type Hints |
| Purpose | Improve code readability and support static type checking |
| Input Types | `str`, `float`, `str` |
| Return Type | `str` |
| Main Function | `process_transaction()` |

### Type Hints Used

```python
def process_transaction(account_number: str, amount: float, transaction_type: str) -> str:
```

- `account_number: str` → account number must be a string.
- `amount: float` → transaction amount is a floating-point value.
- `transaction_type: str` → transaction type is a string.
- `-> str` → the function returns a string.

---

## 3. Step-by-Step Example

### Given Data

| Variable | Value | Type |
|---|---|---|
| Account Number | `ACC1001` | `str` |
| Amount | `5000.0` | `float` |
| Transaction Type | `deposit` | `str` |

### Execution

1. The account number is received as a string.
2. The amount is received as a floating-point number.
3. The transaction type is received as a string.
4. The function checks whether the amount is positive.
5. The function checks whether the transaction type is `deposit` or `withdraw`.
6. A success message is returned as a string.

### Result

```text
Transaction successful: Deposit of ₹5000.00 for account ACC1001.
```

### Second Example

If the amount is `-100`, the function returns:

```text
Transaction amount must be greater than 0.
```

---

## 4. Algorithm

1. Start the program.
2. Define `process_transaction()` using PEP 484-style type hints.
3. Accept `account_number` as `str`.
4. Accept `amount` as `float`.
5. Accept `transaction_type` as `str`.
6. Validate the transaction amount.
7. Validate the transaction type.
8. Return a transaction result as `str`.
9. Display the result.
10. Stop.

### Why Type Hints Are Useful

Type hints do not perform runtime type checking by themselves. Instead, tools such as static type checkers can detect incompatible types before the program is executed.

---

## 5. Implementation

```python
# 1. PEP 484-Style Type Hints for Banking Transactions

from typing import Union


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
```

### Function Explanation

| Function / Variable | Purpose |
|---|---|
| `process_transaction()` | Processes a banking transaction |
| `account_number: str` | Stores account number |
| `amount: float` | Stores transaction amount |
| `transaction_type: str` | Stores deposit/withdraw operation |
| `-> str` | Specifies that the function returns a string |
| `main() -> None` | Handles user input and output |

---

## 6. Input and Output

### Sample Input

```text
--- BANKING TRANSACTION PROCESSING ---
Enter account number: ACC1001
Enter transaction amount: ₹5000
Enter transaction type (deposit/withdraw): deposit
```

### Sample Output

```text
Transaction successful: Deposit of ₹5000.00 for account ACC1001.
```

### Invalid Input Example

```text
Enter account number: ACC1001
Enter transaction amount: ₹-100
Enter transaction type (deposit/withdraw): deposit
```

Output:

```text
Transaction amount must be greater than 0.
```

---

## 7. Complexity Comparison Table

| Operation | Time Complexity | Space Complexity |
|---|---:|---:|
| Amount validation | O(1) | O(1) |
| Transaction type validation | O(1) | O(1) |
| Result generation | O(1) | O(1) |
| Overall | **O(1)** | **O(1)** |

---

## Conclusion

PEP 484-style type hints make the banking transaction function clearer and easier to analyze with static type-checking tools. They document the expected types of parameters and the return value, helping developers detect potential type-related errors earlier.
