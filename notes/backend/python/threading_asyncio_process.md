# Threading vs. Asyncio vs. Process

https://dev.to/coderatul/threading-vs-asyncio-vs-multiprocessing-10ed

## Threading
> gives an illusion of parallelism and not true parallelism due to Python's GIL(Global Interpreter Lock)
> even if we have multiple cores we can't achieve true parallelism

- python's GIL : is a mutex(mutual-exclusion) lock which makes sure that only one thread of a process can execute at a given time
- so under the hood a thread sheduler shedules the execution of threads (depending upon the os) by rapid context swicthing
- use threading in I/O bound tasks( I/O operations like waiting for network requests or reading files);
while a thread waits for I/O completion, other threads can be executed

## Asyncio
> is a python module for asynchronous programming

Leverages:
- Couroutines: 
    - These are special functions that can be paused and resumed later
    - They are the building blocks of asynchronous code in asyncio
    - Definition by: async and await keywords
- Event loops (manages tasks and schedules them for execution when resources become available (e.g., I/O completes):
    - Managing the execution of coroutines and handling events
    - This minimizes context switching and avoids blocking the main thread

- Threading: most of things are handled by OS
- Eventloop: handle by eventloop


