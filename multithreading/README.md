# Multithreading: Parallelize
This is an example of how parallelize multiple jobs (functions), limited to the number of available cores at a time, and how to automatically join a [thread][thread] when it finishes.
It makes use of [mutexes][mutex] and [condition variables][condvar].
The mutex is primarily used to prevent thread completion during spawns and joins.
The condition variable is used to determine when the main thread must join on a finished thread.

[Pthreads][pthreads] is the threading API used.


[condvar]: https://en.wikipedia.org/wiki/Monitor_(synchronization)
[mutex]: https://en.wikipedia.org/wiki/Mutual_exclusion
[pthreads]: https://en.wikipedia.org/wiki/POSIX_Threads
[thread]: https://en.wikipedia.org/wiki/Thread_(computing)
