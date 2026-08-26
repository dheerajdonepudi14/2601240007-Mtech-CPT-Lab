def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2

    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("\n--- STUDENT MARKS RANKING USING MERGE SORT ---")

    n = int(input("Enter number of students: "))
    students = []

    for i in range(n):
        name = input(f"Enter student {i + 1} name: ")
        marks = float(input(f"Enter marks for {name}: "))
        students.append((name, marks))

    sorted_students = merge_sort(students)

    print("\n--- RANKED STUDENTS ---")
    for rank, (name, marks) in enumerate(sorted_students, start=1):
        print(f"{rank}. {name} - {marks:g}")


if __name__ == "__main__":
    main()
