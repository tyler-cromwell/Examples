# Dynamic Programming
The included are examples of how to apply [Dynamic Programming][dynamprog] to solve a computationally complex problem.
In this example, the problem is computing the Nth [Fibonacci Number][fibo].
This task has a [Time Complexity][time] of `O(2^n)` where `n` is the Nth number.
What makes this problem so complex is that in order to compute the Nth fibonacci number, the previous two numbers must first be computed.
Because of this, lower numbers are encountered and computed multiple times.
Dynamic programming aims to solve this by caching the values of numbers when they are computed so they do not need to be recomputed later.
The two dynamic programming solutions are `memoization.py` and `tabulation.py`.
`naive.py` isn't a dynamic programming solution, it is just a "brute force" one.


[dynamprog]: https://en.wikipedia.org/wiki/Dynamic_programming
[fibo]: https://en.wikipedia.org/wiki/Fibonacci_number
[time]: https://en.wikipedia.org/wiki/Time_complexity
