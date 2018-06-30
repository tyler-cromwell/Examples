# Multithreading
This is an example of how to regulate the number of active [threads][thread] based on the number of [CPU cores][multicore].
The program will ensure that a thread is spawned for every core.
When one finishes, it spawns another until all of a specified number of threads have executed.
It makes use of [mutexes][mutex] and [condition variables][condvar] (also called Monitors).
The mutex is primarily used to prevent thread completion during spawns and joins.
The condition variable is used to determine when the main thread must join on a finished thread.
Because multiple threads may finish before the main thread can join them all, an array is used to implement a simple [queue] of all threads that finished execution.
[Pthreads][pthreads] are the threading implementation used.


[condvar]: https://en.wikipedia.org/wiki/Monitor_(synchronization)
[multicore]: https://en.wikipedia.org/wiki/Multi-core_processor
[mutex]: https://en.wikipedia.org/wiki/Mutual_exclusion
[pthreads]: https://en.wikipedia.org/wiki/POSIX_Threads
[queue]: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
[thread]: https://en.wikipedia.org/wiki/Thread_(computing)
