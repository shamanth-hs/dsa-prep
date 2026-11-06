# Alternate Positive and Negative Elements

- **Source File:** `[arrays/arrangement.py](file:///Users/shamanth/Desktop/DSA/problem-solving/arrays/arrangement.py)`
- **Language:** Python
- **Category:** Arrays / Two Pointers & Partitioning
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Given an array of positive and negative integers, rearrange the array such that negative and positive numbers appear at alternate positions while maintaining partition structure.
        
**Input:** An array of integers containing positive and negative values (e.g., `[-1, 2, -3, 4, 5, 6, -7, 8, 9]`).  
**Output:** Rearranged array with alternating negative and positive numbers.  
**Constraints:** In-place modification preferred with $O(1)$ extra space.

---

## 2. Algorithm & Approach

1. **Partition Step (Lomuto Partition):** Rearrange the array so that all negative elements are shifted to the left side and all positive elements are on the right side.
2. **Alternation Step:** Initialize two pointers — `neg` starting at index 0 and `pos` starting at the first positive number (pivot index).
3. Swap positive elements with alternate positions of negative elements (step by 2) until pointers cross or boundaries are reached.

---

## 3. Flowchart

```mermaid
graph TD
    Start[Start: alternate_pos_neg] --> P[Partition: negatives left, positives right]
    P --> Init[Init pointers: neg = 0, pos = pivot_index]
    Init --> Check{neg < pos and pos < len and arr[neg] < 0?}
    Check -- Yes --> Swap[Swap arr[neg], arr[pos]]
    Swap --> Advance[neg = neg + 2, pos = pos + 1]
    Advance --> Check
    Check -- No --> End[Return Rearranged Array]
```

---

## 4. Source Code

```python
def partition(arr, low, high):
    i = low-1   # i elements will be smaller, index of left part

    for j in range(low, high):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def alternate_pos_neg(arr):
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

array = [-1, 2, 3, -4, -5, 6, 7, -2, 9, -10]
print(alternate_pos_neg(array))
```

---

## 5. Simple Dry Run

Consider input `arr = [-1, 2, -3, 4, -5, 6]`:

| Step | State / Action | Current Array |
| :--- | :--- | :--- |
| 1 | Partitioning using `< 0` | `[-1, -3, -5, 4, 2, 6]` (negatives on left, pivot index = 3) |
| 2 | `neg = 0`, `pos = 3` | Swap `arr[0]` (-1) with `arr[3]` (4) -> `[4, -3, -5, -1, 2, 6]` |
| 3 | Advance `neg = 2`, `pos = 4` | Swap `arr[2]` (-5) with `arr[4]` (2) -> `[4, -3, 2, -1, -5, 6]` |
| 4 | Advance `neg = 4`, `pos = 5` | `neg` meets boundary, loop terminates |
| Final | Result | `[4, -3, 2, -1, -5, 6]` |

---

## 6. Sample Output

```text
Original array: [-1, 2, -3, 4, -5, 6]
Rearranged array: [4, -3, 2, -1, -5, 6]
```

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n)$ — single partition pass and linear alternate swap pass
- **Space Complexity:** $O(1)$ — in-place array manipulation

---
[← Back to Master Documentation Index](../README.md)
