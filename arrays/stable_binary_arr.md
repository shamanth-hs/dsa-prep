# Documentation for stable_binary_arr.cpp

## Function: `numberOfStableArrays`

This document provides an analysis of the `numberOfStableArrays` function found in `stable_binary_arr.cpp`. The function aims to count the number of "stable" binary arrays given a number of zeros and ones.

### Algorithm Steps

The algorithm implemented in the code follows these steps:

1.  **`numberOfStableArrays(int zero, int one, int limit)` function:**
    1.  Calculates the total size of the array as `zero + one`.
    2.  Initializes an integer array `arr` of this `size` with all elements set to `0`.
    3.  Initializes a `count` variable to `0`.
    4.  Calls the `stableArray` helper function and returns its result.

2.  **`stableArray(int zero, int one, int size, int count, int arr[])` function:**
    *   This is a recursive function intended to find stable arrays.
    1.  **Base Case:** If `size` becomes negative, it returns the current `count`.
    2.  It modifies the array by setting `arr[size-1] = 1`.
    3.  It calls `isStable` to validate the array.
    4.  If `isStable` returns `true`, the function immediately returns `1`.
    5.  If `isStable` returns `false`, it makes two recursive calls:
        *   `stableArray(zero, one, size - 1, count, arr)`
        *   `stableArray(zero, one, size, count, arr)`
    6.  It returns the sum of `count` and the maximum value from the two recursive calls.

3.  **`isStable(int zero, int one, int size, int arr[])` function:**
    1.  Counts the total number of zeros (`countZero`) and ones (`countOne`) in the `arr`.
    2.  It checks if `countZero` is greater than the allowed `zero` count and if `countOne` is greater than the allowed `one` count.
    3.  Returns `false` if either count is exceeded, `true` otherwise.

### Flowchart

```mermaid
graph TD
    A[Start: numberOfStableArrays] --> B{Initialize arr of size zero+one with 0s};
    B --> C{Call stableArray(zero, one, size, 0, arr)};
    C --> D[stableArray];
    D --> E{size < 0?};
    E -- Yes --> F[Return count];
    E -- No --> G{Set arr[size-1] = 1};
    G --> H{Call isStable(arr)};
    H --> I{isStable?};
    I -- Yes --> J[Return 1];
    I -- No --> K{Recursive Call 1: stableArray(size-1)};
    K --> L{Recursive Call 2: stableArray(size)};
    L --> M{Return count + max(Call 1, Call 2)};
    M --> N[End];
    J --> N;
    F --> N;

    subgraph isStable
        S1{Start isStable} --> S2{countZero = 0, countOne = 0};
        S2 --> S3{Iterate through arr};
        S3 --> S4{arr[i] == 0?};
        S4 -- Yes --> S5{countZero++};
        S4 -- No --> S6{countOne++};
        S5 --> S7{countZero > zero?};
        S6 --> S8{countOne > one?};
        S7 -- Yes --> S9[Return false];
        S8 -- Yes --> S9;
        S3 -- End of loop --> S10{Return true};
    end
```

### Implementation Notes

*   **Unused Parameter:** The `limit` parameter in `numberOfStableArrays` is never used in any of the functions. The name "stable array" usually implies a constraint on consecutive elements, which is what `limit` might be for, but it is not implemented.
*   **Infinite Recursion:** The `stableArray` function has a recursive call `stableArray(zero, one, size, count, arr)` which calls itself with the exact same `size` parameter. This will lead to infinite recursion and a stack overflow error when this branch of logic is taken.
*   **Misleading Function Name:** The `isStable` function does not check for stability in terms of consecutive elements. It only checks if the total counts of zeros and ones are within the limits passed as parameters. A better name would be `hasValidCounts`.
*   **Overall Logic:** The overall logic of the program appears to be incorrect for solving the problem of counting stable binary arrays in the typical sense (with a limit on consecutive elements). The recursive structure is flawed.

This documentation describes the code as written. For a correct implementation of counting stable arrays, the algorithm would need to be significantly different, likely using dynamic programming or a corrected recursive approach that properly manages state (like current number of zeros/ones, and the count of the last consecutive character).

### Required stability constraint and concrete failure

A stable binary array contains exactly the requested counts and no run of equal bits longer than `limit`. The current source does not enforce that condition. Its hardcoded input (2, 1, 3) returns 1 instead of 3 (001, 010, 100). Also, the size < 0 base case does not guard the write to arr[size−1] when size == 0. The flowchart above describes the flawed source, not a correct solution.
