TOTAL_SLOTS = 100
HOURLY_RATE = 50

parking = {}


def get_free_slot():
    occupied_slots = {details["slot"] for details in parking.values()}

    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in occupied_slots:
            return slot

    return None


def park_vehicle():
    if len(parking) >= TOTAL_SLOTS:
        print("Parking is full.")
        return

    vehicle = input("Enter vehicle number: ").strip().upper()

    if vehicle in parking:
        print("Vehicle is already parked.")
        return

    hours = float(input("Enter parking duration in hours: "))

    if hours <= 0:
        print("Parking duration must be greater than zero.")
        return

    slot = get_free_slot()

    if slot is None:
        print("Parking is full.")
        return

    parking[vehicle] = {
        "slot": slot,
        "hours": hours
    }

    print(f"Vehicle {vehicle} parked successfully in slot {slot}.")


def release_vehicle():
    vehicle = input("Enter vehicle number to release: ").strip().upper()

    if vehicle not in parking:
        print("Vehicle not found.")
        return

    details = parking.pop(vehicle)
    charge = details["hours"] * HOURLY_RATE

    print("\n--- PARKING BILL ---")
    print(f"Vehicle Number : {vehicle}")
    print(f"Slot Number    : {details['slot']}")
    print(f"Parking Hours  : {details['hours']:g}")
    print(f"Rate per Hour  : Rs.{HOURLY_RATE:.2f}")
    print(f"Total Charge   : Rs.{charge:.2f}")


def display_status():
    print("\n--- PARKING STATUS ---")
    print(f"Total Slots     : {TOTAL_SLOTS}")
    print(f"Occupied Slots  : {len(parking)}")
    print(f"Available Slots : {TOTAL_SLOTS - len(parking)}")

    if parking:
        print("\nParked Vehicles:")
        for vehicle, details in parking.items():
            print(
                f"Vehicle: {vehicle}, "
                f"Slot: {details['slot']}, "
                f"Hours: {details['hours']:g}"
            )
    else:
        print("No vehicles are currently parked.")


def main():
    while True:
        print("\n--- CAR PARKING SYSTEM ---")
        print("1. Park Vehicle")
        print("2. Release Vehicle")
        print("3. Display Parking Status")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue

        if choice == 1:
            park_vehicle()
        elif choice == 2:
            release_vehicle()
        elif choice == 3:
            display_status()
        elif choice == 4:
            print("Thank you for using the Car Parking System.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
