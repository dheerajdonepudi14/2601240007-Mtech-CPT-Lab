# Student Attendance Analysis System

## 1. Objective

To develop a Python-based attendance analysis system that calculates attendance percentages, identifies students below 75%, finds the student with the highest attendance, and calculates the class average.

## 2. Real-World Problem

Faculty members need a quick way to analyze student attendance and identify students who may not satisfy the minimum attendance requirement.

## 3. Input

- Number of students
- Total classes conducted
- Student name
- Classes attended by each student

## 4. Output

The program displays:

- Individual attendance percentage
- Attendance eligibility
- Student with the highest attendance
- Class average attendance
- Students below 75% attendance

## 5. Algorithm

1. Read the number of students and total classes.
2. Read each student's name and attended classes.
3. Calculate:
   `Attendance % = (Classes Attended / Total Classes) × 100`
4. Mark students below 75%.
5. Find the student with the highest attendance.
6. Calculate the average attendance.
7. Display the complete attendance report.

## 6. Time Complexity

- Reading students: **O(n)**
- Attendance analysis: **O(n)**
- Highest attendance: **O(n)**
- Overall: **O(n)**

## 7. Space Complexity

- **O(n)** for storing student attendance records.

## 8. Sample Test Case

Input:
```text
Enter number of students: 3
Enter total classes conducted: 40
Enter student 1 name: Anitha
Enter classes attended by Anitha: 38
Enter student 2 name: Vivek
Enter classes attended by Vivek: 30
Enter student 3 name: Lakshmi
Enter classes attended by Lakshmi: 25
```

Output:
```text
Anitha: 95.00% - Eligible
Vivek: 75.00% - Eligible
Lakshmi: 62.50% - Below 75%
```
