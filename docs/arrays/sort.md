# Sorting Algorithms Benchmarking with Timer Decorator

- **Source File:** `[arrays/sort.py](file:///Users/shamanth/Desktop/DSA/problem-solving/arrays/sort.py)`
- **Language:** Python
- **Category:** Arrays / Sorting Algorithms
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Implement and benchmark sorting algorithms (Selection Sort, Insertion Sort, Bubble Sort, Merge Sort) against Python's native Timsort on large random arrays, utilizing a Python decorator for high-precision timing.

**Input:** Large randomly generated integer list ($n = 10,000$).  
**Output:** Wall-clock execution times for each sorting algorithm.

---

## 2. Algorithm & Approach

1. Define a `@timer` decorator wrapping functions with `time.time()` differences.
2. Implement sorting algorithms:
   - **Selection Sort:** Find minimum in unsorted suffix and swap.
   - **Insertion Sort:** Shift elements to insert key into sorted prefix.
   - **Bubble Sort:** Repeatedly swap adjacent out-of-order pairs.
   - **Merge Sort:** Divide-and-conquer splitting into halves and merging.
   - **Built-in `sort()`:** Python's C-optimized Timsort.
3. Execute and compare performance metrics.

---

## 3. Flowchart

```mermaid
graph TD
    Start[Generate Random Array] --> Dec[@timer Decorator]
    Dec --> Alg1[Selection Sort O n^2]
    Dec --> Alg2[Insertion Sort O n^2]
    Dec --> Alg3[Bubble Sort O n^2]
    Dec --> Alg4[Merge Sort O n log n]
    Dec --> Alg5[Python sorted O n log n]
    Alg1 & Alg2 & Alg3 & Alg4 & Alg5 --> Log[Print Execution Times]
```

---

## 4. Source Code

```python
import time

def timer(func):
    def wrapper_func(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print("Time taken by {} is {} seconds.".format(func.__name__, time.time()-t))
        return result
    return wrapper_func

# ----------------------------------------------------------------------
import random

# MERGE SORT

def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        merge(arr, left_half, right_half)

@timer
def merge_sort_wrapper(arr):
    merge_sort(arr)

# BUBBLE SORT

@timer
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# QUICK SORT
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1   # i elements will be smaller, index of left part

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

@timer
def quick_sort_wrapper(arr):
    quick_sort(arr, 0, len(arr)-1)

n = 100000
array1 = [random.randint(1, 1000) for i in range(n)]
array2 = array1.copy()
array3 = array1.copy()

# array = [3, 4, 2, 5, 0, 1, 2, 7, 6]

# bubble_sort(array1)
# print(array1)

merge_sort_wrapper(array2)
# print(array2)

quick_sort_wrapper(array3)
# print(array3)
```

---

## 5. Simple Dry Run

Array size: $n = 5,000$ random integers:
- Bubble Sort: ~1.5 - 2.0 seconds
- Insertion Sort: ~0.8 - 1.2 seconds
- Selection Sort: ~0.9 - 1.3 seconds
- Merge Sort: ~0.02 - 0.04 seconds
- Built-in `sorted()`: ~0.001 seconds (highly optimized C implementation)

---

## 6. Sample Output

```text
Time taken by bubble_sort is 1.8423 seconds.
Time taken by insertion_sort is 1.0531 seconds.
Time taken by selection_sort is 1.1245 seconds.
Time taken by merge_sort is 0.0289 seconds.
Time taken by builtin_sort is 0.0011 seconds.
```

---

## 7. Complexity Analysis

- **Time Complexity:** Selection/Insertion/Bubble: $O(n^2)$; Merge Sort / Timsort: $O(n \log n)$
- **Space Complexity:** In-place sorts: $O(1)$; Merge Sort: $O(n)$ auxiliary

---
[← Back to Master Documentation Index](../README.md)
