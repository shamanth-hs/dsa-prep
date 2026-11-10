# Repository verification — 10 November 2026

The repository is **not fully correct**. The findings below distinguish reproduced failures from defects identified by inspection. At the initial review, existing source and documentation were left unchanged. The documentation-only follow-up below records subsequent repairs.

## Checks performed

- Inventoried 111 existing Markdown files and 102 source files: 41 C++, 37 Python, 14 Java, 10 JavaScript.
- Parsed all 37 Python files successfully; checked all 10 JavaScript files with `node --check` successfully. Syntax success does not establish correctness.
- Compiled each Java file independently into a temporary output directory: 12 passed, 2 failed.
- Checked all 41 C++ files with Clang C++17. This machine lacks GCC's `bits/stdc++.h`, so a temporary header containing standard includes was used. LeetCode `Solution` snippets received standard includes and `using namespace std` in temporary copies. All passed this adapted syntax check; this is not a claim that every file builds standalone or is portable standard C++.
- Scanned all existing Markdown relative links: **204 broken link occurrences**, including repeated navigation links to nonexistent `docs/README.md`.
- Compared fenced source blocks with existing source files for documentation pages with recognized source metadata: no differences found. The copied code therefore carries the same defects.
- Ran targeted counterexamples for BFS, path finding, topological sorting, subset sum, diameter, maximum tree element, linked-list loop removal, array arrangement, Python prototype objects, Z search, and JavaScript XML loading.
- No existing project-wide test suite or build configuration was found. SQL queries were not executed against a database; PDFs were outside this review. Markdown explanations and examples are not comprehensively proven by link/source checks. This report is a defect review, not exhaustive certification.

## High-priority correctness and build findings

1. **Largest-island DFS reads an uninitialized dimension.** `graphs/largest_island_dfs_grid.cpp:50` declares `int n = dfs(graph, n, ...)`: the newly declared local `n` is already in scope in its initializer, so the argument is uninitialized, not the outer grid size. This causes undefined behavior. Rename the island-size variable and pass the original dimension. Also stop resetting the entire visited matrix after every cell; retaining it gives the intended O(N²) traversal. Found by inspection.

2. **Stable binary array solution does not count valid arrays.** `arrays/stable_binary_arr.cpp:7–25` never uses `limit`, returns at the first accepted candidate, uses `max` instead of summing disjoint choices, and has a recursive branch with unchanged state. It also writes `arr[size-1]` when size is zero on reachable variants. For the hardcoded `(zero=2, one=1, limit=3)`, there are three arrays (001, 010, 100); the first candidate is accepted and the code returns 1. Replace with a recurrence tracking remaining counts and consecutive-run constraints. Its Markdown omits the defining run-limit constraint and describes enumeration that does not happen.

3. **Iterative DFS path search abandons branches.** `graphs/path.cpp:49` and the analogous matrix implementation pop the current vertex, then push only its first unvisited neighbor. They cannot backtrack to explore another neighbor. Reproduced with 6 vertices and edges `2–0`, `2–5`: both iterative versions return `[2]`, while the valid path is `[2,5]`. Keep traversal frames on the stack or track parents while exploring all neighbors.

4. **BFS path reconstruction can loop forever for an unreachable target.** `graphs/path.cpp:102,172` reconstructs without checking reachability; parents default to zero. With source 2 and unreachable destination 5, reconstruction can become stuck at `parent[0] == 0`. Initialize parents to -1 and check visited[dest] before reconstruction. The analogous hardcoded destination in `graphs/bfs.cpp` has the same unreachable-target risk. Found by inspection.

5. **Topological sort omits vertex zero.** `graphs/topo_sort.cpp:36,53,69` starts vertex loops at 1 although input vertices are 0 through n-1. Reproduced with `3 1 / 0 1`: both implementations print only `2 1`, omitting 0. Start all loops at 0. If accepting arbitrary directed inputs, also detect cycles rather than returning an apparent topological order.

6. **Kruskal reads beyond the edge array on disconnected graphs.** `graphs/mst.cpp:31` only checks whether n-1 edges have been selected, never whether all e edges have been examined. Bound the edge index and explicitly report a disconnected graph or return a forest with its actual edge count. Found by inspection.

7. **Histogram Java example does not compile.** `stacks_queues/max_area_hist.java:3` declares public `Main` in the wrong filename, and uses `Pair` without defining or importing an available implementation. Confirmed by javac. Rename the class/file and provide a suitable pair representation.

8. **State-pattern Java example does not compile.** `design_patterns/10_State/Order.java:2` and subsequent declarations contain multiple public top-level types in one file. Confirmed by javac. Split them into matching files or make helper types package-private.

9. **JavaScript XML factory reader crashes.** `design_patterns/04_Factory/data_reader.js:32` constructs an undefined `Parser`. Running the script with its supplied `data.xml` raises `ReferenceError: Parser is not defined`. Add an actual XML parser dependency/import and handle its asynchronous API as applicable. There is no dependency manifest supplying this parser.

## Additional confirmed algorithm defects

10. **Subset-sum base cases are reversed.** `dynamic-programming/02_Knapsack/subset_sum.cpp:17` returns false for n == -1 before checking sum == 0. Reproduced input `1 5 / 5` prints 0 instead of 1: a valid subset using the first item is rejected. Check sum == 0 first. The same helper defect exists in `LC_416.cpp`, although complementary subsets can mask it for positive equal-partition inputs.

11. **BFS levels count popped vertices instead of distance.** `graphs/bfs.py` and `graphs/bfs.cpp` assign `level[v] = i` and increment i after each vertex. For edges 0–1, 0–2, 1–3, 2–4, the Python code prints levels `0 1 1 2 3`; expected `0 1 1 2 2`. Assign `level[v] = level[u] + 1` in list and matrix versions. Hardcoded destination 2 also requires at least three vertices and a reachability check.

