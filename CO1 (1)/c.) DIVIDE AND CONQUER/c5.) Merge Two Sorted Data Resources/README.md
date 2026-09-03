# c5.) Merge Two Sorted Data Resources

## 1. Problem Statement

In many real-world systems, data may be maintained in two separate resources such as files, databases, logs, or records. If both resources are already sorted in increasing order, they need to be combined into one sorted resource efficiently.

**Problem:** Merge two already sorted data resources into a single sorted resource without performing a separate sorting operation on all the elements.

The problem can be solved efficiently using the **Merge** operation, which is the **Combine** step of the Divide and Conquer strategy used in Merge Sort.

---

## 2. Algorithm Identification

This problem falls under the **Divide and Conquer** paradigm, specifically the **Merge / Combine** operation.

| **Attribute** | **Merge Two Sorted Resources** |
| ------------------------------------------- | ---------------------------------------------- |
| **Definition** | Combines two already sorted resources into one sorted resource. |
| **Approach** | Compare the current elements of both resources and select the smaller one. |
| **Time Complexity** | **O(n + m)** |
| **Auxiliary Space** | **O(n + m)** |
| **Useful for** | Combining sorted files, database records, logs, arrays, and intermediate results. |
| **Chosen** | Two-pointer Merge Technique |

---

## 3. Step-by-Step Example

### Given Data

| **Item** | **Value** |
| -------------------------------- | -------------------------------- |
| Number of elements in Resource 1 | **n = 5** |
| Resource 1 | `[10, 20, 30, 40, 50]` |
| Number of elements in Resource 2 | **m = 5** |
| Resource 2 | `[15, 25, 35, 45, 55]` |
| Order | Increasing |

### Initial Pointers

```text
Resource 1: [10, 20, 30, 40, 50]
              ^
              i

Resource 2: [15, 25, 35, 45, 55]
              ^
              j

Merged: []
```

### Trace Execution

| **Step** | **Resource 1 Element** | **Resource 2 Element** | **Comparison** | **Selected Element** | **Merged Resource** |
| -------- | ---------------------- | ----------------------- | -------------- | -------------------- | ------------------- |
| 1 | 10 | 15 | `10 <= 15` | 10 | `[10]` |
| 2 | 20 | 15 | `20 > 15` | 15 | `[10, 15]` |
| 3 | 20 | 25 | `20 <= 25` | 20 | `[10, 15, 20]` |
| 4 | 30 | 25 | `30 > 25` | 25 | `[10, 15, 20, 25]` |
| 5 | 30 | 35 | `30 <= 35` | 30 | `[10, 15, 20, 25, 30]` |
| 6 | 40 | 35 | `40 > 35` | 35 | `[10, 15, 20, 25, 30, 35]` |
| 7 | 40 | 45 | `40 <= 45` | 40 | `[10, 15, 20, 25, 30, 35, 40]` |
| 8 | 50 | 45 | `50 > 45` | 45 | `[10, 15, 20, 25, 30, 35, 40, 45]` |
| 9 | 50 | 55 | `50 <= 55` | 50 | `[10, 15, 20, 25, 30, 35, 40, 45, 50]` |
| 10 | Empty | 55 | Resource 1 exhausted | 55 | `[10, 15, 20, 25, 30, 35, 40, 45, 50, 55]` |

### Final Result

```text
Resource 1 = [10, 20, 30, 40, 50]
Resource 2 = [15, 25, 35, 45, 55]

Merged Resource = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
```

---

## 4. Algorithm

### Merge Two Sorted Data Resources Algorithm

1. **Input**: Two sorted resources `resource1` and `resource2`.
2. Initialize two pointers `i = 0` and `j = 0`.
3. Create an empty list `merged` to store the final sorted resource.
4. Compare `resource1[i]` and `resource2[j]`.
5. If `resource1[i] <= resource2[j]`, append `resource1[i]` to `merged` and increment `i`.
6. Otherwise, append `resource2[j]` to `merged` and increment `j`.
7. Repeat steps 4–6 while both resources still contain unprocessed elements.
8. If elements remain in `resource1`, append all remaining elements to `merged`.
9. If elements remain in `resource2`, append all remaining elements to `merged`.
10. Return the final merged sorted resource.

### Why This is Related to Divide and Conquer

Merge Sort follows the **Divide and Conquer** strategy:

- **Divide:** Split a large data resource into smaller parts.
- **Conquer:** Sort the smaller parts independently.
- **Combine:** Merge the sorted parts into one sorted resource.

This program directly demonstrates the **Combine / Merge step**. The two input resources are assumed to have already been sorted, so the program only performs the efficient merging operation.

