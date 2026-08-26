# Binary Search – University Library Book Lookup

## 1. Objective

To develop a Python program using the **Binary Search** algorithm to locate a book number in a university library's sorted book-number list.

## 2. Real-World Problem

A university library has a large collection of books arranged by increasing book number. Instead of checking every book one by one, Binary Search repeatedly divides the sorted list into two halves to locate the required book efficiently.

## 3. Input

- Number of books
- Book numbers in increasing order
- Book number to search

## 4. Output

The program displays:

- Whether the requested book exists
- Its position if found
- A message if the book is not available

## 5. Algorithm

1. Set `low` to the first index and `high` to the last index.
2. Find the middle index.
3. Compare the middle book number with the target.
4. If equal, return the position.
5. If the target is greater, search the right half.
6. If the target is smaller, search the left half.
7. Repeat until the book is found or the search range becomes empty.

## 6. Time Complexity

- Best case: **O(1)**
- Average case: **O(log n)**
- Worst case: **O(log n)**

## 7. Space Complexity

- **O(1)** auxiliary space because the search is iterative.

## 8. Sample Test Case

Input:
```text
Enter number of books: 5
Book number 1: 1001
Book number 2: 1005
Book number 3: 1010
Book number 4: 1015
Book number 5: 1020
Enter book number to search: 1015
```

Output:
```text
Book 1015 exists.
Position in sorted list: 4
```
