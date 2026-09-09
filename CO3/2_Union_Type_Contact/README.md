# 2. PEP 604 Union Type Syntax for Contact Information

## 1. Problem Statement

A customer may provide either a mobile number or an email address as the primary contact. Apply the **PEP 604 union type syntax** to model the contact information.

The program uses the modern `str | int` syntax to represent a value that can be either a string email address or an integer mobile number.

---

## 2. Algorithm Identification

| Item | Description |
|---|---|
| Concept | PEP 604 Union Type Syntax |
| Syntax | `str | int` |
| Purpose | Represent multiple possible types without `Union[]` |
| Possible Contact Types | `str` or `int` |
| Main Function | `display_contact()` |

### Union Type Used

```python
def display_contact(contact: str | int) -> str:
```

This means `contact` can contain either a `str` or an `int`.

---

## 3. Step-by-Step Example

### Example 1: Mobile Number

| Variable | Value | Type |
|---|---|---|
| `contact` | `9876543210` | `int` |

Execution:

1. The customer selects mobile number.
2. The mobile number is stored as an integer.
3. The value is passed to `display_contact()`.
4. `isinstance()` identifies it as an integer.
5. The mobile contact message is returned.

Result:

```text
Primary contact is mobile number: 9876543210
```

### Example 2: Email Address

| Variable | Value | Type |
|---|---|---|
| `contact` | `customer@example.com` | `str` |

Result:

```text
Primary contact is email address: customer@example.com
```

---

## 4. Algorithm

1. Start the program.
2. Define `display_contact(contact: str | int)`.
3. Display options for mobile number and email address.
4. Read the customer's choice.
5. If the choice is mobile, store the number as `int`.
6. If the choice is email, store the address as `str`.
7. Pass the value to `display_contact()`.
8. Identify the actual type using `isinstance()`.
9. Display the appropriate contact information.
10. Stop.

### Why PEP 604 Is Used

PEP 604 provides a concise union syntax. Instead of writing:

```python
Union[str, int]
```

the program can write:

```python
str | int
```

---

## 5. Implementation

```python
# 2. PEP 604 Union Type Syntax for Contact Information


def display_contact(contact: str | int) -> str:
    if isinstance(contact, int):
        return f"Primary contact is mobile number: {contact}"
    return f"Primary contact is email address: {contact}"


def main() -> None:
    print("\n--- CUSTOMER PRIMARY CONTACT ---")
    print("1. Mobile Number")
    print("2. Email Address")

    choice: int = int(input("Enter your choice (1/2): "))

    if choice == 1:
        mobile: int = int(input("Enter mobile number: "))
        contact: str | int = mobile
    elif choice == 2:
        email: str = input("Enter email address: ")
        contact = email
    else:
        print("Invalid choice.")
        return

    print(display_contact(contact))


if __name__ == "__main__":
    main()
```

### Function Explanation

| Function / Variable | Purpose |
|---|---|
| `display_contact()` | Displays the primary contact |
| `contact: str | int` | Allows string or integer contact values |
| `isinstance()` | Determines the runtime type |
| `main() -> None` | Handles input and output |

---

## 6. Input and Output

### Sample Input 1

```text
--- CUSTOMER PRIMARY CONTACT ---
1. Mobile Number
2. Email Address
Enter your choice (1/2): 1
Enter mobile number: 9876543210
```

### Sample Output 1

```text
Primary contact is mobile number: 9876543210
```

### Sample Input 2

```text
--- CUSTOMER PRIMARY CONTACT ---
1. Mobile Number
2. Email Address
Enter your choice (1/2): 2
Enter email address: customer@example.com
```

### Sample Output 2

```text
Primary contact is email address: customer@example.com
```

---

## 7. Complexity Comparison Table

| Operation | Time Complexity | Space Complexity |
|---|---:|---:|
| Type checking | O(1) | O(1) |
| Contact display | O(1) | O(1) |
| Overall | **O(1)** | **O(1)** |

---

## Important Point

PEP 604 union syntax is available in modern Python versions. It makes type annotations shorter and easier to read.

---

## Conclusion

PEP 604 union types provide a simple way to model data that can have more than one type. Here, the customer's primary contact can be represented using `str | int`, making the intended data model clear and concise.
