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
