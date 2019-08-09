# Algorithms
Examples of common algorithms.
Enter the directory `examples/` to test each one (except dynamic_programming).

Divide & Conquer:
- [Binary Search][bs], `O(log(n))`.
- [Merge Sort][ms], `O(nlog(n))`.

Dynamic Programming:
- [Longest Common Subsequence][lcsq] `O(n*m)`.
- [Longest Common Substring][lcst] `O(n*m)`.
- (see `dynamic_programming_concept`)

Graph:
- [Breadth First Search][dfs], `O(V+E)`.
- [Clique][clique], `O(n^k)` where `k` is the clique size.
- [Depth First Search][dfs], `O(V+E)`.

Other:
- [Bubble Sort][bsr], `O(n^2)`.
- [Insertion Sort][is], `O(n^2)`.
- [Selection Sort][ss], `O(n^2)`.
- Group: Groups members of a population into n, k-size groups without replacement.
- Melkman: computes the [Convex Hull][ch] of a [Simple Polygon][sp] in `O(n)` time.
- Relative Sort: sorts an array relative to the ordering of another array, `O(n*m*log(m))`, where `m` is the length of the first array and `n` is the length of the second array.


[bfs]: https://en.wikipedia.org/wiki/Breadth-first_search
[bs]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[bsr]: https://en.wikipedia.org/wiki/Bubble_sort
[clique]: https://en.wikipedia.org/wiki/Clique_problem
[dfs]: https://en.wikipedia.org/wiki/Depth-first_search
[is]: https://en.wikipedia.org/wiki/Insertion_sort
[lcsq]: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
[lcst]: https://en.wikipedia.org/wiki/Longest_common_substring_problem
[ss]: https://en.wikipedia.org/wiki/Selection_sort
[ms]: https://en.wikipedia.org/wiki/Merge_sort
[ch]: https://en.wikipedia.org/wiki/Convex_hull
[sp]: https://en.wikipedia.org/wiki/Simple_polygon