### Important Observation

The program does **not** compare every element with every other element. Each pointer only moves forward, so every element is processed once.

For example:

```text
Resource 1: [10, 20, 30]
Resource 2: [15, 25, 35]

10 vs 15 -> take 10
20 vs 15 -> take 15
20 vs 25 -> take 20
30 vs 25 -> take 25
30 vs 35 -> take 30
Resource 1 exhausted -> take remaining 35
```

Final result:

```text
[10, 15, 20, 25, 30, 35]
```

---

## 5. Implementation

```python
# Merge Two Sorted Data Resources


def merge_sorted_resources(resource1, resource2):
    i = 0
    j = 0
    merged = []

    while i < len(resource1) and j < len(resource2):
        if resource1[i] <= resource2[j]:
            merged.append(resource1[i])
            i += 1
        else:
            merged.append(resource2[j])
            j += 1

    while i < len(resource1):
        merged.append(resource1[i])
        i += 1

    while j < len(resource2):
        merged.append(resource2[j])
        j += 1

    return merged


def main():
    print("\n--- MERGE TWO SORTED DATA RESOURCES ---")

    n1 = int(input("Enter number of elements in first resource: "))
    resource1 = []
    print("Enter first resource elements in increasing order:")
    for i in range(n1):
        resource1.append(int(input(f"Resource 1 element {i + 1}: ")))

    n2 = int(input("Enter number of elements in second resource: "))
    resource2 = []
    print("Enter second resource elements in increasing order:")
    for i in range(n2):
        resource2.append(int(input(f"Resource 2 element {i + 1}: ")))

    merged = merge_sorted_resources(resource1, resource2)

    print("Merged sorted data:", merged)


if __name__ == "__main__":
    main()
```

### Function Explanation

| **Function / Part** | **Purpose** |
| -------------------------------- | ---------------------------------------------- |
| `merge_sorted_resources()` | Performs the actual merging operation. |
| `i` | Pointer for the first sorted resource. |
| `j` | Pointer for the second sorted resource. |
| `merged` | Stores the final sorted resource. |
| `while i < len(resource1) and j < len(resource2)` | Compares elements while both resources have remaining elements. |
| First remaining-elements loop | Copies remaining elements from Resource 1. |
| Second remaining-elements loop | Copies remaining elements from Resource 2. |
| `main()` | Reads input, calls the merge function, and displays output. |

---

## 6. Input and Output

### Input

The program accepts:

- Number of elements in the first resource.
- Elements of the first resource in increasing order.
- Number of elements in the second resource.
- Elements of the second resource in increasing order.

### Sample Input

```text
--- MERGE TWO SORTED DATA RESOURCES ---
Enter number of elements in first resource: 5
Enter first resource elements in increasing order:
Resource 1 element 1: 10
Resource 1 element 2: 20
Resource 1 element 3: 30
Resource 1 element 4: 40
Resource 1 element 5: 50
Enter number of elements in second resource: 5
Enter second resource elements in increasing order:
Resource 2 element 1: 15
Resource 2 element 2: 25
Resource 2 element 3: 35
Resource 2 element 4: 45
Resource 2 element 5: 55
```

### Execution Output

```text
Merged sorted data: [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
```

### Complexity Comparison Table

If the first resource contains `n` elements and the second resource contains `m` elements:

| **Feature / Metric** | **Merge Two Sorted Resources** |
| -------------------------------- | -------------------------------- |
| **Data Structure** | Python `list` |
| **Best-case Complexity** | `O(n + m)` |
| **Average Complexity** | **`O(n + m)`** |
| **Worst-case Complexity** | **`O(n + m)`** |
| **Auxiliary Space Complexity** | **`O(n + m)`** |
| **Number of Pointer Movements** | At most `n + m` |
| **Sorting Before Merge** | Not required |
| **Best Suited For** | Combining two already sorted datasets |

### Complexity Explanation

**Time Complexity: `O(n + m)`**

Every element from both resources is processed exactly once. Therefore, for `n` elements in the first resource and `m` elements in the second resource, the total work is proportional to `n + m`.

**Space Complexity: `O(n + m)`**

The `merged` list stores all elements from both input resources, so it requires space proportional to the total number of elements.

### Important Point

Both input resources **must already be sorted in increasing order**. If the resources are not sorted, this merge algorithm cannot guarantee a sorted result.

### Conclusion

Merging two sorted data resources is an efficient operation because each element is processed only once. It is the fundamental **Combine step of the Divide and Conquer approach used in Merge Sort**, with **O(n + m)** time complexity and **O(n + m)** auxiliary space for the resulting merged resource.
