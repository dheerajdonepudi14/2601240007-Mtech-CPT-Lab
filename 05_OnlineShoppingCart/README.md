# Online Shopping Cart System

## 1. Objective

To develop a Python-based online shopping cart system that allows users to add and remove products, change quantities, apply discounts, and calculate the final bill including 18% GST.

## 2. Real-World Problem

An online store needs to maintain products selected by a customer and calculate the final payable amount after applying a discount and GST.

## 3. Input

- Menu choice
- Product name
- Product price
- Product quantity
- Discount percentage

## 4. Output

The program displays:

- Product-wise bill
- Subtotal
- Discount amount
- Amount after discount
- GST at 18%
- Final bill
- Appropriate messages for invalid products or choices

## 5. Algorithm

1. Create an empty shopping cart.
2. Display the shopping cart menu.
3. Add products with name, price, and quantity.
4. Remove a product by searching its name.
5. Change the quantity of an existing product.
6. Store the discount percentage.
7. Calculate each product's total:
   `Product Total = Price × Quantity`
8. Calculate subtotal.
9. Calculate discount amount.
10. Calculate GST on the discounted amount.
11. Calculate the final bill.
12. Repeat until Exit is selected.

## 6. Time Complexity

- Add Product: **O(1)**
- Remove Product: **O(n)**
- Change Quantity: **O(n)**
- Apply Discount: **O(1)**
- Display Bill: **O(n)**
- Overall worst-case menu operation: **O(n)**

## 7. Space Complexity

- **O(n)** for storing cart products.

## 8. Sample Calculation

For a subtotal of Rs.1000 and a 10% discount:

```text
Discount = Rs.100
Amount After Discount = Rs.900
GST = Rs.162
Final Bill = Rs.1062
```
