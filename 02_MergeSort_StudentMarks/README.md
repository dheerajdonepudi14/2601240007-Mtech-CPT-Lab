# Merge Sort – Student Marks Ranking

## 1. Objective

To develop a Python program using the **Merge Sort** algorithm to arrange students in descending order of marks.

## 2. Real-World Problem

A university wants to generate a merit list from student marks. Merge Sort divides the student list into smaller parts, sorts them, and merges the sorted parts to produce the final ranking.

## 3. Input

- Number of students
- Student name
- Student marks

## 4. Output

The program displays students in descending order of marks along with their rank.

## 5. Algorithm

1. Divide the student list into two halves.
2. Recursively divide each half until single-element lists remain.
3. Compare marks while merging the smaller lists.
4. Place the student with higher marks first.
5. Continue until the complete ranked list is produced.

## 6. Time Complexity

- Best case: **O(n log n)**
- Average case: **O(n log n)**
- Worst case: **O(n log n)**

## 7. Space Complexity

- **O(n)** for the temporary lists used during merging.

## 8. Sample Test Case

Input:
```text
Enter number of students: 5
Enter student 1 name: Anitha
Enter marks for Anitha: 95
Enter student 2 name: Vivek
Enter marks for Vivek: 83
Enter student 3 name: Lakshmi
Enter marks for Lakshmi: 67
Enter student 4 name: Ramesh
Enter marks for Ramesh: 97
Enter student 5 name: Kumar
Enter marks for Kumar: 85
```

Output:
```text
1. Ramesh - 97
2. Anitha - 95
3. Kumar - 85
4. Vivek - 83
5. Lakshmi - 67
```
