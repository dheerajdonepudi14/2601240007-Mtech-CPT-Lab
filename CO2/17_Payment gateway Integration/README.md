# Q17. Payment Gateway Integration — 8 Marks

## 1. Problem Statement

An application communicates with multiple payment gateways. Some gateways may not provide a particular API method. One developer checks for the method before calling it, while another attempts the operation directly and handles the exception.

### Questions

**(a)** Identify the two approaches as LBYL and EAFP. **[2]**  
**(b)** Implement the EAFP approach in Python. **[2]**  
**(c)** Explain when EAFP is preferable in Python. **[2]**  
**(d)** Give one situation where LBYL may be more appropriate. **[2]**

**Coverage Note:** EAFP, LBYL, exceptions and duck typing

---

## 2. Algorithm Identification

The problem compares two Python programming approaches for working with different payment gateway objects.

| Approach | Full Form | Basic Idea |
|---|---|---|
| **LBYL** | Look Before You Leap | Check whether the required method exists before calling it. |
| **EAFP** | Easier to Ask for Forgiveness than Permission | Attempt the operation directly and handle the exception if it fails. |
| **Duck Typing** | — | Python focuses on whether an object supports the required operation rather than its declared type. |

### Approach Used in This Program

The program implements **EAFP**.

Instead of checking whether `gateway` has a `pay()` method first, the program directly calls:

```python
gateway.pay(amount)
```

If the selected gateway does not provide `pay()`, Python raises an `AttributeError`, which is handled using `try-except`.

---

## 3. Step-by-Step Example

### Given Data

Suppose an application supports three gateways:

| Gateway | Available Method | Supports `pay()`? |
|---|---|---|
| GatewayA | `pay()` | Yes |
| GatewayB | `process_payment()` | No |
| GatewayC | `pay()` | Yes |

Assume the user selects **GatewayB** and enters a payment amount of **₹1500**.

### Step 1: Select Gateway

```text
Gateway choice = 2
Amount = ₹1500
```

The program creates a `GatewayB` object.

### Step 2: Directly Attempt the Operation

The EAFP function executes:

```python
gateway.pay(1500)
```

### Step 3: Exception Occurs

`GatewayB` does not contain a `pay()` method. Therefore, Python raises:

```text
AttributeError
```

### Step 4: Handle the Exception

The `except AttributeError` block executes and returns:

```text
Payment failed: this gateway does not provide the pay() API.
```

### Step 5: Successful Case

If the user selects GatewayA:

```python
GatewayA().pay(1500)
```

The operation succeeds because GatewayA provides the required `pay()` method.

### Trace Execution

| Step | Operation | Result |
|---|---|---|
| 1 | Select GatewayB | GatewayB object created |
| 2 | Call `gateway.pay(1500)` | Operation attempted directly |
| 3 | Python looks for `pay()` | Method not found |
| 4 | `AttributeError` raised | Exception caught |
| 5 | `except` block executes | Failure message displayed |

### Final Result

```text
Payment failed: this gateway does not provide the pay() API.
```

---

## 4. Algorithm

### EAFP Algorithm

1. Start the program.
2. Create different payment gateway objects.
3. Select a gateway based on user input.
4. Accept the payment amount.
5. Pass the gateway object and amount to the payment function.
6. Directly attempt to call `gateway.pay(amount)`.
7. If the gateway supports `pay()`, process the payment successfully.
8. If the gateway does not support `pay()`, Python raises `AttributeError`.
9. Catch the exception using `try-except`.
10. Display an appropriate failure message.
11. Stop the program.

### Why This Demonstrates EAFP

The key idea is:

> **Do the operation first; handle the failure if it happens.**

The program does **not** first ask:

```python
if hasattr(gateway, "pay"):
```

Instead, it attempts:

```python
gateway.pay(amount)
```

and handles the exception when the operation is unavailable.

### EAFP vs LBYL

#### LBYL

```python
if hasattr(gateway, "pay"):
    gateway.pay(amount)
else:
    print("Gateway does not support pay()")
```

The program checks first and then performs the operation.

#### EAFP

```python
try:
    gateway.pay(amount)
except AttributeError:
    print("Gateway does not support pay()")
```

The program performs the operation first and handles the failure.

---

## 5. Implementation

### Python Program

```python
# Q17. Payment Gateway Integration
# EAFP (Easier to Ask for Forgiveness than Permission)


class GatewayA:
    """Payment gateway that provides the pay() API."""

    def pay(self, amount):
        return f"GatewayA: Payment of ₹{amount:.2f} successful"


class GatewayB:
    """Payment gateway that uses a different API and has no pay() method."""

    def process_payment(self, amount):
        return f"GatewayB: Payment of ₹{amount:.2f} successful"


class GatewayC:
    """Payment gateway that provides the pay() API."""

    def pay(self, amount):
        return f"GatewayC: Payment of ₹{amount:.2f} successful"


def make_payment(gateway, amount):
    """Process payment using the EAFP approach.

    EAFP directly attempts the required operation and handles
    AttributeError if the gateway does not provide the pay() API.
    """
    try:
        return gateway.pay(amount)
    except AttributeError:
        return "Payment failed: this gateway does not provide the pay() API."


def main():
    print("\n--- PAYMENT GATEWAY INTEGRATION ---")
    print("1. GatewayA (supports pay())")
    print("2. GatewayB (does not support pay())")
    print("3. GatewayC (supports pay())")

    choice = int(input("Enter gateway choice: "))
    amount = float(input("Enter payment amount: ₹"))

    gateways = {
        1: GatewayA(),
        2: GatewayB(),
        3: GatewayC()
    }

    gateway = gateways.get(choice)

    if gateway is None:
        print("Invalid gateway choice.")
        return

    print(make_payment(gateway, amount))


if __name__ == "__main__":
    main()
```

