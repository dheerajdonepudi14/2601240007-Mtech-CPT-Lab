# Maximum Subarray – Maximum Profit Streak

## 1. Objective

To develop a Python program using the **Maximum Subarray (Kadane's Algorithm)** to find the consecutive period that produces the maximum total profit.

## 2. Real-World Problem

A business records its daily profit or loss changes. Management wants to identify the consecutive period with the highest total gain. The Maximum Subarray algorithm can solve this efficiently.

## 3. Input

- Number of days
- Profit/loss change for each day

Positive values represent gains and negative values represent losses.

## 4. Output

The program displays:

- Starting day of the best period
- Ending day of the best period
- Maximum total profit
- Daily changes included in that period

## 5. Algorithm

1. Initialize the current sum and best sum with the first day's value.
2. For every next day, decide whether to:
   - Start a new subarray at the current day, or
   - Extend the existing subarray.
3. Update the best sum whenever a larger sum is found.
4. Track the starting and ending positions.
5. Display the maximum-profit consecutive period.

## 6. Time Complexity

- **O(n)**

Each daily value is processed only once.

## 7. Space Complexity

- **O(1)** auxiliary space apart from the input list.

## 8. Sample Test Case

Input:
```text
Enter number of days: 8
Enter profit/loss for day 1: -2
Enter profit/loss for day 2: 3
Enter profit/loss for day 3: -1
Enter profit/loss for day 4: 5
Enter profit/loss for day 5: -6
Enter profit/loss for day 6: 4
Enter profit/loss for day 7: 2
Enter profit/loss for day 8: -1
```

Output:
```text
Best period: Day 2 to Day 4
Maximum profit: Rs.7.00
Daily changes in best period:
3 -1 5
```
