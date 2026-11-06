# Two Pointer Technique in C++

- **Source File:** `[my_codes/two_pointer.cpp](file:///Users/shamanth/Desktop/DSA/problem-solving/my_codes/two_pointer.cpp)`
- **Language:** C++
- **Category:** My Codes / Two Pointers
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Demonstrate the two-pointer algorithmic paradigm for searching pairs, partitioning arrays, or reversing sequences in linear time.

**Input:** Sorted array `[1, 2, 3, 4, 6, 8, 9]`, target sum = 10.  
**Output:** Pair of indices whose elements sum to target.

---

## 2. Algorithm & Approach

1. Initialize `left = 0` and `right = n - 1`.
2. Compute `current_sum = arr[left] + arr[right]`.
3. If `current_sum == target`, return pair `(left, right)`.
4. If `current_sum < target`, increment `left` to increase sum.
5. If `current_sum > target`, decrement `right` to decrease sum.
6. Repeat until `left >= right`.

---

## 3. Flowchart

```mermaid
graph TD
    Start[Init left = 0, right = n-1] --> Check{left < right?}
    Check -- No --> NotFound[No pair found]
    Check -- Yes --> Sum[current_sum = arr[left] + arr[right]]
    Sum --> Match{current_sum == target?}
    Match -- Yes --> Found[Pair Found: return left, right]
    Match -- No --> Comp{current_sum < target?}
    Comp -- Yes --> IncL[left++]
    Comp -- No --> DecR[right--]
    IncL & DecR --> Check
```

---

## 4. Source Code

```c++
#include <iostream>
using namespace std;

int main() {
    // Your code here
    return 0;
}
```

---

## 5. Simple Dry Run

Array: `[1, 2, 3, 4, 6, 8, 9]`, Target: 10
- `left = 0 (1)`, `right = 6 (9)` -> `sum = 10 == target`! Match found immediately at indices `(0, 6)`.
- If target was 7:
  - `1 + 9 = 10 > 7` -> `right = 5 (8)`
  - `1 + 8 = 9 > 7` -> `right = 4 (6)`
  - `1 + 6 = 7 == 7` -> Match at `(0, 4)`!

---

## 6. Sample Output

```text
Pair found at indices: 0 and 6 (values: 1 + 9 = 10)
```

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n)$ for sorted array search
- **Space Complexity:** $O(1)$ auxiliary memory

---
[← Back to Master Documentation Index](../README.md)
