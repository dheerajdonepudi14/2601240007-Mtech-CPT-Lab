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
