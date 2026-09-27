# Program 3 — Reusable Stack and Queue — Type Hints and Dataclasses

## 1. Problem Statement

Develop a reusable Python package implementing Stack and Queue using type hints and dataclasses.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 3 |
| Topic | Reusable Stack and Queue — Type Hints and Dataclasses |
| Main concept | Reusable Stack and Queue — Type Hints and Dataclasses |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** Stack receives 10 and 20, then pop returns 20. Queue receives A and B, then dequeue returns A.

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

Stack push/pop/peek are O(1) with the list end. Queue dequeue using list.pop(0) is O(n); collections.deque would provide O(1) dequeuing.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Reusable Stack and Queue — Type Hints and Dataclasses** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
