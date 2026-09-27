from dataclasses import dataclass, field
from typing import Generic, TypeVar, List

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: List[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]


@dataclass
class Queue(Generic[T]):
    items: List[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items[0]


def main() -> None:
    stack: Stack[int] = Stack()
    stack.push(10)
    stack.push(20)
    print("Stack:", stack.items)
    print("Stack pop:", stack.pop())

    queue: Queue[str] = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    print("Queue:", queue.items)
    print("Queue dequeue:", queue.dequeue())


if __name__ == "__main__":
    main()
