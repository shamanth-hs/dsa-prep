# Segregate Zeros to End of Array

- **Source File:** `[arrays/arrangement3.py](file:///Users/shamanth/Desktop/DSA/problem-solving/arrays/arrangement3.py)`
- **Language:** Python
- **Category:** Arrays / Two Pointers & Partitioning
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Given an array of integers containing zeros and non-zeros, move all zeros to the end of the array while maintaining non-zero elements at the beginning.

**Input:** Array `[1, 0, 2, 0, 0, 3, 4]`  
**Output:** Array `[1, 2, 3, 4, 0, 0, 0]`  
**Constraints:** In-place modifications with minimal swaps.

---

## 2. Algorithm & Approach

1. Use a partition scheme where `arr[j] != 0` pushes non-zero elements into the left boundary tracked by index `i`.
2. Whenever `arr[j] != 0`, increment `i` and swap `arr[i]` with `arr[j]`.
3. All zero elements naturally migrate toward the higher indices.

---

## 3. Flowchart

```mermaid
graph TD
    Start[Start: push_zeros] --> Init[i = low - 1, loop j from low to high]
    Init --> Check{arr[j] != 0?}
    Check -- Yes --> Inc[i = i + 1]
    Inc --> Swap[Swap arr[i] with arr[j]]
    Swap --> Next[Next j]
    Check -- No --> Next
    Next --> LoopEnd{j reached high?}
    LoopEnd -- No --> Check
    LoopEnd -- Yes --> Final[Return array with zeros at end]
```

---

## 4. Source Code

```python
def partition(arr, low, high):
    i = low-1   # i elements will be smaller, index of left part

    for j in range(low, high):
        if arr[j] != 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def push_zeros(arr):
    n = len(arr)//2

    # Partitioning
    pivot_index = partition(arr, 0, len(arr)-1)

    # neg_idx = 0
    # pos_idx = n

    # while pos_idx < 2*n and neg_idx < n:
    #     arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
    #     pos_idx += 2
    #     neg_idx += 2
    
    return arr

array = [3, 0, 1, 0, 6, 0, 10, 11, 0, 10]
print(push_zeros(array))
```

---

## 5. Simple Dry Run

Input: `[1, 0, 2, 0, 3]`

| j | arr[j] | Action | Array State |
| :---: | :---: | :--- | :--- |
| 0 | 1 | `!= 0`: `i = 0`, swap `arr[0], arr[0]` | `[1, 0, 2, 0, 3]` |
| 1 | 0 | `== 0`: skip | `[1, 0, 2, 0, 3]` |
| 2 | 2 | `!= 0`: `i = 1`, swap `arr[1], arr[2]` | `[1, 2, 0, 0, 3]` |
| 3 | 0 | `== 0`: skip | `[1, 2, 0, 0, 3]` |
| 4 | 3 | `!= 0`: `i = 2`, swap `arr[2], arr[4]` | `[1, 2, 3, 0, 0]` |

---

## 6. Sample Output

```text
Input: [1, 0, 2, 0, 3]
Output: [1, 2, 3, 0, 0]
```

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n)$ — single pass partition over array
- **Space Complexity:** $O(1)$ — in-place swaps

---
[← Back to Master Documentation Index](../README.md)
