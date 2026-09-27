# Program 7 — Producer-Consumer — Threading and Multiprocessing

## 1. Problem Statement

Develop a Producer-Consumer application using threading, multiprocessing and synchronization primitives.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 7 |
| Topic | Producer-Consumer — Threading and Multiprocessing |
| Main concept | Producer-Consumer — Threading and Multiprocessing |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** A producer places numbered items into a bounded buffer and a consumer removes them. The program demonstrates both threads and processes.

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
import multiprocessing as mp
import queue
import threading
import time
from typing import Any


def thread_producer(buffer: queue.Queue[Any], count: int) -> None:
    for value in range(1, count + 1):
        buffer.put(value)
        print(f"Thread producer -> {value}")
        time.sleep(0.05)
    buffer.put(None)


def thread_consumer(buffer: queue.Queue[Any]) -> None:
    while True:
        value = buffer.get()
        if value is None:
            buffer.task_done()
            break
        print(f"Thread consumer <- {value}")
        buffer.task_done()


def run_threading(count: int) -> None:
    buffer: queue.Queue[Any] = queue.Queue(maxsize=3)

    producer = threading.Thread(target=thread_producer, args=(buffer, count))
    consumer = threading.Thread(target=thread_consumer, args=(buffer,))

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()


def process_worker(shared_queue: Any, count: int) -> None:
    for value in range(1, count + 1):
        shared_queue.put(value)
    shared_queue.put(None)


def run_multiprocessing(count: int) -> None:
    shared_queue: Any = mp.Queue(maxsize=3)

    producer = mp.Process(target=process_worker, args=(shared_queue, count))
    producer.start()

    while True:
        value = shared_queue.get()
        if value is None:
            break
        print(f"Process consumer <- {value}")

    producer.join()


def main() -> None:
    count = int(input("Enter number of items: "))

    print("\n--- Threading Producer-Consumer ---")
    run_threading(count)

    print("\n--- Multiprocessing Producer-Consumer ---")
    run_multiprocessing(count)


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

Threading shares memory and uses Queue for synchronization. Multiprocessing uses separate processes and an inter-process Queue.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Producer-Consumer — Threading and Multiprocessing** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
