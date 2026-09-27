# Program 11 — Specification-First Development with AI Assistance

## 1. Problem Statement
Develop a Python application using GitHub Copilot, Cursor or Claude Code with specification-first development and document how AI assistance is used.

## 2. Algorithm / Concept Identification
| Item | Details |
|---|---|
| Topic | Specification-first development |
| Application | Task Manager |
| Main concepts | Dataclass, type hints, requirements-first workflow |
| AI role | Generate suggestions, documentation and implementation drafts |

## 3. Step-by-Step Example
1. Specify the required Task Manager behavior.
2. Define the Task data model.
3. Implement typed methods.
4. Use an AI coding assistant for suggestions.
5. Review every generated change against the specification.
6. Run the application and tests.

## 4. Procedure
- Requirement: a task has an ID, title and completion state.
- Requirement: tasks can be added and completed.
- Type the data model and service methods.
- Validate AI-generated code manually.
- Test the final behavior.

## 5. Implementation
~~~python
from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    task_id: int
    title: str
    completed: bool = False


class TaskManager:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, title: str) -> Task:
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                return
        raise ValueError("Task not found")

    def list_tasks(self) -> List[Task]:
        return self.tasks


def main() -> None:
    manager = TaskManager()
    manager.add_task("Write specification")
    manager.add_task("Implement feature")
    manager.complete_task(1)

    for task in manager.list_tasks():
        status = "DONE" if task.completed else "PENDING"
        print(f"{task.task_id}. {task.title} - {status}")


if __name__ == "__main__":
    main()
~~~

## 6. Input and Output
**Example operations:** add two tasks and complete task 1.

**Output:**
~~~text
1. Write specification - DONE
2. Implement feature - PENDING
~~~

## 7. Complexity
| Operation | Complexity |
|---|---|
| Add task | O(1) amortized |
| Complete task | O(n) |
| List tasks | O(n) |

## 8. AI Assistance Documentation
AI can help draft code, tests and documentation, but the developer verifies requirements, security, correctness and edge cases before accepting changes.

## 9. Conclusion
The implementation demonstrates a specification-first workflow where AI assists development without replacing human review.
