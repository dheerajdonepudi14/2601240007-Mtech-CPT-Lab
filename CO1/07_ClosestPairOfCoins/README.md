# Closest Pair of Coins – Coin Tray Detection

## 1. Objective

To develop a Python program that identifies the **closest pair of coins** placed on a two-dimensional tray.

## 2. Real-World Problem

Consider a coin-sorting machine or automated tray where the position of each coin is represented by `(x, y)` coordinates. The system needs to determine which two coins are closest to each other.

This demonstrates the real-world application of the **Closest Pair** computational problem.

## 3. Input

- Number of coins
- `(x, y)` coordinates of every coin

## 4. Output

The program displays:

- Coordinates of the closest two coins
- Minimum distance between them

## 5. Algorithm

This implementation uses the straightforward pair-comparison approach:

1. Read the coordinates of all coins.
2. Compare every coin with every other coin exactly once.
3. Calculate Euclidean distance:
   `d = √((x2-x1)² + (y2-y1)²)`
4. Keep track of the smallest distance.
5. Display the pair having the minimum distance.

## 6. Time Complexity

- **O(n²)** because every possible pair is checked.

## 7. Space Complexity

- **O(n)** for storing the coin coordinates.

## 8. Sample Test Case

Input:
```text
Enter number of coins: 4
Enter coordinates for coin 1 (x y): 1 1
Enter coordinates for coin 2 (x y): 5 5
Enter coordinates for coin 3 (x y): 2 2
Enter coordinates for coin 4 (x y): 9 9
```

Output:
```text
Coin 1: (1, 1)
Coin 2: (2, 2)
Minimum distance: 1.41 units
```

## 9. Note

The standard optimized divide-and-conquer Closest Pair algorithm can achieve **O(n log n)**, but this version uses the direct pair-comparison method because it is simple, transparent, and suitable for demonstrating the core problem.