### Function and Class Explanation

| Component | Purpose |
|---|---|
| `GatewayA` | Represents a gateway that supports the `pay()` method. |
| `GatewayB` | Represents a gateway with a different API, `process_payment()`. |
| `GatewayC` | Represents another gateway that supports `pay()`. |
| `make_payment()` | Implements the EAFP approach using `try-except`. |
| `main()` | Accepts user input, selects a gateway and displays the result. |
| `AttributeError` | Handles the case where `pay()` is not available. |

### Duck Typing in the Program

Python does not require all gateway classes to inherit from a common payment-gateway class.

The function:

```python
def make_payment(gateway, amount):
    gateway.pay(amount)
```

simply expects the object to provide the required operation. This is an example of **duck typing**.

If the object has a compatible `pay()` method, it works. If it does not, the exception is handled.

---

## 6. Input and Output

### Example 1 — Gateway Supports `pay()`

**Input:**

```text
--- PAYMENT GATEWAY INTEGRATION ---
1. GatewayA (supports pay())
2. GatewayB (does not support pay())
3. GatewayC (supports pay())
Enter gateway choice: 1
Enter payment amount: ₹2500
```

**Output:**

```text
GatewayA: Payment of ₹2500.00 successful
```

### Example 2 — Gateway Does Not Support `pay()`

**Input:**

```text
--- PAYMENT GATEWAY INTEGRATION ---
1. GatewayA (supports pay())
2. GatewayB (does not support pay())
3. GatewayC (supports pay())
Enter gateway choice: 2
Enter payment amount: ₹1500
```

**Output:**

```text
Payment failed: this gateway does not provide the pay() API.
```

---

## 7. Complexity Comparison Table

| Approach | Method Check | Operation | Exception Handling | Main Advantage |
|---|---|---|---|---|
| **LBYL** | Checks before operation | Performed after check | Usually not required for missing method | Useful when checking is cheap and important before the operation |
| **EAFP** | No explicit pre-check | Attempted directly | Uses `try-except` | Concise and natural for Python's duck-typed style |

### Time Complexity

For this program, the payment operation itself is treated as **O(1)** at the program level.

- Gateway selection using the dictionary is **O(1)** average time.
- Calling `pay()` is **O(1)** for this demonstration.
- Handling an `AttributeError` is treated as constant-time for the complexity discussion.

Therefore, the overall algorithm is approximately:

**Time Complexity: O(1)**

### Space Complexity

The program stores only a constant number of gateway objects and variables.

**Space Complexity: O(1)**

---

## 8. When EAFP Is Preferable in Python

EAFP is preferable when the operation itself is the most reliable way to determine whether an object can perform an action.

### Example 1 — File Operations

Instead of checking whether a file exists first:

```python
if os.path.exists("data.txt"):
    open("data.txt")
```

Python code can attempt the operation and handle the failure:

```python
try:
    with open("data.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
```

This avoids a separate check that may become outdated before the file is opened.

### Example 2 — Payment Gateway APIs

When several third-party gateway objects may expose different methods, the application can attempt the required operation and handle `AttributeError` when the API is unavailable.

This fits Python's dynamic and duck-typed programming style.

---

## 9. When LBYL May Be More Appropriate

LBYL can be more appropriate when checking a condition before performing an operation is important for program flow or when the check itself is the intended validation.

### Example — User Input Validation

Before performing a calculation involving a divisor, checking for zero can be clearer:

```python
if divisor != 0:
    result = number / divisor
else:
    print("Division by zero is not allowed")
```

Here the condition is simple, expected, and directly controls whether the operation should happen.

---

## 10. Important Points

1. **LBYL** means **Look Before You Leap**.
2. **EAFP** means **Easier to Ask for Forgiveness than Permission**.
3. EAFP attempts an operation first and handles the resulting exception.
4. In this program, `AttributeError` is used when the gateway does not provide `pay()`.
5. Python's **duck typing** allows objects to be used based on the operations they support rather than their declared type.
6. EAFP is commonly associated with Python's dynamic programming style.
7. LBYL can be useful when an explicit precondition check makes the code clearer or safer for the particular operation.
8. In real payment systems, gateway-specific errors should also be handled appropriately; this academic example focuses specifically on missing methods, as required by the question.

---

## Conclusion

The Payment Gateway Integration problem demonstrates the difference between **LBYL** and **EAFP** approaches in Python. The implemented solution follows **EAFP** by directly attempting to call the `pay()` method and catching `AttributeError` when a gateway does not provide that method. This also demonstrates **duck typing**, where the function works with objects based on the behavior they provide rather than requiring a common concrete type.

**Key Idea:**

```text
LBYL → Check first → Perform operation

EAFP → Perform operation → Handle exception if it fails
```
