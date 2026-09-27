# Program 6 — Dataclass vs Traditional Class

## 1. Problem Statement

Implement a Student/Employee data model using dataclasses and compare it with a traditional class implementation.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 6 |
| Topic | Dataclass vs Traditional Class |
| Main concept | Dataclass vs Traditional Class |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** A Student dataclass automatically supplies initialization and representation. A traditional class requires explicit method definitions when the same behavior is wanted.

### Working

1. Accept or define the required data.
2. Apply the concept specified in the exercise.
3. Validate important conditions and edge cases.
4. Display the result and relevant analysis.
5. Use the stated complexity/tooling/testing information where applicable.

## 4. Algorithm / Procedure

1. Start the Python program.
2. Prepare the required input or sample data.
3. Execute the main operation for the selected concept.
4. Handle invalid or exceptional conditions where appropriate.
5. Display the result.
6. Verify the behavior using the relevant complexity, testing, typing, concurrency or development workflow.

## 5. Implementation

~~~python
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
~~~

## 6. Input and Output

### Sample Input

The exact input depends on the program. Use the prompts displayed by the Python program.

### Sample Output

The program prints the calculated result and/or demonstration of the requested concept.

## 7. Complexity / Engineering Analysis

| Aspect | Analysis |
|---|---|
| Primary operation | Depends on the program's algorithm or workflow |
| Space | Depends on stored data, recursion, buffers or generated objects |
| Verification | Output, tests, type checking or timing as appropriate |

### Program-specific Notes

Dataclass construction is concise because common methods are generated automatically. The traditional class requires explicit boilerplate.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Dataclass vs Traditional Class** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
