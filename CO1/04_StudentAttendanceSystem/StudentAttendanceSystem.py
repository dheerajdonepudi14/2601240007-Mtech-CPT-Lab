def main():
    print("\n--- STUDENT ATTENDANCE ANALYSIS ---")

    n = int(input("Enter number of students: "))

    if n <= 0:
        print("Number of students must be greater than zero.")
        return

    total_classes = int(input("Enter total classes conducted: "))

    if total_classes <= 0:
        print("Total classes must be greater than zero.")
        return

    students = []

    for i in range(n):
        name = input(f"Enter student {i + 1} name: ").strip()
        attended = int(input(f"Enter classes attended by {name}: "))

        if attended < 0 or attended > total_classes:
            print("Invalid attendance. Enter a value between 0 and total classes.")
            return

        percentage = (attended / total_classes) * 100
        students.append({
            "name": name,
            "attended": attended,
            "percentage": percentage
        })

    print("\n--- ATTENDANCE REPORT ---")

    total_percentage = 0
    below_75 = []

    for student in students:
        percentage = student["percentage"]
        total_percentage += percentage

        status = "Eligible" if percentage >= 75 else "Below 75%"
        print(
            f"{student['name']}: "
            f"{percentage:.2f}% - {status}"
        )

        if percentage < 75:
            below_75.append(student["name"])

    highest = max(students, key=lambda student: student["percentage"])
    average = total_percentage / n

    print(f"\nHighest Attendance: {highest['name']} ({highest['percentage']:.2f}%)")
    print(f"Class Average Attendance: {average:.2f}%")

    print("\nStudents Below 75%:")
    if below_75:
        for name in below_75:
            print(f"- {name}")
    else:
        print("None")


if __name__ == "__main__":
    main()