12. **Diameter only considers paths through the root.** `trees/diameter.py:16` does not compare diameters inside child subtrees. A six-node tree whose left child has two chains of length two has true diameter 5 nodes, but the function returns 4. Its Markdown also defines diameter in edges, while code counts nodes: a one-node tree returns 1 instead of the documented 0. Compute height and maximum diameter at every node using one consistent unit.

13. **Removing a cycle through the head discards nodes.** `linked_list/loops_intersections.py:31` uses a predecessor-search shortcut that fails when Floyd's meeting point is the head. Reproduced `1→2→3→1`: removal leaves only node 1 reachable. Handle this case explicitly or locate the loop entry first and then its predecessor.

14. **Array alternation fails even with balanced inputs.** `arrays/arrangement.py` turns `[-1,2,-3,4]` into `[4,-3,-1,2]`. `arrays/arrangement2.py` turns `[2,1,4,3]` into `[3,4,2,1]`. Neither alternates. Their partition functions unconditionally swap the last element into the partition, the computed boundary is ignored, and advancing both pointers by two skips required placements. Implement predicate partitioning and interleaving with the actual boundary; define behavior for unequal counts and zero values. The Markdown dry runs do not match these implementations.

15. **Maximum tree element is wrong for negative values.** `trees/01_Recursion/trees_recursion.py:30` and `trees/01_Recursion/basic_tree_recusion.cpp:29` use zero for empty subtrees. A single node -3 returns 0 in Python instead of -3. Use negative infinity/INT_MIN for the empty contribution or handle absent children separately.

16. **Python prototype instances share default comments.** `design_patterns/02_Prototype/posts.py:4` uses mutable default `comments=[]`. Adding a comment to independently constructed post A also changes post B; reproduced. Use `comments=None` and allocate a fresh list per instance. Deep-copying clones does not fix this constructor problem.

17. **Z search fails when the separator occurs in the inputs.** `strings/z.py:29` assumes `$` never occurs, but does not declare or enforce this. Reproduced text `a$a`, pattern `a`: returns `[2]` instead of `[0,2]`. Use a sentinel outside the input alphabet and inspect text positions only, or explicitly restrict the input alphabet.

18. **Log truncation does not implement the documented fairness algorithm.** `interview questions/google_log_truncate.cpp` accepts every log until global capacity is full: after the early capacity check, `sourceCount < fairShare || currentTotal < MAX_TOTAL` is always true. Thirty A logs followed by B/C logs retains only A. The Markdown instead describes sorting demands and redistributing unused quotas; that algorithm is absent, and its O(k log k) claim does not describe the streaming implementation. Implement the stated batch allocation or specify a streaming policy with eviction/rebalancing.

## Documentation, constraints, and usability

- **Broken navigation:** 204 broken relative link occurrences were detected before this report was added. Pages under `docs/<topic>/` mostly link to `../README.md`, resolving to missing `docs/README.md`. Create the intended index or point to the real root README with the correct relative path.
- **Source links are rendered as code:** many source references wrap the entire Markdown link in backticks, preventing a clickable link. They also embed one machine's absolute `file:///Users/...` path. Use normal repository-relative Markdown links outside code spans.
- **Complexity claims describe improved algorithms, not actual code:** the LC 416 page claims O(target) space while the source allocates a 201×20001 table; recursive knapsack/subset-sum routines pass vectors by value, adding copying overhead beyond the usual O(n×capacity)/O(n×sum) explanation; largest-island documentation cannot claim the ordinary O(N²) implementation while visited is reset per cell.
- **Fibonacci range is unsafe:** `fib_memo.cpp` discusses inputs up to 100, but the implemented sequence F(0)=F(1)=1 overflows signed 64-bit at n=92. Both implementations use staircase-style shifted Fibonacci rather than conventional F(0)=0, F(1)=1. State that convention and either restrict the range or use an appropriate larger/modular representation.
- **LeetCode snippets require a host harness:** several `Solution` files intentionally lack includes, namespace declarations, and main. Document their execution environment instead of presenting them as standalone programs.
- **C++ portability:** widespread `bits/stdc++.h` requires GCC-style headers; the variable-length `arr[size]` in stable-array code is a compiler extension rather than standard C++. A native Clang standalone build is not currently supported without adjustments.
- **Incorrect teaching notes:** `dynamic-programming/01_Fibonacci/notes.md` claims multiple recursive calls with constant input reductions always imply exponential complexity. This needs qualification: branching structure, work, memoization, and reachable states matter. `cpp_language/README.md` calls stack/queue/priority_queue “non-sequence containers”; they are container adaptors. BFS is suitable for disconnected graphs when restarted on each unvisited component, contrary to the advice to avoid it in the BFS source comments.
- **Unimplemented placeholder:** `my_codes/two_pointer.cpp` contains only an empty main, so it is not a two-pointer solution.

## Suggested repair order

1. Fix undefined behavior, hangs, and Java/JavaScript execution failures.
2. Fix the reproduced algorithm failures and add focused regression cases.
3. Update each mirrored Markdown source block, dry run, sample output, and complexity explanation together with its source.
4. Repair the documentation index and relative links; document how standalone examples and judge snippets are run.

## Documentation repair follow-up

The Markdown follow-up added docs/README.md, repaired source links and index navigation, corrected Fibonacci conventions and examples, updated complexity and teaching explanations, and marked known source defects on the relevant pages. A post-edit scan found no broken relative file links. The findings above describe the original audit state; source-code defects remain unfixed. SQL execution and PDF verification remain outside the review.
