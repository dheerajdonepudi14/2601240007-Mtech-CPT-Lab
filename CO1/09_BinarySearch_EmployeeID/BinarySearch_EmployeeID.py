# Binary Search - Employee ID Lookup


def binary_search(employee_ids, target):
    low = 0
    high = len(employee_ids) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if employee_ids[mid] == target:
            return mid, comparisons
        elif employee_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def main():
    print("=" * 60)
    print("        COMPANY EMPLOYEE DATABASE - BINARY SEARCH")
    print("=" * 60)

    n = int(input("Enter number of employee IDs: "))

    employee_ids = []
    print("Enter employee IDs in increasing order:")
    for i in range(n):
        employee_id = int(input(f"Employee ID {i + 1}: "))
        employee_ids.append(employee_id)

    target = int(input("Enter employee ID to search: "))

    position, comparisons = binary_search(employee_ids, target)

    print("\n" + "-" * 60)
    if position != -1:
        print(f"Employee ID {target} exists.")
        print(f"Position in sorted database: {position + 1}")
        print(f"Comparisons performed: {comparisons}")
    else:
        print(f"Employee ID {target} does not exist.")
        print(f"Comparisons performed: {comparisons}")

    print("-" * 60)
    print("Divide-and-Conquer: Each comparison eliminates about half")
    print("of the remaining employee IDs from consideration.")
    print("Time Complexity: O(log n)")
    print("Space Complexity: O(1) auxiliary space")
    print("=" * 60)


if __name__ == "__main__":
    main()
