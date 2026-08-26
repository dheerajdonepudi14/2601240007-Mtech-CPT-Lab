# Quick Sort – Delivery Order Distance Management

## 1. Objective

To develop a Python program using the **Quick Sort** algorithm to arrange delivery orders in ascending order of delivery distance.

## 2. Real-World Problem

A delivery company wants to organize orders based on delivery distance so that nearby deliveries can be reviewed first. Quick Sort is used to sort the order distances efficiently.

## 3. Input

- Number of delivery orders
- Order ID
- Delivery distance in kilometres

## 4. Output

The program displays delivery orders sorted by distance in ascending order.

## 5. Algorithm

1. Select the last element as the pivot.
2. Compare every element with the pivot.
3. Move elements smaller than or equal to the pivot to the left.
4. Place the pivot in its correct position.
5. Recursively apply Quick Sort to the left and right partitions.
6. Display the sorted delivery orders.

## 6. Time Complexity

- Best case: **O(n log n)**
- Average case: **O(n log n)**
- Worst case: **O(n²)**

## 7. Space Complexity

- Average recursion space: **O(log n)**
- Worst-case recursion space: **O(n)**

## 8. Sample Test Case

Input:
```text
Enter number of delivery orders: 5
Enter order ID 1: ORD101
Enter delivery distance for ORD101 (km): 8
Enter order ID 2: ORD102
Enter delivery distance for ORD102 (km): 3
Enter order ID 3: ORD103
Enter delivery distance for ORD103 (km): 12
Enter order ID 4: ORD104
Enter delivery distance for ORD104 (km): 2
Enter order ID 5: ORD105
Enter delivery distance for ORD105 (km): 6
```

Output:
```text
Order ORD104 - 2 km
Order ORD102 - 3 km
Order ORD105 - 6 km
Order ORD101 - 8 km
Order ORD103 - 12 km
```
