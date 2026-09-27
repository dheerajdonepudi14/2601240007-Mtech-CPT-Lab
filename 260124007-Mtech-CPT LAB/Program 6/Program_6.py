from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    name: str
    course: str


@dataclass
class Employee:
    employee_id: int
    name: str
    department: str


class TraditionalStudent:
    def __init__(self, student_id: int, name: str, course: str) -> None:
        self.student_id = student_id
        self.name = name
        self.course = course

    def __repr__(self) -> str:
        return (
            f"TraditionalStudent(student_id={self.student_id}, "
            f"name='{self.name}', course='{self.course}')"
        )


def main() -> None:
    student = Student(101, "Arun", "Cyber Security")
    employee = Employee(501, "Meena", "Security Operations")
    traditional = TraditionalStudent(102, "Kiran", "Computer Science")

    print("Dataclass Student:", student)
    print("Dataclass Employee:", employee)
    print("Traditional Student:", traditional)

    print("\nDataclasses automatically provide useful methods such as __init__ and __repr__.")
    print("Traditional classes require these methods to be written manually when needed.")


if __name__ == "__main__":
    main()
