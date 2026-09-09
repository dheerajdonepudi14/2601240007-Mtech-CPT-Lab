# 2. PEP 604 Union Type Syntax for Contact Information


def display_contact(contact: str | int) -> str:
    if isinstance(contact, int):
        return f"Primary contact is mobile number: {contact}"
    return f"Primary contact is email address: {contact}"


def main() -> None:
    print("\n--- CUSTOMER PRIMARY CONTACT ---")
    print("1. Mobile Number")
    print("2. Email Address")

    choice: int = int(input("Enter your choice (1/2): "))

    if choice == 1:
        mobile: int = int(input("Enter mobile number: "))
        contact: str | int = mobile
    elif choice == 2:
        email: str = input("Enter email address: ")
        contact = email
    else:
        print("Invalid choice.")
        return

    print(display_contact(contact))


if __name__ == "__main__":
    main()
