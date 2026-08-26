def binary_search(books, target):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2

        if books[mid] == target:
            return mid
        elif books[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    print("\n--- UNIVERSITY LIBRARY BOOK LOOKUP ---")

    n = int(input("Enter number of books: "))
    books = []

    print("Enter book numbers in increasing order:")
    for i in range(n):
        books.append(int(input(f"Book number {i + 1}: ")))

    target = int(input("Enter book number to search: "))

    position = binary_search(books, target)

    if position != -1:
        print(f"Book {target} exists.")
        print(f"Position in sorted list: {position + 1}")
    else:
        print(f"Book {target} does not exist.")


if __name__ == "__main__":
    main()
