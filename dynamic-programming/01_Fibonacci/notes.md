### 01. Fibonacci 
<hr>

#### Introduction

This is the problem with which you start your DP journey. What you need to learn in this is:

1. Naive Fibonacci recursion branches into overlapping subproblems and takes O(φ^n) time, where φ ≈ 1.618 is the golden ratio. Multiple recursive calls with constant input reductions do not by themselves prove exponential complexity; analyze the recurrence, branching, work per call, and whether results are cached.
2. However, you can reduce the time-complexity by creating a memo table and storing the results of recursive calls inside a global array, i.e. the memo table. This is the top-down approach, also called as memoization. YOU ARE DONE! This is the DP solution. DP = Recursion + Memoization. In other words, DP is just an efficient recursion which doesn't repeat calculating the recursive calls for which it already has computed the answer.  
3. Once we have written the Memoization solution, we can observe how the memo table is filled. We can utilize that pattern and fill the same table using for loops. This is the bottom-up approach, also called as tabulation. Tabulation is ever so slightly better than memoization, but coming up with a tabulation solution organically is tough! My intuition most of the times gives me recursive ideas, and not the for-loop ideas on how to solve a particular problem. Again, just saying, Recursion is easier!!

You should also learn one thing, that DP problems are solving two types of problems: 

* **Optimization Problems:** Whenever the question asks you to find something maximum, minimum, least, longest, highest, shortest, etc., i.e. they are asking you to find the extreme value or provide the optimized solution, there is a chance that this could be the DP problem. Not always, but still a good chance. 
* **Combinatorial Problems:** If the question asks the number of ways you can do something, or perform some specific count, there is a good chance it is a DP problem. 

Once you know this and also know the common pattern of how to convert a recursion to a memoized DP solution, you can solve for the staircase problem. 

#### Variations

**1. Staircase Problem**

There is only one variation to this pattern. The problem says:

Given $n$ steps on a staircase, you can climb either 1 step or 2 steps at a time. If the sequence of taken by you to reach the $n$th step is called the way you reach the top, in how many ways you can reach to the top of the staircase. For example, if the staircase has 4 steps, you can climb in 5 ways: (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2), (1, 1, 1 , 1). So the output here is 5. 

Look this is a combinatorial problem. This is a fibonacci template because: 

$ways(n) = ways(n-1) + ways(n-2)$

I will discuss this separately. (Not today!) 

Since the equation is exactly same as fibonacci, you can solve this problem by using the code in `fib_memo.cpp`. 

<hr/>
## Sequence convention and numeric range

The source uses f(0) = f(1) = 1, which counts staircase paths and equals conventional Fibonacci F(n+1). Signed 64-bit results are valid only through n = 91; n = 92 already overflows. The memo table size of 101 does not make results through 100 numerically safe. Use an appropriate larger or modular representation if larger inputs are required.
