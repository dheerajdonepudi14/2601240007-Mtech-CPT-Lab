# Merge Two Sorted Data Resources

## 1. Objective

To develop a Python program using the **Divide and Conquer** concept to merge two already sorted data resources into one sorted resource efficiently.

## 2. Real-World Problem

A company may maintain data in two separate systems, databases, or files. If both data resources are already sorted, they can be combined into a single sorted resource without sorting all the elements again.

The **Merge** step of Merge Sort uses this same idea. It compares the smallest remaining elements from both sorted resources and places the smaller element into the final resource.

## 3. Input

- Number of elements in the first data resource
- Elements of the first resource in increasing order
- Number of elements in the second data resource
- Elements of the second resource in increasing order

## 4. Output

The program displays:

- The final merged data resource
- All elements in increasing order

## 5. Algorithm

1. Set two pointers `i` and `j` to the first elements of the two sorted resources.
2. Compare `resource1[i]` and `resource2[j]`.
3. Add the smaller element to the merged resource.
4. Move the pointer of the resource from which the element was selected.
5. Repeat until one resource is completely processed.
6. Copy the remaining elements from the other resource.
7. Display the merged sorted resource.

## 6. Why This is Related to Divide and Conquer

Merge Sort follows the **Divide and Conquer** strategy:

- **Divide:** Split a large data resource into smaller parts.
- **Conquer:** Sort the smaller parts independently.
- **Combine:** Merge the sorted parts into one sorted resource.

This program demonstrates the **combine/merge step**, where two sorted resources are efficiently combined.

## 7. Time Complexity

If the first resource contains `n` elements and the second resource contains `m` elements:

- **Time Complexity: O(n + m)**

Every element from both resources is visited once.

## 8. Space Complexity

- **O(n + m)** auxiliary space is required for the merged resource.

## 9. Sample Test Case

Input:
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

Output:
```text
Merged sorted data: [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
```

## 10. Example Explanation

First resource:
```text
[10, 20, 30, 40, 50]
```

Second resource:
```text
[15, 25, 35, 45, 55]
```

The program compares the front elements:

```text
10 < 15  -> take 10
20 > 15  -> take 15
20 < 25  -> take 20
25 > 30  -> take 25
...
```

Finally:

```text
[10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
```

## 11. Important Point

Both input resources **must already be sorted** in increasing order. The program does not perform a separate sorting operation before merging.

## 12. Conclusion

Merging two sorted resources is an efficient operation because the program processes each element only once. This is the fundamental **combine step of the Divide and Conquer approach used in Merge Sort**, giving a time complexity of **O(n + m)**.
