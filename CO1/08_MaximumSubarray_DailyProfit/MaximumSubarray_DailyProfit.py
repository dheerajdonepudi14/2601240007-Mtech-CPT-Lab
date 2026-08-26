def maximum_subarray(changes):
    current_sum = changes[0]
    best_sum = changes[0]

    current_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(changes)):
        if changes[i] > current_sum + changes[i]:
            current_sum = changes[i]
            current_start = i
        else:
            current_sum += changes[i]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = i

    return best_sum, best_start, best_end


def main():
    print("\n--- MAXIMUM PROFIT STREAK ---")
    print("Enter daily profit/loss changes.")

    n = int(input("Enter number of days: "))

    if n <= 0:
        print("Number of days must be greater than zero.")
        return

    changes = []

    for i in range(n):
        value = float(input(f"Enter profit/loss for day {i + 1}: "))
        changes.append(value)

    best_sum, start, end = maximum_subarray(changes)

    print("\n--- RESULT ---")
    print(f"Best period: Day {start + 1} to Day {end + 1}")
    print(f"Maximum profit: Rs.{best_sum:.2f}")

    print("Daily changes in best period:")
    print(" ".join(f"{value:g}" for value in changes[start:end + 1]))


if __name__ == "__main__":
    main()
