# Program 13 — Specification-First, Type-Driven and Test-First Development with AI

## 1. Problem Statement
Implement a Python program using specification-first, type-driven and test-first development with AI assistance.

## 2. Algorithm / Concept Identification
| Item | Details |
|---|---|
| Topic | Specification-first + type-driven + test-first |
| Application | User Service |
| Type system | Type hints and dataclass |
| AI role | Assist with implementation, tests and documentation |

## 3. Step-by-Step Example
1. Write the specification for creating and deactivating users.
2. Define typed User data.
3. Define expected test cases before implementation.
4. Implement the service.
5. Run tests and review AI-generated suggestions.
6. Refactor without violating the specification.

## 4. Procedure
- A user must have a unique integer ID.
- A user name cannot be empty.
- New users are active.
- A known user can be deactivated.
- Unknown users raise an error.
- Use types to make the contract explicit.

## 5. Implementation
~~~python
from dataclasses import dataclass
from typing import Dict


@dataclass
class User:
    user_id: int
    name: str
    active: bool = True


class UserService:
    def __init__(self) -> None:
        self.users: Dict[int, User] = {}

    def create_user(self, user_id: int, name: str) -> User:
        if user_id in self.users:
            raise ValueError("User ID already exists")
        if not name.strip():
            raise ValueError("Name cannot be empty")

        user = User(user_id, name.strip())
        self.users[user_id] = user
        return user

    def deactivate_user(self, user_id: int) -> None:
        if user_id not in self.users:
            raise KeyError("User not found")
        self.users[user_id].active = False

    def get_user(self, user_id: int) -> User:
        if user_id not in self.users:
            raise KeyError("User not found")
        return self.users[user_id]


def main() -> None:
    service = UserService()
    print("Created:", service.create_user(101, "Dheeraj"))
    service.deactivate_user(101)
    print("After deactivation:", service.get_user(101))
    print("Workflow: Specification -> Types -> Tests -> Implementation -> Refactoring")


if __name__ == "__main__":
    main()
~~~

## 6. Input and Output
**Input:** user ID `101`, name `Dheeraj`.

**Output:** the created active user followed by the same user with `active=False`.

## 7. Complexity
| Operation | Complexity |
|---|---|
| Create user | O(1) average |
| Get user | O(1) average |
| Deactivate user | O(1) average |
| Storage | O(n) |

## 8. Test-First Development
Tests should cover:
- Valid user creation.
- Duplicate ID rejection.
- Empty-name rejection.
- Successful deactivation.
- Unknown-user error.

## 9. Conclusion
The program demonstrates how specification, type contracts, tests, implementation and AI-assisted development can be combined into one repeatable workflow.
