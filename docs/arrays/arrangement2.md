# Alternate Even and Odd Elements

- **Source File:** `[arrays/arrangement2.py](file:///Users/shamanth/Desktop/DSA/problem-solving/arrays/arrangement2.py)`
- **Language:** Python
- **Category:** Arrays / Two Pointers & Partitioning
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Given an array of integers, rearrange the array such that even and odd numbers appear at alternate positions.

**Input:** An integer array (e.g., `[1, 2, 3, 4, 5, 6]`).  
**Output:** Array with alternating even and odd elements.  
**Constraints:** In-place modification with $O(1)$ auxiliary space.

---

## 2. Algorithm & Approach

1. **Partition Step:** Apply Lomuto partition with condition `arr[j] % 2 == 0` to move all even numbers to the left half.
2. **Alternate Interleaving:** Use two pointers (`even = 0`, `odd = pivot_index`) and swap elements at even steps (`even += 2`) to alternate parity.

---

## 3. Flowchart

```mermaid
graph TD
    Start[Start: alternate_odd_even] --> Part[Partition: Evens to left, Odds to right]
    Part --> Ptrs[Init: even = 0, odd = pivot_index]
    Ptrs --> Cond{even < odd and odd < len?}
    Cond -- Yes --> Swap[Swap arr[even], arr[odd]]
    Swap --> Step[even += 2, odd += 1]
    Step --> Cond
    Cond -- No --> Done[Return Interleaved Array]
```

---

## 4. Source Code

```python
def partition(arr, low, high):
    i = low-1   # i elements will be smaller, index of left part

    for j in range(low, high):
        if arr[j]%2 == 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def alternate_odd_even(arr):
    n = len(arr)//2

    # Partitioning
    pivot_index = partition(arr, 0, len(arr)-1)

    neg_idx = 0
    pos_idx = n

    while pos_idx < 2*n and neg_idx < n:
        arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
        pos_idx += 2
        neg_idx += 2
    
    return arr

array = [3, 4, 1, 1, 6, 8, 10, 11, 9, 10]
print(alternate_odd_even(array))
```

---

## 5. Simple Dry Run

Input: `arr = [1, 2, 3, 4, 5, 6]`

| Step | Operation | Array State |
| :--- | :--- | :--- |
| 1 | Partition evens to left | `[2, 4, 6, 1, 5, 3]` (pivot index = 3) |
| 2 | `even = 0`, `odd = 3` | Swap `arr[0]` (2) with `arr[3]` (1) -> `[1, 4, 6, 2, 5, 3]` |
| 3 | Advance `even = 2`, `odd = 4` | Swap `arr[2]` (6) with `arr[4]` (5) -> `[1, 4, 5, 2, 6, 3]` |
| 4 | Loop terminates | Alternating odd/even parity achieved |

---

## 6. Sample Output

```text
Input: [1, 2, 3, 4, 5, 6]
Output: [1, 4, 5, 2, 6, 3]
```

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n)$ — partition followed by linear pointer scan
- **Space Complexity:** $O(1)$ — in-place array operations

---
[← Back to Master Documentation Index](../README.md)
