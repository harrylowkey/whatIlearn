---
title: "Python Concurrency Implementation"
description: "Python Concurrency Implementation"
tags:
  - python
  - concurrency
  - parallelism
---
## How many ways to implement concurrency in Python?

Implementing concurrency in Python can be done in several ways depending on the task at hand and the level of concurrency required. Here are the main approaches:

### 1. **Threading**
The `threading` module is used for creating and working with threads. Threads are lighter than processes and are useful for I/O-bound tasks.

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### 2. **Multiprocessing**
The `multiprocessing` module allows you to create processes. Processes are separate memory spaces and are useful for CPU-bound tasks.

```python
import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_letters)

process1.start()
process2.start()

process1.join()
process2.join()
```

### 3. **Asyncio**
The `asyncio` module is used for asynchronous programming and is useful for I/O-bound tasks, particularly when dealing with network operations.
`asyncio` is a framework for writing single-threaded, concurrent code using the async and await keywords.
It does not inherently use multiple threads. Instead, it uses an event loop to manage asynchronous operations within a single thread.

*Note*: when handling blocking I/O operations, use `threading` or `multiprocessing` instead if handler not support asynchronous I/O like boto3

```python
import asyncio

async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in 'abcde':
        print(letter)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1
    await task2

asyncio.run(main())
```

### 4. **Concurrent.Futures**
The `concurrent.futures` module provides a high-level interface for asynchronously executing callables using threads or processes.

#### Using ThreadPoolExecutor: (use threading pool behind the scenes)
```python
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

with ThreadPoolExecutor() as executor:
    executor.submit(print_numbers)
    executor.submit(print_letters)
```

#### Using ProcessPoolExecutor: (use multiprocessing pool behind the scenes)
```python
from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

with ProcessPoolExecutor() as executor:
    executor.submit(print_numbers)
    executor.submit(print_letters)
```

Each method has its own use cases, strengths, and weaknesses. Threading is suitable for I/O-bound tasks, multiprocessing for CPU-bound tasks, asyncio for managing a large number of network connections, and concurrent.futures for a higher-level interface for threading and multiprocessing.


### Combining `asyncio` with Threads
While `asyncio` itself does not use threads for running tasks, you can run blocking code in a separate thread using `loop.run_in_executor`. This is useful for offloading blocking I/O operations to a thread pool while keeping the event loop responsive.

```python
import asyncio
import concurrent.futures
import time

def blocking_io():
    time.sleep(3)
    print("Blocking I/O finished")

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, blocking_io)
        print("Continued with other tasks while blocking I/O runs in the background")

asyncio.run(main())
```

In this example, `blocking_io` is a blocking function that runs in a separate thread, allowing the event loop to continue executing other tasks.

### Key Points
- `asyncio` uses an event loop to manage asynchronous tasks in a single thread.
- `asyncio` does not use multiple threads for its event loop and task management.
- You can use `loop.run_in_executor` to run blocking code in a separate thread or process.

In summary, `asyncio` is designed for concurrency within a single thread using an event loop, but it provides mechanisms to integrate with threading or multiprocessing when necessary.

## When to use threading, multiprocessing, or asyncio?

- Use **multiprocessing** for CPU-bound tasks
- Use **threading** for I/O-bound tasks
- Use **asyncio** for supported asynchronous I/O-bound tasks

### [?] Let take an example of uploading files to s3 storage, we have 2 options:
We have two options:

- Using threading
- Using asyncio

Which one is suitable for this use case?

- **Solution 1**: If you are using a synchronous library like boto3, you should go with threading.
This approach spawns other threads to handle uploading files, which can block I/O in these spawned threads but not the main thread.
- **Solution 2**: If you are using an asynchronous library like aioboto3, you can go with asyncio to achieve non-blocking I/O operations.
- **Solution 3**: If you need to use asyncio with boto3, you can combine threading using loop.run_in_executor to keep the event loop responsive.

### Let's take some examples to understand

**Case 1**: Using aysyncio with boto3
```
[Main Thread (asyncio Event Loop)]
     |
     |--- Upload File 1 (blocking) ---|
     |                               |
     |--- Upload File 2 (waiting) ---|
     |                               |
     |--- Upload File 3 (waiting) ---|
```
Even using asyncio with boto3, we still face blocking.

---

**Case 2**: Using threading with boto3
```
[Main Thread]
   |--> [Thread 1] --- Upload File 1 --- (blocked)
   |--> [Thread 2] --- Upload File 2 --- (blocked)
   |--> [Thread 3] --- Upload File 3 --- (blocked)
```
Let's the blocking I/O in other threads instead of main thread

---

**Case 3**: Using asyncio with boto3 and thread pool

```
[Main Thread (asyncio Event Loop)]
     |                                     
     |--- Upload File 1 (in thread pool) ---|
     |                                      |
     |--- Upload File 2 (in thread pool) ---|
     |                                      |
     |--- Upload File 3 (in thread pool) ---|

```

If you need to use asyncio with boto3, you can combine threading using loop.run_in_executor to keep the event loop responsive.
