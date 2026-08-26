def quick_sort(orders, low, high):
    if low < high:
        pivot_index = partition(orders, low, high)
        quick_sort(orders, low, pivot_index - 1)
        quick_sort(orders, pivot_index + 1, high)


def partition(orders, low, high):
    pivot = orders[high]["distance"]
    i = low - 1

    for j in range(low, high):
        if orders[j]["distance"] <= pivot:
            i += 1
            orders[i], orders[j] = orders[j], orders[i]

    orders[i + 1], orders[high] = orders[high], orders[i + 1]
    return i + 1


def main():
    print("\n--- DELIVERY ORDER ROUTE PRIORITY ---")

    n = int(input("Enter number of delivery orders: "))

    if n <= 0:
        print("Number of orders must be greater than zero.")
        return

    orders = []

    for i in range(n):
        order_id = input(f"Enter order ID {i + 1}: ").strip()
        distance = float(input(f"Enter delivery distance for {order_id} (km): "))

        if distance < 0:
            print("Distance cannot be negative.")
            return

        orders.append({
            "id": order_id,
            "distance": distance
        })

    quick_sort(orders, 0, len(orders) - 1)

    print("\n--- ORDERS SORTED BY DELIVERY DISTANCE ---")
    for order in orders:
        print(f"Order {order['id']} - {order['distance']:g} km")


if __name__ == "__main__":
    main()
