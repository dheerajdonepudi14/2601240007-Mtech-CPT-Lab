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
