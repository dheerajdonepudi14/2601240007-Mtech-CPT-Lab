# Merge Two Sorted Data Resources


def merge_sorted_resources(resource1, resource2):
    i = 0
    j = 0
    merged = []

    while i < len(resource1) and j < len(resource2):
        if resource1[i] <= resource2[j]:
            merged.append(resource1[i])
            i += 1
        else:
            merged.append(resource2[j])
            j += 1

    while i < len(resource1):
        merged.append(resource1[i])
        i += 1

    while j < len(resource2):
        merged.append(resource2[j])
        j += 1

    return merged


def main():
    print("\n--- MERGE TWO SORTED DATA RESOURCES ---")

    n1 = int(input("Enter number of elements in first resource: "))
    resource1 = []
    print("Enter first resource elements in increasing order:")
    for i in range(n1):
        resource1.append(int(input(f"Resource 1 element {i + 1}: ")))

    n2 = int(input("Enter number of elements in second resource: "))
    resource2 = []
    print("Enter second resource elements in increasing order:")
    for i in range(n2):
        resource2.append(int(input(f"Resource 2 element {i + 1}: ")))

    merged = merge_sorted_resources(resource1, resource2)

    print("Merged sorted data:", merged)


if __name__ == "__main__":
    main()
