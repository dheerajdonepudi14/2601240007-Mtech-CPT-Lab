# Binary Search – Company Employee ID Lookup

## 1. Objective

To develop a Python program using **Binary Search** to locate an employee ID in a company's sorted employee database and explain how Binary Search applies the **Divide-and-Conquer** technique.

## 2. Real-World Problem

A company has a sorted database containing **millions of employee IDs**. When HR or an internal system needs to check whether a particular employee ID exists, checking every ID one by one would be inefficient.

Binary Search solves this problem by repeatedly dividing the search range into two halves. After every comparison, one half of the database can be discarded because the employee IDs are already sorted.

For example, if the database contains **1,000,000 employee IDs**, Binary Search needs at most about **20 comparisons** in the worst case because:

$$
\log_2(1,000,000) \approx 19.93
$$

This is the key advantage of Divide-and-Conquer.

## 3. Divide-and-Conquer Approach

Binary Search follows three basic ideas:

1. **Divide** – Find the middle employee ID of the current search range.
2. **Conquer** – Compare the middle ID with the target and keep only the half that can contain the target.
3. **Repeat** – Continue dividing the remaining range until the target is found or no elements remain.

### Example

Suppose the sorted employee database is:

`[1001, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040]`

Target employee ID: **1035**

| Step | Search Range | Middle ID | Decision |
|---|---|---:|---|
| 1 | 1001 – 1040 | 1020 | 1035 > 1020 → search right half |
| 2 | 1025 – 1040 | 1030 | 1035 > 1030 → search right half |
| 3 | 1035 – 1040 | 1035 | Match found |

Instead of checking all 9 IDs, only **3 comparisons** are required.

## 4. Input

- Number of employees
- Employee IDs in increasing/sorted order
- Employee ID to search

## 5. Output

The program displays:

- Whether the employee ID exists
- Its position if found
- Number of comparisons performed
- Time and space complexity

## 6. Algorithm

1. Set `low` to the first index.
2. Set `high` to the last index.
3. Find the middle index using:
   `mid = (low + high) // 2`
4. Compare `employee_ids[mid]` with the target employee ID.
5. If they are equal, the employee ID is found.
6. If the target is greater than the middle ID, discard the left half and set `low = mid + 1`.
7. If the target is smaller than the middle ID, discard the right half and set `high = mid - 1`.
8. Repeat until the employee ID is found or `low > high`.

## 7. Why Binary Search is Divide-and-Conquer

The important operation is that every comparison removes approximately **half of the remaining search space**.

If there are `n` employee IDs:

- After 1 comparison → `n / 2` remain
- After 2 comparisons → `n / 4` remain
- After 3 comparisons → `n / 8` remain
- After `k` comparisons → `n / 2^k` remain

The search stops when only one possible element remains:

$$
\frac{n}{2^k} = 1
$$

Therefore:

$$
2^k = n
$$

Taking logarithm on both sides:

$$
k = \log_2 n
$$

So the time complexity is:

$$
\boxed{O(\log n)}
$$

## 8. Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| **Best Case** | **O(1)** | Target is found at the first middle comparison. |
| **Average Case** | **O(log n)** | The search repeatedly reduces the range by half. |
| **Worst Case** | **O(log n)** | The maximum number of divisions is logarithmic. |

### Space Complexity

The implementation is iterative, so it uses:

**O(1) auxiliary space**

No additional array or recursive call stack is required.

## 9. Implementation

```python
# Binary Search - Employee ID Lookup


def binary_search(employee_ids, target):
    low = 0
    high = len(employee_ids) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if employee_ids[mid] == target:
            return mid, comparisons
        elif employee_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def main():
    print("=" * 60)
    print("        COMPANY EMPLOYEE DATABASE - BINARY SEARCH")
    print("=" * 60)

    n = int(input("Enter number of employee IDs: "))

    employee_ids = []
    print("Enter employee IDs in increasing order:")
    for i in range(n):
        employee_id = int(input(f"Employee ID {i + 1}: "))
        employee_ids.append(employee_id)

    target = int(input("Enter employee ID to search: "))

    position, comparisons = binary_search(employee_ids, target)

    print("\n" + "-" * 60)
    if position != -1:
        print(f"Employee ID {target} exists.")
        print(f"Position in sorted database: {position + 1}")
        print(f"Comparisons performed: {comparisons}")
    else:
        print(f"Employee ID {target} does not exist.")
        print(f"Comparisons performed: {comparisons}")

    print("-" * 60)
    print("Divide-and-Conquer: Each comparison eliminates about half")
    print("of the remaining employee IDs from consideration.")
    print("Time Complexity: O(log n)")
    print("Space Complexity: O(1) auxiliary space")
    print("=" * 60)


if __name__ == "__main__":
    main()
```

## 10. Sample Test Case – Employee Found

### Input

```text
Enter number of employee IDs: 9
Enter employee IDs in increasing order:
Employee ID 1: 1001
Employee ID 2: 1005
Employee ID 3: 1010
Employee ID 4: 1015
Employee ID 5: 1020
Employee ID 6: 1025
Employee ID 7: 1030
Employee ID 8: 1035
Employee ID 9: 1040
Enter employee ID to search: 1035
```

### Output

```text
------------------------------------------------------------
Employee ID 1035 exists.
Position in sorted database: 8
Comparisons performed: 3
------------------------------------------------------------
Divide-and-Conquer: Each comparison eliminates about half
of the remaining employee IDs from consideration.
Time Complexity: O(log n)
Space Complexity: O(1) auxiliary space
------------------------------------------------------------
```

## 11. Sample Test Case – Employee Not Found

### Input

```text
Enter number of employee IDs: 9
Enter employee IDs in increasing order:
Employee ID 1: 1001
Employee ID 2: 1005
Employee ID 3: 1010
Employee ID 4: 1015
Employee ID 5: 1020
Employee ID 6: 1025
Employee ID 7: 1030
Employee ID 8: 1035
Employee ID 9: 1040
Enter employee ID to search: 1037
```

### Output

```text
------------------------------------------------------------
Employee ID 1037 does not exist.
Comparisons performed: 4
------------------------------------------------------------
Divide-and-Conquer: Each comparison eliminates about half
of the remaining employee IDs from consideration.
Time Complexity: O(log n)
Space Complexity: O(1) auxiliary space
------------------------------------------------------------
```

## 12. Large Database Analysis

Consider a company database with **1,000,000 employee IDs**.

### Linear Search

In the worst case, the system may check all 1,000,000 IDs:

$$
O(n) = O(1,000,000)
$$

### Binary Search

Binary Search repeatedly halves the search range:

$$
\log_2(1,000,000) \approx 19.93
$$

Therefore, at most about **20 comparisons** are required.

This shows why Binary Search is suitable for very large **sorted** databases.

## 13. Important Requirement

Binary Search works correctly only when the employee IDs are **sorted** according to the value being searched.

If the employee database is unsorted, Binary Search cannot simply be applied. The data must first be sorted, or another search technique should be considered.

## 14. Conclusion

Binary Search is an efficient **Divide-and-Conquer** searching algorithm for a sorted employee database.

It repeatedly divides the search space into two halves and eliminates the half that cannot contain the target. Because the search space is reduced by half after every comparison, its worst-case time complexity is:

$$
\boxed{O(\log n)}
$$

For millions of employee IDs, this is dramatically more efficient than checking every employee ID sequentially with Linear Search.
