GST_RATE = 0.18

cart = []
discount = 0.0


def add_product():
    product = input("Enter product name: ").strip()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if not product or price < 0 or quantity <= 0:
        print("Invalid product details.")
        return

    cart.append([product, price, quantity])
    print("Product added to cart.")


def remove_product():
    product = input("Enter product name to remove: ").strip()

    for item in cart:
        if item[0].lower() == product.lower():
            cart.remove(item)
            print("Product removed from cart.")
            return

    print("Product not found.")


def change_quantity():
    product = input("Enter product name: ").strip()

    for item in cart:
        if item[0].lower() == product.lower():
            quantity = int(input("Enter new quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

            item[2] = quantity
            print("Quantity updated successfully.")
            return

    print("Product not found.")


def apply_discount():
    global discount

    discount = float(input("Enter discount percentage: "))

    if discount < 0 or discount > 100:
        print("Discount must be between 0 and 100.")
        discount = 0.0
        return

    print(f"{discount:g}% discount applied.")


def display_bill():
    if not cart:
        print("Cart is empty.")
        return

    subtotal = 0.0

    print("\n--- PRODUCT BILL ---")
    for product, price, quantity in cart:
        total = price * quantity
        subtotal += total
        print(
            f"{product}: "
            f"Rs.{price:.2f} x {quantity} = Rs.{total:.2f}"
        )

    discount_amount = subtotal * (discount / 100)
    amount_after_discount = subtotal - discount_amount
    gst = amount_after_discount * GST_RATE
    final_bill = amount_after_discount + gst

    print(f"\nSubtotal              : Rs.{subtotal:.2f}")
    print(f"Discount ({discount:g}%)      : Rs.{discount_amount:.2f}")
    print(f"Amount After Discount : Rs.{amount_after_discount:.2f}")
    print(f"GST (18%)             : Rs.{gst:.2f}")
    print(f"Final Bill            : Rs.{final_bill:.2f}")


def main():
    while True:
        print("\n--- ONLINE SHOPPING CART ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Change Quantity")
        print("4. Apply Discount")
        print("5. Display Bill")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue

        if choice == 1:
            add_product()
        elif choice == 2:
            remove_product()
        elif choice == 3:
            change_quantity()
        elif choice == 4:
            apply_discount()
        elif choice == 5:
            display_bill()
        elif choice == 6:
            print("Thank you for shopping.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
