# Car Parking Management System

## 1. Objective

To develop a Python-based car parking management system for **100 parking slots** that can allocate slots, release vehicles, display parking availability, and calculate parking charges.

## 2. Real-World Problem

A parking facility needs to know which vehicles occupy which slots and how much each vehicle should pay when leaving. The program maintains this information using a Python dictionary.

## 3. Input

- Menu choice
- Vehicle number
- Parking duration in hours

## 4. Output

The program displays:

- Allocated parking slot
- Occupied and available slots
- Parked vehicle details
- Parking bill
- Total parking charge
- Appropriate messages for a full parking area or unavailable vehicle

## 5. Algorithm

1. Set the total number of slots to 100.
2. Create an empty dictionary for parked vehicles.
3. Display the menu.
4. For parking, check whether space is available.
5. Assign the next free slot to the vehicle.
6. For release, search for the vehicle number.
7. Calculate the charge using:
   `Parking Charge = Hours × Hourly Rate`
8. Remove the vehicle from the parking dictionary.
9. Display parking status when requested.
10. Repeat until Exit is selected.

## 6. Time Complexity

- Park vehicle: **O(n)** in the worst case when locating a free slot
- Release vehicle: **O(1)** average dictionary lookup
- Display status: **O(n)**
- Exit: **O(1)**

## 7. Space Complexity

- **O(n)** for stored parked vehicles.

## 8. Default Configuration

- Total parking slots: **100**
- Hourly parking rate: **Rs.50**

## 9. Sample Test Case

Input:
```text
1
AP39AB1234
3
3
2
AP39AB1234
4
```

Expected result includes:
```text
Vehicle AP39AB1234 parked successfully in slot 1.
Available Slots : 99
Total Charge   : Rs.150.00
```
