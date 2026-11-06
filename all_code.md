# All Repository Code

> **Repository:** `problem-solving`  
> **Note:** All directories starting with `_` (e.g. `_NOTES_`, `_reading_material_`, `_sql_interviews_`) and non-code binaries are excluded.  
> **Total Source Files:** 102  
> **Total Lines of Code:** 6,933  

## Summary Statistics

| Language | Files | Lines of Code |
| :--- | :---: | :---: |
| **C++** | 41 | 2,862 |
| **Python** | 37 | 2,266 |
| **Java** | 14 | 1,052 |
| **JavaScript** | 10 | 753 |
| **Total** | **102** | **6,933** |

### Directory Overview

| Directory / Topic | Code Files |
| :--- | :---: |
| [`arrays`](#dir-arrays) | 12 |
| [`cpp_language`](#dir-cpp_language) | 1 |
| [`design_patterns`](#dir-design_patterns) | 30 |
| [`dynamic-programming`](#dir-dynamic-programming) | 12 |
| [`graphs`](#dir-graphs) | 12 |
| [`interview questions`](#dir-interview-questions) | 1 |
| [`linked_list`](#dir-linked_list) | 3 |
| [`my_codes`](#dir-my_codes) | 1 |
| [`range queries`](#dir-range-queries) | 1 |
| [`recursion_backtracking`](#dir-recursion_backtracking) | 3 |
| [`stacks_queues`](#dir-stacks_queues) | 15 |
| [`strings`](#dir-strings) | 3 |
| [`trees`](#dir-trees) | 8 |
| [*Companion Data & Input Files*](#companion-data-files) | 6 |

---

<a id="table-of-contents"></a>
## Table of Contents

- **[`arrays/`](#dir-arrays)** (12 files)
  - [arrays/arrangement.py](#file-arrays-arrangement-py) *(Python, 29 lines)*
  - [arrays/arrangement2.py](#file-arrays-arrangement2-py) *(Python, 29 lines)*
  - [arrays/arrangement3.py](#file-arrays-arrangement3-py) *(Python, 29 lines)*
  - [arrays/custom_sort.cpp](#file-arrays-custom_sort-cpp) *(C++, 46 lines)*
  - [arrays/custom_sort.py](#file-arrays-custom_sort-py) *(Python, 7 lines)*
  - [arrays/leetcode_sliding_window_map_76.cpp](#file-arrays-leetcode_sliding_window_map_76-cpp) *(C++, 58 lines)*
  - [arrays/maps.cpp](#file-arrays-maps-cpp) *(C++, 41 lines)*
  - [arrays/sets.cpp](#file-arrays-sets-cpp) *(C++, 27 lines)*
  - [arrays/sets.py](#file-arrays-sets-py) *(Python, 3 lines)*
  - [arrays/sort.py](#file-arrays-sort-py) *(Python, 100 lines)*
  - [arrays/stable_binary_arr.cpp](#file-arrays-stable_binary_arr-cpp) *(C++, 52 lines)*
  - [arrays/toggle.py](#file-arrays-toggle-py) *(Python, 63 lines)*
- **[`cpp_language/`](#dir-cpp_language)** (1 files)
  - [cpp_language/01_Array_Operations/sort.cpp](#file-cpp_language-01_array_operations-sort-cpp) *(C++, 59 lines)*
- **[`design_patterns/`](#dir-design_patterns)** (30 files)
  - [design_patterns/01_Singleton/Logger.java](#file-design_patterns-01_singleton-logger-java) *(Java, 44 lines)*
  - [design_patterns/01_Singleton/logger.js](#file-design_patterns-01_singleton-logger-js) *(JavaScript, 26 lines)*
  - [design_patterns/01_Singleton/logger.py](#file-design_patterns-01_singleton-logger-py) *(Python, 31 lines)*
  - [design_patterns/02_Prototype/SocialMediaPost.java](#file-design_patterns-02_prototype-socialmediapost-java) *(Java, 69 lines)*
  - [design_patterns/02_Prototype/posts.js](#file-design_patterns-02_prototype-posts-js) *(JavaScript, 52 lines)*
  - [design_patterns/02_Prototype/posts.py](#file-design_patterns-02_prototype-posts-py) *(Python, 46 lines)*
  - [design_patterns/03_Builder/Main.java](#file-design_patterns-03_builder-main-java) *(Java, 76 lines)*
  - [design_patterns/03_Builder/sandwich.js](#file-design_patterns-03_builder-sandwich-js) *(JavaScript, 63 lines)*
  - [design_patterns/03_Builder/sandwich.py](#file-design_patterns-03_builder-sandwich-py) *(Python, 48 lines)*
  - [design_patterns/04_Factory/Main.java](#file-design_patterns-04_factory-main-java) *(Java, 81 lines)*
  - [design_patterns/04_Factory/data_reader.js](#file-design_patterns-04_factory-data_reader-js) *(JavaScript, 71 lines)*
  - [design_patterns/04_Factory/data_reader.py](#file-design_patterns-04_factory-data_reader-py) *(Python, 66 lines)*
  - [design_patterns/05_Facade/Main.java](#file-design_patterns-05_facade-main-java) *(Java, 70 lines)*
  - [design_patterns/05_Facade/home.js](#file-design_patterns-05_facade-home-js) *(JavaScript, 62 lines)*
  - [design_patterns/05_Facade/home.py](#file-design_patterns-05_facade-home-py) *(Python, 50 lines)*
  - [design_patterns/06_Proxy/Main.java](#file-design_patterns-06_proxy-main-java) *(Java, 64 lines)*
  - [design_patterns/06_Proxy/image_renderer.js](#file-design_patterns-06_proxy-image_renderer-js) *(JavaScript, 62 lines)*
  - [design_patterns/06_Proxy/image_renderer.py](#file-design_patterns-06_proxy-image_renderer-py) *(Python, 49 lines)*
  - [design_patterns/07_Iterator/Main.java](#file-design_patterns-07_iterator-main-java) *(Java, 128 lines)*
  - [design_patterns/07_Iterator/books.js](#file-design_patterns-07_iterator-books-js) *(JavaScript, 118 lines)*
  - [design_patterns/07_Iterator/books.py](#file-design_patterns-07_iterator-books-py) *(Python, 96 lines)*
  - [design_patterns/08_Observer/Main.java](#file-design_patterns-08_observer-main-java) *(Java, 77 lines)*
  - [design_patterns/08_Observer/broadcast.js](#file-design_patterns-08_observer-broadcast-js) *(JavaScript, 60 lines)*
  - [design_patterns/08_Observer/broadcast.py](#file-design_patterns-08_observer-broadcast-py) *(Python, 67 lines)*
  - [design_patterns/09_Mediator/Main.java](#file-design_patterns-09_mediator-main-java) *(Java, 154 lines)*
  - [design_patterns/09_Mediator/tower.js](#file-design_patterns-09_mediator-tower-js) *(JavaScript, 130 lines)*
  - [design_patterns/09_Mediator/tower.py](#file-design_patterns-09_mediator-tower-py) *(Python, 107 lines)*
  - [design_patterns/10_State/Order.java](#file-design_patterns-10_state-order-java) *(Java, 127 lines)*
  - [design_patterns/10_State/order.js](#file-design_patterns-10_state-order-js) *(JavaScript, 109 lines)*
  - [design_patterns/10_State/order.py](#file-design_patterns-10_state-order-py) *(Python, 89 lines)*
- **[`dynamic-programming/`](#dir-dynamic-programming)** (12 files)
  - [dynamic-programming/01_Fibonacci/fib.cpp](#file-dynamic-programming-01_fibonacci-fib-cpp) *(C++, 36 lines)*
  - [dynamic-programming/01_Fibonacci/fib_memo.cpp](#file-dynamic-programming-01_fibonacci-fib_memo-cpp) *(C++, 51 lines)*
  - [dynamic-programming/02_Knapsack/LC_322.cpp](#file-dynamic-programming-02_knapsack-lc_322-cpp) *(C++, 42 lines)*
  - [dynamic-programming/02_Knapsack/LC_416.cpp](#file-dynamic-programming-02_knapsack-lc_416-cpp) *(C++, 40 lines)*
  - [dynamic-programming/02_Knapsack/LC_494.cpp](#file-dynamic-programming-02_knapsack-lc_494-cpp) *(C++, 19 lines)*
  - [dynamic-programming/02_Knapsack/LC_518.cpp](#file-dynamic-programming-02_knapsack-lc_518-cpp) *(C++, 32 lines)*
  - [dynamic-programming/02_Knapsack/knapsack.cpp](#file-dynamic-programming-02_knapsack-knapsack-cpp) *(C++, 56 lines)*
  - [dynamic-programming/02_Knapsack/knapsack_space_optimize.cpp](#file-dynamic-programming-02_knapsack-knapsack_space_optimize-cpp) *(C++, 48 lines)*
  - [dynamic-programming/02_Knapsack/subset_sum.cpp](#file-dynamic-programming-02_knapsack-subset_sum-cpp) *(C++, 69 lines)*
  - [dynamic-programming/03_LCS/scs_1.cpp](#file-dynamic-programming-03_lcs-scs_1-cpp) *(C++, 91 lines)*
  - [dynamic-programming/03_LCS/scs_2.cpp](#file-dynamic-programming-03_lcs-scs_2-cpp) *(C++, 98 lines)*
  - [dynamic-programming/Problem_Set_Easy/01_min_steps_to_one.cpp](#file-dynamic-programming-problem_set_easy-01_min_steps_to_one-cpp) *(C++, 70 lines)*
- **[`graphs/`](#dir-graphs)** (12 files)
  - [graphs/bfs.cpp](#file-graphs-bfs-cpp) *(C++, 133 lines)*
  - [graphs/bfs.py](#file-graphs-bfs-py) *(Python, 115 lines)*
  - [graphs/create_graph.cpp](#file-graphs-create_graph-cpp) *(C++, 67 lines)*
  - [graphs/cycles.cpp](#file-graphs-cycles-cpp) *(C++, 93 lines)*
  - [graphs/cycles.py](#file-graphs-cycles-py) *(Python, 96 lines)*
  - [graphs/dfs.cpp](#file-graphs-dfs-cpp) *(C++, 134 lines)*
  - [graphs/dfs.py](#file-graphs-dfs-py) *(Python, 93 lines)*
  - [graphs/largest_island_dfs_grid.cpp](#file-graphs-largest_island_dfs_grid-cpp) *(C++, 71 lines)*
  - [graphs/minimum_moves_knight_bfs_grid.py](#file-graphs-minimum_moves_knight_bfs_grid-py) *(Python, 34 lines)*
  - [graphs/mst.cpp](#file-graphs-mst-cpp) *(C++, 67 lines)*
  - [graphs/path.cpp](#file-graphs-path-cpp) *(C++, 226 lines)*
  - [graphs/topo_sort.cpp](#file-graphs-topo_sort-cpp) *(C++, 105 lines)*
- **[`interview questions/`](#dir-interview-questions)** (1 files)
  - [interview questions/google_log_truncate.cpp](#file-interview-questions-google_log_truncate-cpp) *(C++, 114 lines)*
- **[`linked_list/`](#dir-linked_list)** (3 files)
  - [linked_list/crud_ll.py](#file-linked_list-crud_ll-py) *(Python, 140 lines)*
  - [linked_list/loops_intersections.py](#file-linked_list-loops_intersections-py) *(Python, 107 lines)*
  - [linked_list/ops_ll.py](#file-linked_list-ops_ll-py) *(Python, 108 lines)*
- **[`my_codes/`](#dir-my_codes)** (1 files)
  - [my_codes/two_pointer.cpp](#file-my_codes-two_pointer-cpp) *(C++, 7 lines)*
- **[`range queries/`](#dir-range-queries)** (1 files)
  - [range queries/segment_tree.cpp](#file-range-queries-segment_tree-cpp) *(C++, 120 lines)*
- **[`recursion_backtracking/`](#dir-recursion_backtracking)** (3 files)
  - [recursion_backtracking/02_Backtracking/knights_tour.cpp](#file-recursion_backtracking-02_backtracking-knights_tour-cpp) *(C++, 72 lines)*
  - [recursion_backtracking/02_Backtracking/n_queens.cpp](#file-recursion_backtracking-02_backtracking-n_queens-cpp) *(C++, 86 lines)*
  - [recursion_backtracking/02_Backtracking/subset_sum_with_subsets.cpp](#file-recursion_backtracking-02_backtracking-subset_sum_with_subsets-cpp) *(C++, 49 lines)*
- **[`stacks_queues/`](#dir-stacks_queues)** (15 files)
  - [stacks_queues/max_area_hist.cpp](#file-stacks_queues-max_area_hist-cpp) *(C++, 92 lines)*
  - [stacks_queues/max_area_hist.java](#file-stacks_queues-max_area_hist-java) *(Java, 65 lines)*
  - [stacks_queues/max_area_hist.py](#file-stacks_queues-max_area_hist-py) *(Python, 57 lines)*
  - [stacks_queues/mergeRods.java](#file-stacks_queues-mergerods-java) *(Java, 28 lines)*
  - [stacks_queues/merge_rods.cpp](#file-stacks_queues-merge_rods-cpp) *(C++, 29 lines)*
  - [stacks_queues/merge_rods.py](#file-stacks_queues-merge_rods-py) *(Python, 20 lines)*
  - [stacks_queues/ngr_ngl.cpp](#file-stacks_queues-ngr_ngl-cpp) *(C++, 64 lines)*
  - [stacks_queues/ngr_ngl_index.cpp](#file-stacks_queues-ngr_ngl_index-cpp) *(C++, 64 lines)*
  - [stacks_queues/nsr_nsl.cpp](#file-stacks_queues-nsr_nsl-cpp) *(C++, 64 lines)*
  - [stacks_queues/queues.cpp](#file-stacks_queues-queues-cpp) *(C++, 36 lines)*
  - [stacks_queues/queues.java](#file-stacks_queues-queues-java) *(Java, 36 lines)*
  - [stacks_queues/queues.py](#file-stacks_queues-queues-py) *(Python, 29 lines)*
  - [stacks_queues/stacks.cpp](#file-stacks_queues-stacks-cpp) *(C++, 36 lines)*
  - [stacks_queues/stacks.java](#file-stacks_queues-stacks-java) *(Java, 33 lines)*
  - [stacks_queues/stacks.py](#file-stacks_queues-stacks-py) *(Python, 25 lines)*
- **[`strings/`](#dir-strings)** (3 files)
  - [strings/replace_words.py](#file-strings-replace_words-py) *(Python, 57 lines)*
  - [strings/trie.py](#file-strings-trie-py) *(Python, 56 lines)*
  - [strings/z.py](#file-strings-z-py) *(Python, 48 lines)*
- **[`trees/`](#dir-trees)** (8 files)
  - [trees/01_Recursion/basic_tree_recusion.cpp](#file-trees-01_recursion-basic_tree_recusion-cpp) *(C++, 71 lines)*
  - [trees/01_Recursion/trees_recursion.py](#file-trees-01_recursion-trees_recursion-py) *(Python, 113 lines)*
  - [trees/01_Recursion/types_of_trees.cpp](#file-trees-01_recursion-types_of_trees-cpp) *(C++, 127 lines)*
  - [trees/diameter.py](#file-trees-diameter-py) *(Python, 39 lines)*
  - [trees/lca.py](#file-trees-lca-py) *(Python, 40 lines)*
  - [trees/root_to_leaf_path.py](#file-trees-root_to_leaf_path-py) *(Python, 42 lines)*
  - [trees/root_to_node_path.py](#file-trees-root_to_node_path-py) *(Python, 45 lines)*
  - [trees/trees.py](#file-trees-trees-py) *(Python, 93 lines)*
- **[Companion Input & Data Files](#companion-data-files)** (6 files)
  - [design_patterns/04_Factory/data.csv](#file-design_patterns-04_factory-data-csv) *(CSV, 5 lines)*
  - [design_patterns/04_Factory/data.json](#file-design_patterns-04_factory-data-json) *(JSON, 22 lines)*
  - [design_patterns/04_Factory/data.xml](#file-design_patterns-04_factory-data-xml) *(XML, 22 lines)*
  - [graphs/in.txt](#file-graphs-in-txt) *(Plain Text, 11 lines)*
  - [graphs/in2.txt](#file-graphs-in2-txt) *(Plain Text, 5 lines)*
  - [graphs/in3.txt](#file-graphs-in3-txt) *(Plain Text, 6 lines)*

---

<a id="dir-arrays"></a>
## Directory: `arrays/`

<a id="file-arrays-arrangement-py"></a>
### `arrays/arrangement.py`

- **Language:** Python
- **Path:** `arrays/arrangement.py`
- **Lines:** 29
- [↑ Back to Top](#table-of-contents)

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

<a id="file-arrays-arrangement2-py"></a>
### `arrays/arrangement2.py`

- **Language:** Python
- **Path:** `arrays/arrangement2.py`
- **Lines:** 29
- [↑ Back to Top](#table-of-contents)

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

<a id="file-arrays-arrangement3-py"></a>
### `arrays/arrangement3.py`

- **Language:** Python
- **Path:** `arrays/arrangement3.py`
- **Lines:** 29
- [↑ Back to Top](#table-of-contents)

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

<a id="file-arrays-custom_sort-cpp"></a>
### `arrays/custom_sort.cpp`

- **Language:** C++
- **Path:** `arrays/custom_sort.cpp`
- **Lines:** 46
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

bool compare_1(int a, int b) {
    string str_a = to_string(a);  // "9"
    string str_b = to_string(b);  // "98"

    string ab = str_a + str_b;
    string ba = str_b + str_a;

    // "998" > "989"
    return ab > ba;
}

bool compare_2(string a, string b) {
   return a.length() < b.length();
}

int main() {
    vector<int> nums = {9, 41, 98, 1, 7, 24, 53, 82};

    // Arrange them to form the largest number
    sort(nums.begin(), nums.end(), compare_1);

    for (auto x: nums)
        cout << x;
    cout << endl;

    string s = "i am a data scientist and i teach at heycoach";

    vector<string> words;

    // Learn it later: Splitting the sentence into the array of words
    stringstream str(s);
    string word;
    while (str >> word) 
        words.push_back(word);

    sort(words.begin(), words.end(), compare_2);

    for (auto x: words)
        cout << x << " ";
    cout << endl;

    return 0;
}
```

---

<a id="file-arrays-custom_sort-py"></a>
### `arrays/custom_sort.py`

- **Language:** Python
- **Path:** `arrays/custom_sort.py`
- **Lines:** 7
- [↑ Back to Top](#table-of-contents)

```python
s = "i am a data scientist and i teach at heycoach"

words = s.split(" ")

words.sort(key=len)

print(" ".join(words))
```

---

<a id="file-arrays-leetcode_sliding_window_map_76-cpp"></a>
### `arrays/leetcode_sliding_window_map_76.cpp`

- **Language:** C++
- **Path:** `arrays/leetcode_sliding_window_map_76.cpp`
- **Lines:** 58
- [↑ Back to Top](#table-of-contents)

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        // Lets create the first map for t
        map<char, int> t_freq;
        for (char c: t)
            t_freq[c]++;

        // How many unique chars are there in t
        int required_unique = t_freq.size();

        // Window, i to j in s, I need to make a map for that well
        map<char, int> window_freq;

        // Couple of variables
        int min_len = 10e6, min_window_left = 0, window_size = 0;
        int i = 0, j = 0;

        // Sliding window
        while (j < s.length()) {

            char c = s[j];
            window_freq[c]++;

            // Checking if the solution is kinda reached

            // find() == end() : element is not present
            if (t_freq.find(c) != t_freq.end() && window_freq[c] == t_freq[c])
                window_size++;

            // Can I shed elements from i'th side
            while (i <= j && window_size == required_unique) {
                // Update the minimum value of the length
                if (min_len > j - i + 1) {
                    min_len = j - i + 1;
                    min_window_left = i;
                }

                // Left char is 
                char left_char = s[i];

                // Can I remove this from window_freq
                window_freq[left_char]--;

                if (t_freq.find(left_char) != t_freq.end() && window_freq[left_char] < t_freq[left_char]) {
                    window_size--;
                }

                i++;
            }
            j++; 

            cout << i  << " " << j << endl;
        }

        return min_len == 10e6 ? "" : s.substr(min_window_left, min_len);
    }
};
```

---

<a id="file-arrays-maps-cpp"></a>
### `arrays/maps.cpp`

- **Language:** C++
- **Path:** `arrays/maps.cpp`
- **Lines:** 41
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

bool compare(pair<char, int> a, pair<char, int> b) {
    if (a.second > b.second)
        return true;
    else if (a.first < b.first)
        return true;
    return false;
}

int main() {

    map<char, int> m;  // Usecase: name : frequency

    string temp; cin >> temp;
    for (auto character: temp) {
        m[character]++;
    }

    // Interesting problem: Sort on frequencies
    vector<pair<char, int>> char_frequency;

    for (auto x: m) {
        char_frequency.push_back({x.first, x.second});
    }

    sort(char_frequency.begin(), char_frequency.end(), compare);

    string ans = "";
    for (auto x: char_frequency) {
        // cout << x.first << " " << x.second << endl;
        while (x.second--) {
            ans += x.first;
        }
    }

    cout << ans << endl;

    return 0;
}
```

---

<a id="file-arrays-sets-cpp"></a>
### `arrays/sets.cpp`

- **Language:** C++
- **Path:** `arrays/sets.cpp`
- **Lines:** 27
- [↑ Back to Top](#table-of-contents)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {

    set<char> s;  // Also sorts your unique values: unordered_set is also available.

    string temp; cin >> temp;

    for (auto c: temp) 
        s.insert(c);

    for (auto x: s)
        cout << x << " ";
    cout << endl;

    cout << s.size() << endl;

    char c1 = 'z'; 

    if (s.find(c1) == s.end()) {
        cout << c1 << " is not present.\n";
    } else 
        cout << "Present.\n";

    return 0;
}
```

---

<a id="file-arrays-sets-py"></a>
### `arrays/sets.py`

- **Language:** Python
- **Path:** `arrays/sets.py`
- **Lines:** 3
- [↑ Back to Top](#table-of-contents)

```python
s = "ssgysyqa"

print(set(s))

```

---

<a id="file-arrays-sort-py"></a>
### `arrays/sort.py`

- **Language:** Python
- **Path:** `arrays/sort.py`
- **Lines:** 100
- [↑ Back to Top](#table-of-contents)

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

<a id="file-arrays-stable_binary_arr-cpp"></a>
### `arrays/stable_binary_arr.cpp`

- **Language:** C++
- **Path:** `arrays/stable_binary_arr.cpp`
- **Lines:** 52
- [↑ Back to Top](#table-of-contents)

```cpp
#include<stdio.h>
#include<iostream>
using namespace std;

class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        int size = zero + one;
        int arr[size];
        for(int i=0;i<size;i++){
            arr[i] = 0;
        }
        int count = 0;
        count = stableArray(zero,one,size,count,arr);
        return count;
    }

    int stableArray(int zero, int one, int size, int count,int arr[]){
        if(size < 0){
            return count;
        }
        arr[size-1] = 1;
        if(isStable(zero,one,size,arr))
        return 1;
        return count+max(stableArray(zero,one,size-1,count,arr),stableArray(zero,one,size,count,arr));
    }

    bool isStable(int zero,int one,int size, int arr[]){
        int countZero = 0;
        int countOne = 0;
        for(int i=0;i<size;i++){
            if(arr[i]==0){
                countZero++;
            }else{
                countOne++;
            }
            if(countZero>zero)
            return false;
            if(countOne>one)
            return false;
        }
        return true;
    }
};

int main(){
    Solution s;
    int zero = 2;
    int one = 1;
    int limit = 3;
    cout<<s.numberOfStableArrays(zero,one,limit)<<endl;
}
```

---

<a id="file-arrays-toggle-py"></a>
### `arrays/toggle.py`

- **Language:** Python
- **Path:** `arrays/toggle.py`
- **Lines:** 63
- [↑ Back to Top](#table-of-contents)

```python
import time

def timer(func):
    def wrapper_func(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print("Time taken by {} is {} seconds.".format(func.__name__, time.time()-t))
        return result
    return wrapper_func

# ------------------------------------------------------------------------------------

import random

n = 100000
q = 5000
bulbs = [random.choice([0, 1]) for _ in range(n)]
bulbs2 = bulbs.copy()

# print(bulbs)

queries = []
for _ in range(q):
    l = random.randint(0, n-1)
    m = random.randint(l, n-1)
    queries.append((l, m))

# print(queries)
    
# O(nq)
@timer
def bulb_toggle(bulbs, queries):
    for query in queries:
        l, m = query
        for i in range(l, m+1):
            bulbs[i] = 1 - bulbs[i]
    print("Total lit bulbs: ", sum(bulbs))

# O(n+q)
@timer
def bulb_toggle_prefix_sum(bulbs, queries):
    diff_array = [0]*(n+1) 

    for query in queries:
        l, m = query
        diff_array[l] += 1
        diff_array[m+1] -= 1
    # print(sum(diff_array))

    prefix_array = [0]*n
    prefix_array[0] = diff_array[0]
    for i in range(1, n):
        prefix_array[i] = prefix_array[i - 1] + diff_array[i]

    for i in range(len(bulbs)):
        if prefix_array[i]%2 != 0:
            bulbs[i] = 1 - bulbs[i]
    
    print("Total lit bulbs: ", sum(bulbs))


bulb_toggle(bulbs, queries)
bulb_toggle_prefix_sum(bulbs2, queries)
```

---

<a id="dir-cpp_language"></a>
## Directory: `cpp_language/`

<a id="file-cpp_language-01_array_operations-sort-cpp"></a>
### `cpp_language/01_Array_Operations/sort.cpp`

- **Language:** C++
- **Path:** `cpp_language/01_Array_Operations/sort.cpp`
- **Lines:** 59
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {

    // Normal integer array
    int arr[] = {3, 4, 7, 1, 2, 9, 0, 2, 6, 5};
    int n = sizeof(arr)/sizeof(arr[0]);  
    sort(arr, arr+n);

    for (int i = 0; i < n; i++) 
        cout << arr[i] << " ";
    cout << endl;

    // Vector sort
    vector<int> arr2 = {3, 4, 7, 1, 2, 9, 0, 2, 6, 5};
    sort(arr2.begin(), arr2.end());

    for (auto x: arr2)
        cout << x << " ";
    cout << endl;

    // Normal string array
    string arr3[] = {"sagar", "hari", "vishnu", "ashutosh"};
    int n2 = sizeof(arr3)/sizeof(arr3[0]);
    sort(arr3, arr3+n2);

    for (int i = 0; i < n2; i++)
        cout << arr3[i] << " ";
    cout << endl;

    // Vector sort of strings
    vector<string> arr4 = {"sagar", "hari", "vishnu", "ashutosh"};
    sort(arr4.begin(), arr4.end());

    for (auto x: arr4)
        cout << x << " ";
    cout << endl;

    // Use greater<int>() to sort in descending order
    int arr5[] = {3, 4, 7, 1, 2, 9, 0, 2, 6, 5};
    int n3 = sizeof(arr)/sizeof(arr[0]);  
    sort(arr5, arr5+n, greater<int>());

    for (int i = 0; i < n; i++) 
        cout << arr5[i] << " ";
    cout << endl;

    // Use greater<string>() to sort strings in descending order
    vector<string> arr6 = {"sagar", "hari", "vishnu", "ashutosh"};
    sort(arr6.begin(), arr6.end(), greater<string>());

    for (auto x: arr6)
        cout << x << " ";
    cout << endl;


    return 0;
}
```

---

<a id="dir-design_patterns"></a>
## Directory: `design_patterns/`

<a id="file-design_patterns-01_singleton-logger-java"></a>
### `design_patterns/01_Singleton/Logger.java`

- **Language:** Java
- **Path:** `design_patterns/01_Singleton/Logger.java`
- **Lines:** 44
- [↑ Back to Top](#table-of-contents)

```java
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class Logger {
    private static Logger instance;
    private static final Object lock = new Object();
    private final String logFile = "app.log";

    private Logger() {
        // private constructor to prevent instantiation
    }

    public static Logger getInstance() {
        if (instance == null) {
            synchronized (lock) {
                if (instance == null) {
                    instance = new Logger();
                }
            }
        }
        return instance;
    }

    public void log(String message) {
        try (FileWriter fw = new FileWriter(logFile, true);
             PrintWriter pw = new PrintWriter(fw)) {
            pw.println(message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Example usage
    public static void main(String[] args) {
        Logger logger1 = Logger.getInstance();
        Logger logger2 = Logger.getInstance();

        logger1.log("Logging from logger1");
        logger2.log("Logging from logger2");

        System.out.println("Logger1 and Logger2 are the same instance: " + (logger1 == logger2));
    }
}

```

---

<a id="file-design_patterns-01_singleton-logger-js"></a>
### `design_patterns/01_Singleton/logger.js`

- **Language:** JavaScript
- **Path:** `design_patterns/01_Singleton/logger.js`
- **Lines:** 26
- [↑ Back to Top](#table-of-contents)

```javascript
const fs = require('fs');
const path = require('path');

class Logger {
    constructor() {
        if (Logger.instance) {
            return Logger.instance;
        }
        
        this._logFile = path.join(__dirname, 'app.log');
        Logger.instance = this;
    }

    log(message) {
        fs.appendFileSync(this._logFile, `${message}\n`);
    }
}

// Example usage
const logger1 = new Logger();
const logger2 = new Logger();

logger1.log("Logging from logger1");
logger2.log("Logging from logger2");

console.log(`Logger1 and Logger2 are the same instance: ${logger1 === logger2}`);

```

---

<a id="file-design_patterns-01_singleton-logger-py"></a>
### `design_patterns/01_Singleton/logger.py`

- **Language:** Python
- **Path:** `design_patterns/01_Singleton/logger.py`
- **Lines:** 31
- [↑ Back to Top](#table-of-contents)

```python
import threading

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._log_file = "app.log"
        self._initialized = True

    def log(self, message):
        with open(self._log_file, "a") as file:
            file.write(f"{message}\n")

# Example usage
logger1 = Logger()
logger2 = Logger()

logger1.log("Logging from logger1")
logger2.log("Logging from logger2")

print(f"Logger1 and Logger2 are the same instance: {logger1 is logger2}")

```

---

<a id="file-design_patterns-02_prototype-socialmediapost-java"></a>
### `design_patterns/02_Prototype/SocialMediaPost.java`

- **Language:** Java
- **Path:** `design_patterns/02_Prototype/SocialMediaPost.java`
- **Lines:** 69
- [↑ Back to Top](#table-of-contents)

```java
import java.util.ArrayList;
import java.util.List;

public class SocialMediaPost implements Cloneable {
    private String content;
    private String author;
    private int likes;
    private List<String> comments;

    public SocialMediaPost(String content, String author, int likes, List<String> comments) {
        this.content = content;
        this.author = author;
        this.likes = likes;
        this.comments = comments;
    }

    public SocialMediaPost(String content, String author) {
        this(content, author, 0, new ArrayList<>());
    }

    public void addComment(String comment) {
        this.comments.add(comment);
    }

    public void display() {
        System.out.println("Content: " + this.content);
        System.out.println("Author: " + this.author);
        System.out.println("Likes: " + this.likes);
        System.out.println("Comments: " + this.comments);
    }

    // For deep copy purposes
    @Override
    public SocialMediaPost clone() {
        try {
            // Perform a deep copy of the object
            SocialMediaPost clonedPost = (SocialMediaPost) super.clone();
            clonedPost.comments = new ArrayList<>(this.comments);
            return clonedPost;
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        // Create a prototype post
        SocialMediaPost originalPost = new SocialMediaPost("Excited to launch our new product!", "John Doe");

        // Add some comments
        originalPost.addComment("Looks great!");
        originalPost.addComment("Can't wait to try it out!");

        // Display original post
        System.out.println("Original Post:");
        originalPost.display();
        System.out.println();

        // Clone the original post and make slight modifications
        SocialMediaPost clonedPost = originalPost.clone();
        clonedPost.content = "Check out our latest update!";
        clonedPost.addComment("Interesting...");
        clonedPost.likes = 10;

        // Display cloned post
        System.out.println("Cloned Post:");
        clonedPost.display();
    }
}

```

---

<a id="file-design_patterns-02_prototype-posts-js"></a>
### `design_patterns/02_Prototype/posts.js`

- **Language:** JavaScript
- **Path:** `design_patterns/02_Prototype/posts.js`
- **Lines:** 52
- [↑ Back to Top](#table-of-contents)

```javascript
class SocialMediaPost {
    constructor(content, author, likes=0, comments=[]) {
        this.content = content;
        this.author = author;
        this.likes = likes;
        this.comments = comments;
    }

    addComment(comment) {
        this.comments.push(comment);
    }

    display() {
        console.log("Content:", this.content);
        console.log("Author:", this.author);
        console.log("Likes:", this.likes);
        console.log("Comments:", this.comments);
    }

    clone() {
        // Perform a deep copy of the object
        return new SocialMediaPost(
            this.content,
            this.author,
            this.likes,
            this.comments.slice() // Create a shallow copy of comments array
        );
    }
}

// Example of using the Prototype pattern
// Create a prototype post
let originalPost = new SocialMediaPost("Excited to launch our new product!", "John Doe");

// Add some comments
originalPost.addComment("Looks great!");
originalPost.addComment("Can't wait to try it out!");

// Display original post
console.log("Original Post:");
originalPost.display();
console.log();

// Clone the original post and make slight modifications
let clonedPost = originalPost.clone();
clonedPost.content = "Check out our latest update!";
clonedPost.addComment("Interesting...");
clonedPost.likes = 10;

// Display cloned post
console.log("Cloned Post:");
clonedPost.display();

```

---

<a id="file-design_patterns-02_prototype-posts-py"></a>
### `design_patterns/02_Prototype/posts.py`

- **Language:** Python
- **Path:** `design_patterns/02_Prototype/posts.py`
- **Lines:** 46
- [↑ Back to Top](#table-of-contents)

```python
import copy

class SocialMediaPost:
    def __init__(self, content, author, likes=0, comments=[]):
        self.content = content
        self.author = author
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment):
        self.comments.append(comment)

    def display(self):
        print("Content:", self.content)
        print("Author:", self.author)
        print("Likes:", self.likes)
        print("Comments:", self.comments)

    def clone(self):
        # Use the built-in copy module to perform a deep copy of the object
        return copy.deepcopy(self)


# Example of using the Prototype pattern
if __name__ == "__main__":
    # Create a prototype post
    original_post = SocialMediaPost("Excited to launch our new product!", "John Doe")

    # Add some comments
    original_post.add_comment("Looks great!")
    original_post.add_comment("Can't wait to try it out!")

    # Display original post
    print("Original Post:")
    original_post.display()
    print()

    # Clone the original post and make slight modifications
    cloned_post = original_post.clone()
    cloned_post.content = "Check out our latest update!"
    cloned_post.add_comment("Interesting...")
    cloned_post.likes = 10

    # Display cloned post
    print("Cloned Post:")
    cloned_post.display()

```

---

<a id="file-design_patterns-03_builder-main-java"></a>
### `design_patterns/03_Builder/Main.java`

- **Language:** Java
- **Path:** `design_patterns/03_Builder/Main.java`
- **Lines:** 76
- [↑ Back to Top](#table-of-contents)

```java
import java.util.ArrayList;
import java.util.List;

class Sandwich {
    private List<String> ingredients;
    private String bread;
    private List<String> condiments;

    public Sandwich() {
        this.ingredients = new ArrayList<>();
        this.bread = "";
        this.condiments = new ArrayList<>();
    }

    public void addIngredient(String ingredient) {
        this.ingredients.add(ingredient);
    }

    public void setBread(String bread) {
        this.bread = bread;
    }

    public void addCondiment(String condiment) {
        this.condiments.add(condiment);
    }

    @Override
    public String toString() {
        return "Sandwich with " + String.join(", ", this.ingredients) +
               " on " + this.bread + " bread with " + String.join(", ", this.condiments) + ".";
    }
}

class SandwichBuilder {
    private Sandwich sandwich;

    public SandwichBuilder() {
        this.sandwich = new Sandwich();
    }

    public SandwichBuilder addIngredients(List<String> ingredients) {
        for (String ingredient : ingredients) {
            this.sandwich.addIngredient(ingredient);
        }
        return this;
    }

    public SandwichBuilder addBread(String bread) {
        this.sandwich.setBread(bread);
        return this;
    }

    public SandwichBuilder addCondiments(List<String> condiments) {
        for (String condiment : condiments) {
            this.sandwich.addCondiment(condiment);
        }
        return this;
    }

    public Sandwich build() {
        return this.sandwich;
    }
}

public class Main {
    public static void main(String[] args) {
        SandwichBuilder builder = new SandwichBuilder();
        Sandwich sandwich = builder
                .addIngredients(List.of("Ham", "Cheese"))
                .addBread("Wheat")
                .addCondiments(List.of("Mayo", "Mustard"))
                .build();

        System.out.println(sandwich.toString());
    }
}

```

---

<a id="file-design_patterns-03_builder-sandwich-js"></a>
### `design_patterns/03_Builder/sandwich.js`

- **Language:** JavaScript
- **Path:** `design_patterns/03_Builder/sandwich.js`
- **Lines:** 63
- [↑ Back to Top](#table-of-contents)

```javascript
class Sandwich {
    constructor() {
        this.ingredients = [];
        this.bread = "";
        this.condiments = [];
    }

    addIngredient(ingredient) {
        this.ingredients.push(ingredient);
    }

    setBread(bread) {
        this.bread = bread;
    }

    addCondiment(condiment) {
        this.condiments.push(condiment);
    }

    toString() {
        return `Sandwich with ${this.ingredients.join(", ")} on ${this.bread} bread with ${this.condiments.join(", ")}.`;
    }
}

class SandwichBuilder {
    constructor() {
        this.sandwich = new Sandwich();
    }

    addIngredients(ingredients) {
        for (let ingredient of ingredients) {
            this.sandwich.addIngredient(ingredient);
        }
        return this;
    }

    addBread(bread) {
        this.sandwich.setBread(bread);
        return this;
    }

    addCondiments(condiments) {
        for (let condiment of condiments) {
            this.sandwich.addCondiment(condiment);
        }
        return this;
    }

    build() {
        return this.sandwich;
    }
}

// Client code
const builder = new SandwichBuilder();

const sandwich = builder
    .addBread("Wheat")
    .addIngredients(["Ham", "Cheese"])
    .addCondiments(["Mayo", "Mustard"])
    .build();

console.log(sandwich.toString());
```

---

<a id="file-design_patterns-03_builder-sandwich-py"></a>
### `design_patterns/03_Builder/sandwich.py`

- **Language:** Python
- **Path:** `design_patterns/03_Builder/sandwich.py`
- **Lines:** 48
- [↑ Back to Top](#table-of-contents)

```python
class Sandwich:
    def __init__(self):
        self.ingredients = []
        self.bread = ""
        self.condiments = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def set_bread(self, bread):
        self.bread = bread

    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f"Sandwich with {', '.join(self.ingredients)} on {self.bread} bread with {', '.join(self.condiments)}."


class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            self.sandwich.add_ingredient(ingredient)
        return self

    def add_bread(self, bread):
        self.sandwich.set_bread(bread)
        return self

    def add_condiments(self, condiments):
        for condiment in condiments:
            self.sandwich.add_condiment(condiment)
        return self

    def build(self):
        return self.sandwich


# Client code
builder = SandwichBuilder()
sandwich = builder.add_ingredients(["Ham", "Cheese"]).add_bread("Wheat").add_condiments(["Mayo", "Mustard"]).build()

print(sandwich)



```

---

<a id="file-design_patterns-04_factory-main-java"></a>
### `design_patterns/04_Factory/Main.java`

- **Language:** Java
- **Path:** `design_patterns/04_Factory/Main.java`
- **Lines:** 81
- [↑ Back to Top](#table-of-contents)

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

// Abstract class for DataReader
abstract class DataReader {
    abstract List<List<String>> readData(String filePath) throws IOException;
}

// Concrete implementations of DataReader
class CSVDataReader extends DataReader {
    @Override
    List<List<String>> readData(String filePath) throws IOException {
        List<List<String>> data = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                List<String> row = new ArrayList<>();
                String[] values = line.split(",");
                for (String value : values) {
                    row.add(value);
                }
                data.add(row);
            }
        }
        return data;
    }
}

class JSONDataReader extends DataReader {
    @Override
    List<List<String>> readData(String filePath) throws IOException {
        throw new UnsupportedOperationException("JSONDataReader not implemented");
    }
}

class XMLDataReader extends DataReader {
    @Override
    List<List<String>> readData(String filePath) throws IOException {
        throw new UnsupportedOperationException("XMLDataReader not implemented");
    }
}

// Factory class for creating data readers
class DataReaderFactory {
    static DataReader createDataReader(String filePath) {
        String fileExtension = filePath.substring(filePath.lastIndexOf('.')).toLowerCase();
        switch (fileExtension) {
            case ".csv":
                return new CSVDataReader();
            case ".json":
                return new JSONDataReader();
            case ".xml":
                return new XMLDataReader();
            default:
                throw new IllegalArgumentException("Unsupported file type");
        }
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Main <file_path>");
            System.exit(1);
        }

        String filePath = args[0];

        try {
            DataReader dataReader = DataReaderFactory.createDataReader(filePath);
            List<List<String>> data = dataReader.readData(filePath);
            System.out.println("Data read from " + filePath + ": " + data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

---

<a id="file-design_patterns-04_factory-data_reader-js"></a>
### `design_patterns/04_Factory/data_reader.js`

- **Language:** JavaScript
- **Path:** `design_patterns/04_Factory/data_reader.js`
- **Lines:** 71
- [↑ Back to Top](#table-of-contents)

```javascript
const fs = require('fs');
const path = require('path');

// Abstract class for DataReader
class DataReader {
    readData(file_path) {}
}

// Concrete implementations of DataReader
class CSVDataReader extends DataReader {
    readData(file_path) {
        const data = fs.readFileSync(file_path, 'utf8').split('\n').map(row => row.split(','));
        return data;
    }
}

class JSONDataReader extends DataReader {
    readData(file_path) {
        const data = JSON.parse(fs.readFileSync(file_path, 'utf8'));
        return data;
    }
}

class XMLDataReader extends DataReader {
    readData(file_path) {
        const xmlContent = fs.readFileSync(file_path, 'utf8');
        const data = this.parseXML(xmlContent);
        return data;
    }

    parseXML(xmlContent) {
        const parser = new Parser();
        const data = {};
        parser.parseString(xmlContent, (err, result) => {
            if (err) {
                console.error(err);
                return;
            }
            data.root = result;
        });
        return data;
    }
}

// Factory class for creating data readers
class DataReaderFactory {
    static createDataReader(file_path) {
        const file_extension = path.extname(file_path).toLowerCase();
        if (file_extension === ".csv") {
            return new CSVDataReader();
        } else if (file_extension === ".json") {
            return new JSONDataReader();
        } else if (file_extension === ".xml") {
            return new XMLDataReader();
        } else {
            throw new Error("Unsupported file type");
        }
    }
}

// Client code
if (process.argv.length !== 3) {
    console.log("Usage: node script.js <file_path>");
    process.exit(1);
}

const file_path = process.argv[2];

const dataReader = DataReaderFactory.createDataReader(file_path);
const data = dataReader.readData(file_path);
console.log("Data read from", file_path, ":", data);

```

---

<a id="file-design_patterns-04_factory-data_reader-py"></a>
### `design_patterns/04_Factory/data_reader.py`

- **Language:** Python
- **Path:** `design_patterns/04_Factory/data_reader.py`
- **Lines:** 66
- [↑ Back to Top](#table-of-contents)

```python
import csv
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
import os
import sys

# Abstract class for DataReader
class DataReader(ABC):
    @abstractmethod
    def read_data(self, file_path):
        pass

# Concrete implementations of DataReader
class CSVDataReader(DataReader):
    def read_data(self, file_path):
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data

class JSONDataReader(DataReader):
    def read_data(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

class XMLDataReader(DataReader):
    def read_data(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for element in root:
            element_data = {}
            for child in element:
                element_data[child.tag] = child.text
            data.append(element_data)
        return data

# Factory class for creating data readers
class DataReaderFactory:
    @staticmethod
    def create_data_reader(file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == ".csv":
            return CSVDataReader()
        elif file_extension == ".json":
            return JSONDataReader()
        elif file_extension == ".xml":
            return XMLDataReader()
        else:
            raise ValueError("Unsupported file type")

# Client code
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    data_reader = DataReaderFactory.create_data_reader(file_path)
    data = data_reader.read_data(file_path)
    print("Data read from", file_path, ":", data)
```

---

<a id="file-design_patterns-05_facade-main-java"></a>
### `design_patterns/05_Facade/Main.java`

- **Language:** Java
- **Path:** `design_patterns/05_Facade/Main.java`
- **Lines:** 70
- [↑ Back to Top](#table-of-contents)

```java
// Define the appliance classes
class Light {
    void on() {
        System.out.println("Light is on");
    }

    void off() {
        System.out.println("Light is off");
    }
}

class Television {
    void on() {
        System.out.println("Television is on");
    }

    void off() {
        System.out.println("Television is off");
    }
}

class AirConditioner {
    void on() {
        System.out.println("Air Conditioner is on");
    }

    void off() {
        System.out.println("Air Conditioner is off");
    }
}

// Define the HomeFacade class
class HomeFacade {
    private Light light;
    private Television tv;
    private AirConditioner ac;

    public HomeFacade() {
        this.light = new Light();
        this.tv = new Television();
        this.ac = new AirConditioner();
    }

    public void eveningMode() {
        System.out.println("Setting evening mode...");
        light.on();
        tv.on();
        ac.on();
    }

    public void morningMode() {
        System.out.println("Setting morning mode...");
        light.off();
        tv.off();
        ac.off();
    }
}

// Using the HomeFacade to control appliances
public class Main {
    public static void main(String[] args) {
        HomeFacade home = new HomeFacade();

        // Activating evening mode
        home.eveningMode();
        System.out.println();
        // Activating morning mode
        home.morningMode();
    }
}

```

---

<a id="file-design_patterns-05_facade-home-js"></a>
### `design_patterns/05_Facade/home.js`

- **Language:** JavaScript
- **Path:** `design_patterns/05_Facade/home.js`
- **Lines:** 62
- [↑ Back to Top](#table-of-contents)

```javascript
// Define the appliance classes
class Light {
  on() {
    console.log('Light is on');
  }

  off() {
    console.log('Light is off');
  }
}

class Television {
  on() {
    console.log('Television is on');
  }

  off() {
    console.log('Television is off');
  }
}

class AirConditioner {
  on() {
    console.log('Air Conditioner is on');
  }

  off() {
    console.log('Air Conditioner is off');
  }
}

// Define the HomeFacade class
class HomeFacade {
  constructor() {
    this.light = new Light();
    this.tv = new Television();
    this.ac = new AirConditioner();
  }

  eveningMode() {
    console.log('Setting evening mode...');
    this.light.on();
    this.tv.on();
    this.ac.on();
  }

  morningMode() {
    console.log('Setting morning mode...');
    this.light.off();
    this.tv.off();
    this.ac.off();
  }
}

// Using the HomeFacade to control appliances
const home = new HomeFacade();

// Activating evening mode
home.eveningMode();
console.log();
// Activating morning mode
home.morningMode();

```

---

<a id="file-design_patterns-05_facade-home-py"></a>
### `design_patterns/05_Facade/home.py`

- **Language:** Python
- **Path:** `design_patterns/05_Facade/home.py`
- **Lines:** 50
- [↑ Back to Top](#table-of-contents)

```python
# Define the appliance classes
class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")

class Television:
    def on(self):
        print("Television is on")

    def off(self):
        print("Television is off")

class AirConditioner:
    def on(self):
        print("Air Conditioner is on")

    def off(self):
        print("Air Conditioner is off")

# Define the HomeFacade class
class HomeFacade:
    def __init__(self):
        self.light = Light()
        self.tv = Television()
        self.ac = AirConditioner()

    def evening_mode(self):
        print("Setting evening mode...")
        self.light.on()
        self.tv.on()
        self.ac.on()

    def morning_mode(self):
        print("Setting morning mode...")
        self.light.off()
        self.tv.off()
        self.ac.off()

# Using the HomeFacade to control appliances
if __name__ == "__main__":
    home = HomeFacade()

    # Activating evening mode
    home.evening_mode()
    print()
    # Activating morning mode
    home.morning_mode()

```

---

<a id="file-design_patterns-06_proxy-main-java"></a>
### `design_patterns/06_Proxy/Main.java`

- **Language:** Java
- **Path:** `design_patterns/06_Proxy/Main.java`
- **Lines:** 64
- [↑ Back to Top](#table-of-contents)

```java
import java.util.concurrent.TimeUnit;

interface Image {
    void display();
}

class RealImage implements Image {
    private String filename;

    public RealImage(String filename) {
        this.filename = filename;
        loadImage();
    }

    private void loadImage() {
        System.out.println("Loading image '" + filename + "' from disk...");
        try {
            // Simulate the delay of loading a large file
            TimeUnit.SECONDS.sleep(2);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Image '" + filename + "' loaded.");
    }

    @Override
    public void display() {
        System.out.println("Displaying " + filename);
    }
}

class ProxyImage implements Image {
    private String filename;
    private RealImage realImage;

    public ProxyImage(String filename) {
        this.filename = filename;
    }

    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }
}

public class Main {
    public static void main(String[] args) {
        Image[] images = {
            new ProxyImage("image1.jpg"),
            new ProxyImage("image2.jpg"),
            new ProxyImage("image3.jpg")
        };

        System.out.println("User is opening the image viewer.");
        images[0].display();
        System.out.println("User navigates to the next image.");
        images[1].display();
        System.out.println("User goes back to the first image.");
        images[0].display();
    }
}

```

---

<a id="file-design_patterns-06_proxy-image_renderer-js"></a>
### `design_patterns/06_Proxy/image_renderer.js`

- **Language:** JavaScript
- **Path:** `design_patterns/06_Proxy/image_renderer.js`
- **Lines:** 62
- [↑ Back to Top](#table-of-contents)

```javascript
// This is an abstract base class => To be inherited. 
class Image {
    display() {
        throw new Error("This method should be overridden.");
    }
}

class RealImage extends Image {
    constructor(filename) {
        super();
        this.filename = filename;
        this._loadImage();
    }

    _loadImage() {
        console.log(`Loading image '${this.filename}' from disk...`);
        // Simulate the delay of loading a large file
        setTimeout(() => {
            console.log(`Image '${this.filename}' loaded.`);
        }, 2000);
    }

    display() {
        console.log(`Displaying ${this.filename}`);
    }
}

class ProxyImage extends Image {
    constructor(filename) {
        super();
        this.filename = filename;
        this._realImage = null;
    }

    display() {
        if (this._realImage === null) {
            this._realImage = new RealImage(this.filename);
        }
        this._realImage.display();
    }
}

function main() {
    const images = [
        new ProxyImage("image1.jpg"),
        new ProxyImage("image2.jpg"),
        new ProxyImage("image3.jpg")
    ];

    console.log("User is opening the image viewer.");
    images[0].display();
    setTimeout(() => {
        console.log("User navigates to the next image.");
        images[1].display();
        setTimeout(() => {
            console.log("User goes back to the first image.");
            images[0].display();
        }, 2500);
    }, 2500);
}

main();

```

---

<a id="file-design_patterns-06_proxy-image_renderer-py"></a>
### `design_patterns/06_Proxy/image_renderer.py`

- **Language:** Python
- **Path:** `design_patterns/06_Proxy/image_renderer.py`
- **Lines:** 49
- [↑ Back to Top](#table-of-contents)

```python
from abc import ABC, abstractmethod
import time

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_image()

    def _load_image(self):
        # Simulate loading image from disk
        print(f"Loading image '{self.filename}' from disk...")
        time.sleep(2)  # Simulate the delay of loading a large file
        print(f"Image '{self.filename}' loaded.")

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

def main():
    images = [
        ProxyImage("image1.jpg"),
        ProxyImage("image2.jpg"),
        ProxyImage("image3.jpg")
    ]

    # Simulate user interacting with the image viewer
    print("User is opening the image viewer.")
    images[0].display()  # Only now the real image is loaded and displayed
    print("User navigates to the next image.")
    images[1].display()  # The second image is now loaded and displayed
    print("User goes back to the first image.")
    images[0].display()  # The first image is already loaded, so just display it

if __name__ == "__main__":
    main()

```

---

<a id="file-design_patterns-07_iterator-main-java"></a>
### `design_patterns/07_Iterator/Main.java`

- **Language:** Java
- **Path:** `design_patterns/07_Iterator/Main.java`
- **Lines:** 128
- [↑ Back to Top](#table-of-contents)

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

// Book class
class Book {
    private String title;
    private String author;
    private int year;

    public Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    @Override
    public String toString() {
        return title + " by " + author + ", " + year;
    }
}

// Library class
class Library implements Iterable<Book> {
    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
    }

    @Override
    public Iterator<Book> iterator() {
        return new LibraryIterator(books);
    }

    public Iterable<Book> getBooksByAuthor(String author) {
        return new LibraryAuthorIterable(books, author);
    }

    public Iterable<Book> getBooksByYear(int year) {
        return new LibraryYearIterable(books, year);
    }
}

// LibraryIterator class
class LibraryIterator implements Iterator<Book> {
    private List<Book> books;
    private int index;

    public LibraryIterator(List<Book> books) {
        this.books = books;
        this.index = 0;
    }

    @Override
    public boolean hasNext() {
        return index < books.size();
    }

    @Override
    public Book next() {
        return books.get(index++);
    }
}

// LibraryAuthorIterable class
class LibraryAuthorIterable implements Iterable<Book> {
    private List<Book> books;

    public LibraryAuthorIterable(List<Book> books, String author) {
        this.books = new ArrayList<>();
        for (Book book : books) {
            if (book.toString().contains(author)) {
                this.books.add(book);
            }
        }
    }

    @Override
    public Iterator<Book> iterator() {
        return books.iterator();
    }
}

// LibraryYearIterable class
class LibraryYearIterable implements Iterable<Book> {
    private List<Book> books;

    public LibraryYearIterable(List<Book> books, int year) {
        this.books = new ArrayList<>();
        for (Book book : books) {
            if (book.toString().contains(Integer.toString(year))) {
                this.books.add(book);
            }
        }
    }

    @Override
    public Iterator<Book> iterator() {
        return books.iterator();
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        library.addBook(new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925));
        library.addBook(new Book("1984", "George Orwell", 1949));
        library.addBook(new Book("To Kill a Mockingbird", "Harper Lee", 1960));
        library.addBook(new Book("Animal Farm", "George Orwell", 1945));

        System.out.println("All books in the library:");
        for (Book book : library) {
            System.out.println(book);
        }

        System.out.println("\nBooks by George Orwell:");
        for (Book book : library.getBooksByAuthor("George Orwell")) {
            System.out.println(book);
        }

        System.out.println("\nBooks published in 1945:");
        for (Book book : library.getBooksByYear(1945)) {
            System.out.println(book);
        }
    }
}

```

---

<a id="file-design_patterns-07_iterator-books-js"></a>
### `design_patterns/07_Iterator/books.js`

- **Language:** JavaScript
- **Path:** `design_patterns/07_Iterator/books.js`
- **Lines:** 118
- [↑ Back to Top](#table-of-contents)

```javascript
class Book {
  constructor(title, author, year) {
    this.title = title;
    this.author = author;
    this.year = year;
  }

  toString() {
    return `${this.title} by ${this.author}, ${this.year}`;
  }
}

class Library {
  constructor() {
    this.books = [];
  }

  addBook(book) {
    this.books.push(book);
  }

  [Symbol.iterator]() {
    return new LibraryIterator(this.books);
  }

  getBooksByAuthor(author) {
    return new LibraryAuthorIterator(this.books, author);
  }

  getBooksByYear(year) {
    return new LibraryYearIterator(this.books, year);
  }
}

class LibraryIterator {
  constructor(books) {
    this._books = books;
    this._index = 0;
  }

  next() {
    if (this._index < this._books.length) {
      return { value: this._books[this._index++], done: false };
    } else {
      return { done: true };
    }
  }
}

class LibraryAuthorIterator {
  constructor(books, author) {
    this._books = books.filter((book) => book.author === author);
    this._index = 0;
  }

  [Symbol.iterator]() {
    return this;
  }

  next() {
    if (this._index < this._books.length) {
      return { value: this._books[this._index++], done: false };
    } else {
      return { done: true };
    }
  }
}

class LibraryYearIterator {
  constructor(books, year) {
    this._books = books.filter((book) => book.year === year);
    this._index = 0;
  }

  [Symbol.iterator]() {
    return this;
  }

  next() {
    if (this._index < this._books.length) {
      return { value: this._books[this._index++], done: false };
    } else {
      return { done: true };
    }
  }
}

// Usage example
const library = new Library();

library.addBook(new Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925));
library.addBook(new Book('1984', 'George Orwell', 1949));
library.addBook(new Book('To Kill a Mockingbird', 'Harper Lee', 1960));
library.addBook(new Book('Animal Farm', 'George Orwell', 1945));

console.log('All books in the library:');
// of => automatically calls next() for you, done flag as well! 
for (const book of library) {  // for loop is sequential 
  console.log(book.toString());
}

// How will you simulate pause? next() by yourself

console.log('\nBooks by George Orwell:');
for (const book of library.getBooksByAuthor('George Orwell')) {
  console.log(book.toString());
}

console.log('\nBooks published in 1945:');
for (const book of library.getBooksByYear(1945)) {
  console.log(book.toString());
}

// const iterator = library[Symbol.iterator]();

// console.log(iterator.next().value.toString())
// console.log(iterator.next().value.toString())
// console.log(iterator.next())

```

---

<a id="file-design_patterns-07_iterator-books-py"></a>
### `design_patterns/07_Iterator/books.py`

- **Language:** Python
- **Path:** `design_patterns/07_Iterator/books.py`
- **Lines:** 96
- [↑ Back to Top](#table-of-contents)

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.author}, {self.year}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return LibraryIterator(self.books)

    def get_books_by_author(self, author):
        return LibraryAuthorIterator(self.books, author)

    def get_books_by_year(self, year):
        return LibraryYearIterator(self.books, year)

class LibraryIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            result = self._books[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

class LibraryAuthorIterator:
    def __init__(self, books, author):
        self._books = [book for book in books if book.author == author]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            result = self._books[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

class LibraryYearIterator:
    def __init__(self, books, year):
        self._books = [book for book in books if book.year == year]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            result = self._books[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    library = Library()
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("Animal Farm", "George Orwell", 1945))

    print("All books in the library:")
    for book in library:
        print(book)

    print("\nBooks by George Orwell:")
    for book in library.get_books_by_author("George Orwell"):
        print(book)

    print("\nBooks published in 1945:")
    for book in library.get_books_by_year(1945):
        print(book)

    iterator = iter(library)
    print(iterator.__next__())
    print(iterator.__next__())
    print(next(iterator))
```

---

<a id="file-design_patterns-08_observer-main-java"></a>
### `design_patterns/08_Observer/Main.java`

- **Language:** Java
- **Path:** `design_patterns/08_Observer/Main.java`
- **Lines:** 77
- [↑ Back to Top](#table-of-contents)

```java
import java.util.ArrayList;
import java.util.List;

// Subject (Observable)
interface Subject {
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}

// Concrete Subject
class WeatherStation implements Subject {
    private Double temperature;
    private List<Observer> observers;

    public WeatherStation() {
        this.observers = new ArrayList<>();
    }

    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(temperature);
        }
    }

    public void setTemperature(Double temperature) {
        System.out.println("Setting temperature to: " + temperature);
        this.temperature = temperature;
        notifyObservers();
    }
}

// Observer
interface Observer {
    void update(Double temperature);
}

// Concrete Observer
class Display implements Observer {
    private String name;

    public Display(String name) {
        this.name = name;
    }

    public void update(Double temperature) {
        System.out.println(name + " received temperature update: " + temperature);
    }
}

// Usage example
public class Main {
    public static void main(String[] args) {
        WeatherStation weatherStation = new WeatherStation();

        Observer observer1 = new Display("Observer 1");
        Observer observer2 = new Display("Observer 2");

        weatherStation.registerObserver(observer1);
        weatherStation.registerObserver(observer2);

        weatherStation.setTemperature(25.5);
        weatherStation.setTemperature(30.0);

        weatherStation.removeObserver(observer1);

        weatherStation.setTemperature(27.8);
    }
}

```

---

<a id="file-design_patterns-08_observer-broadcast-js"></a>
### `design_patterns/08_Observer/broadcast.js`

- **Language:** JavaScript
- **Path:** `design_patterns/08_Observer/broadcast.js`
- **Lines:** 60
- [↑ Back to Top](#table-of-contents)

```javascript
// Subject (Observable)

// Libraries = Redux? Sveltestore? 
class WeatherStation {
    constructor() {
        this.temperature = null; // Variables (states) are dynamically taken care of, each state => observers
        this.observers = [];
    }

    registerObserver(observer) {
        this.observers.push(observer);
    }

    removeObserver(observer) {
        const index = this.observers.indexOf(observer);
        if (index !== -1) {
            this.observers.splice(index, 1);
        }
    }

    notifyObservers() {
        this.observers.forEach(observer => observer.update(this.temperature));
    }

    setTemperature(temperature) {
        console.log(`Setting temperature to: ${temperature}`);
        this.temperature = temperature;
        this.notifyObservers();
    }
}

// Observer
class Display {
    constructor(name) {
        this.name = name;
        // temperature
    }

    update(temperature) {
        console.log(`${this.name} received temperature update: ${temperature}`);
        // this.temperature = temperature
        // Whatever you want to trigger, when value change happens.
    }
}

// Usage example
const weatherStation = new WeatherStation();

const observer1 = new Display("Observer 1");
const observer2 = new Display("Observer 2");

weatherStation.registerObserver(observer1);
weatherStation.registerObserver(observer2);

weatherStation.setTemperature(25.5);
weatherStation.setTemperature(30.0);

weatherStation.removeObserver(observer1);

weatherStation.setTemperature(27.8);

```

---

<a id="file-design_patterns-08_observer-broadcast-py"></a>
### `design_patterns/08_Observer/broadcast.py`

- **Language:** Python
- **Path:** `design_patterns/08_Observer/broadcast.py`
- **Lines:** 67
- [↑ Back to Top](#table-of-contents)

```python
from abc import ABC, abstractmethod

# Abstract Subject
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._temperature = None
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print("Setting temperature to:", temperature)
        self._temperature = temperature
        self.notify_observers()

# Abstract Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Concrete Observer
class Display(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, temperature):
        print(f"{self._name} received temperature update: {temperature}")

# Usage example
if __name__ == "__main__":
    weather_station = WeatherStation()

    observer1 = Display("Observer 1")
    observer2 = Display("Observer 2")

    weather_station.register_observer(observer1)
    weather_station.register_observer(observer2)

    weather_station.set_temperature(25.5)
    weather_station.set_temperature(30.0)

    weather_station.remove_observer(observer1)

    weather_station.set_temperature(27.8)

```

---

<a id="file-design_patterns-09_mediator-main-java"></a>
### `design_patterns/09_Mediator/Main.java`

- **Language:** Java
- **Path:** `design_patterns/09_Mediator/Main.java`
- **Lines:** 154
- [↑ Back to Top](#table-of-contents)

```java
import java.util.ArrayList;
import java.util.List;

class TowerMediator {
    private List<Runway> runways;
    private List<Airplane> airplanes;

    public TowerMediator() {
        this.runways = new ArrayList<>();
        this.airplanes = new ArrayList<>();
    }

    public void addRunway(Runway runway) {
        runways.add(runway);
    }

    public void addAirplane(Airplane airplane) {
        airplanes.add(airplane);
    }

    public void requestToLand(Airplane airplane) {
        for (Runway runway : runways) {
            if (runway.isAvailable()) {
                runway.land(airplane);
                return;
            }
        }
        System.out.println("All runways are busy, " + airplane.getName() + " cannot land now.");
    }

    public void requestToTakeoff(Airplane airplane) {
        for (Runway runway : runways) {
            if (runway.isAvailable()) {
                runway.takeoff(airplane);
                return;
            }
        }
        System.out.println("All runways are busy, " + airplane.getName() + " cannot take off now.");
    }
}

class Runway {
    private String name;
    private boolean isAvailable;

    public Runway(String name) {
        this.name = name;
        this.isAvailable = true;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void land(Airplane airplane) {
        if (isAvailable) {
            System.out.println(airplane.getName() + " is landing on " + name + ".");
            isAvailable = false;
            airplane.land();
        } else {
            System.out.println(name + " is currently occupied.");
        }
    }

    public void takeoff(Airplane airplane) {
        if (isAvailable) {
            System.out.println(airplane.getName() + " is taking off from " + name + ".");
            isAvailable = false;
            airplane.takeoff();
        } else {
            System.out.println(name + " is currently occupied.");
        }
    }

    public void release() {
        isAvailable = true;
        System.out.println(name + " is now available.");
    }
}

class Airplane {
    private String name;
    private TowerMediator mediator;
    private boolean isFlying;

    public Airplane(String name, TowerMediator mediator) {
        this.name = name;
        this.mediator = mediator;
        this.isFlying = false;
    }

    public String getName() {
        return name;
    }

    public void requestLanding() {
        System.out.println(name + " is requesting to land.");
        mediator.requestToLand(this);
    }

    public void requestTakeoff() {
        System.out.println(name + " is requesting to take off.");
        mediator.requestToTakeoff(this);
    }

    public void land() {
        isFlying = false;
        System.out.println(name + " has landed.");
    }

    public void takeoff() {
        isFlying = true;
        System.out.println(name + " has taken off.");
    }
}

public class Main {
    public static void main(String[] args) {
        TowerMediator mediator = new TowerMediator();

        Runway runway1 = new Runway("Runway 1");
        Runway runway2 = new Runway("Runway 2");

        mediator.addRunway(runway1);
        mediator.addRunway(runway2);

        Airplane airplane1 = new Airplane("Airplane 1", mediator);
        Airplane airplane2 = new Airplane("Airplane 2", mediator);

        mediator.addAirplane(airplane1);
        mediator.addAirplane(airplane2);

        // Airplane 1 requests to land
        airplane1.requestLanding();

        // Airplane 2 requests to land
        airplane2.requestLanding();

        // Runway 1 is released and now available
        runway1.release();

        // Airplane 2 can now land
        airplane2.requestLanding();

        // Airplane 1 requests to take off
        airplane1.requestTakeoff();

        // Runway 1 is released and now available
        runway1.release();

        // Airplane 2 requests to take off
        airplane2.requestTakeoff();
    }
}

```

---

<a id="file-design_patterns-09_mediator-tower-js"></a>
### `design_patterns/09_Mediator/tower.js`

- **Language:** JavaScript
- **Path:** `design_patterns/09_Mediator/tower.js`
- **Lines:** 130
- [↑ Back to Top](#table-of-contents)

```javascript
class TowerMediator {
  constructor() {
    this.runways = [];
    this.airplanes = [];
  }

  addRunway(runway) {
    this.runways.push(runway);
  }

  addAirplane(airplane) {
    this.airplanes.push(airplane);
  }

  requestToLand(airplane) {
    for (let runway of this.runways) {
      if (runway.isAvailable) {
        runway.land(airplane);
        return;
      }
    }
    console.log(`All runways are busy, ${airplane.name} cannot land now.`);
  }

  requestToTakeoff(airplane) {
    for (let runway of this.runways) {
      if (runway.isAvailable) {
        runway.takeoff(airplane);
        return;
      }
    }
    console.log(`All runways are busy, ${airplane.name} cannot take off now.`);
  }
}

class Runway {
  constructor(name) {
    this.name = name;
    this.isAvailable = true;
  }

  land(airplane) {
    if (this.isAvailable) {
      console.log(`${airplane.name} is landing on ${this.name}.`);
      this.isAvailable = false;
      airplane.land();
    } else {
      console.log(`${this.name} is currently occupied.`);
    }
  }

  takeoff(airplane) {
    if (this.isAvailable) {
      console.log(`${airplane.name} is taking off from ${this.name}.`);
      this.isAvailable = false;
      airplane.takeoff();
    } else {
      console.log(`${this.name} is currently occupied.`);
    }
  }

  release() {
    this.isAvailable = true;
    console.log(`${this.name} is now available.`);
  }
}

class Airplane {
  constructor(name, mediator) {
    this.name = name;
    this.mediator = mediator;
    this.isFlying = false;
  }

  requestLanding() {
    console.log(`${this.name} is requesting to land.`);
    this.mediator.requestToLand(this);
  }

  requestTakeoff() {
    console.log(`${this.name} is requesting to take off.`);
    this.mediator.requestToTakeoff(this);
  }

  land() {
    this.isFlying = false;
    console.log(`${this.name} has landed.`);
  }

  takeoff() {
    this.isFlying = true;
    console.log(`${this.name} has taken off.`);
  }
}

// Example usage
const mediator = new TowerMediator();

const runway1 = new Runway('Runway 1');
const runway2 = new Runway('Runway 2');

mediator.addRunway(runway1);
mediator.addRunway(runway2);

const airplane1 = new Airplane('Airplane 1', mediator);
const airplane2 = new Airplane('Airplane 2', mediator);

mediator.addAirplane(airplane1);
mediator.addAirplane(airplane2);

// Airplane 1 requests to land
airplane1.requestLanding();

// Airplane 2 requests to land
airplane2.requestLanding();

// Runway 1 is released and now available
runway1.release();

// Airplane 2 can now land
airplane2.requestLanding();

// Airplane 1 requests to take off
airplane1.requestTakeoff();

// Runway 1 is released and now available
runway1.release();

// Airplane 2 requests to take off
airplane2.requestTakeoff();

```

---

<a id="file-design_patterns-09_mediator-tower-py"></a>
### `design_patterns/09_Mediator/tower.py`

- **Language:** Python
- **Path:** `design_patterns/09_Mediator/tower.py`
- **Lines:** 107
- [↑ Back to Top](#table-of-contents)

```python
class TowerMediator:
    def __init__(self):
        self.runways = []
        self.airplanes = []

    def add_runway(self, runway):
        self.runways.append(runway)

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)

    def request_to_land(self, airplane):
        for runway in self.runways:
            if runway.is_available:
                runway.land(airplane)
                return
        print(f"All runways are busy, {airplane.name} cannot land now.")

    def request_to_takeoff(self, airplane):
        for runway in self.runways:
            if runway.is_available:
                runway.takeoff(airplane)
                return
        print(f"All runways are busy, {airplane.name} cannot take off now.")

class Runway:
    def __init__(self, name):
        self.name = name
        self.is_available = True

    def land(self, airplane):
        if self.is_available:
            print(f"{airplane.name} is landing on {self.name}.")
            self.is_available = False
            airplane.land()
        else:
            print(f"{self.name} is currently occupied.")

    def takeoff(self, airplane):
        if self.is_available:
            print(f"{airplane.name} is taking off from {self.name}.")
            self.is_available = False
            airplane.takeoff()
        else:
            print(f"{self.name} is currently occupied.")

    def release(self):
        self.is_available = True
        print(f"{self.name} is now available.")

class Airplane:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.is_flying = False

    def request_landing(self):
        print(f"{self.name} is requesting to land.")
        self.mediator.request_to_land(self)

    def request_takeoff(self):
        print(f"{self.name} is requesting to take off.")
        self.mediator.request_to_takeoff(self)

    def land(self):
        self.is_flying = False
        print(f"{self.name} has landed.")

    def takeoff(self):
        self.is_flying = True
        print(f"{self.name} has taken off.")

# Example usage
mediator = TowerMediator()

runway1 = Runway("Runway 1")
runway2 = Runway("Runway 2")

mediator.add_runway(runway1)
mediator.add_runway(runway2)

airplane1 = Airplane("Airplane 1", mediator)
airplane2 = Airplane("Airplane 2", mediator)

mediator.add_airplane(airplane1)
mediator.add_airplane(airplane2)

# Airplane 1 requests to land
airplane1.request_landing()

# Airplane 2 requests to land
airplane2.request_landing()

# Runway 1 is released and now available
runway1.release()

# Airplane 2 can now land
airplane2.request_landing()

# Airplane 1 requests to take off
airplane1.request_takeoff()

# Runway 1 is released and now available
runway1.release()

# Airplane 2 requests to take off
airplane2.request_takeoff()

```

---

<a id="file-design_patterns-10_state-order-java"></a>
### `design_patterns/10_State/Order.java`

- **Language:** Java
- **Path:** `design_patterns/10_State/Order.java`
- **Lines:** 127
- [↑ Back to Top](#table-of-contents)

```java
// OrderState.java
public interface OrderState {
    void nextState(Order order);
    void prevState(Order order);
    String toString();
}

// NewOrderState.java
public class NewOrderState implements OrderState {
    @Override
    public void nextState(Order order) {
        order.setState(new ProcessingOrderState());
    }

    @Override
    public void prevState(Order order) {
        System.out.println("The order is already in the initial state.");
    }

    @Override
    public String toString() {
        return "New Order";
    }
}

// ProcessingOrderState.java
public class ProcessingOrderState implements OrderState {
    @Override
    public void nextState(Order order) {
        order.setState(new ShippedOrderState());
    }

    @Override
    public void prevState(Order order) {
        order.setState(new NewOrderState());
    }

    @Override
    public String toString() {
        return "Processing Order";
    }
}

// ShippedOrderState.java
public class ShippedOrderState implements OrderState {
    @Override
    public void nextState(Order order) {
        order.setState(new DeliveredOrderState());
    }

    @Override
    public void prevState(Order order) {
        order.setState(new ProcessingOrderState());
    }

    @Override
    public String toString() {
        return "Shipped Order";
    }
}

// DeliveredOrderState.java
public class DeliveredOrderState implements OrderState {
    @Override
    public void nextState(Order order) {
        System.out.println("The order is already in the final state.");
    }

    @Override
    public void prevState(Order order) {
        order.setState(new ShippedOrderState());
    }

    @Override
    public String toString() {
        return "Delivered Order";
    }
}

// Order.java
public class Order {
    private OrderState state;

    public Order() {
        state = new NewOrderState();
    }

    public void setState(OrderState state) {
        this.state = state;
    }

    public void nextState() {
        state.nextState(this);
    }

    public void prevState() {
        state.prevState(this);
    }

    @Override
    public String toString() {
        return "Order is currently in '" + state + "' state.";
    }

    public static void main(String[] args) {
        Order order = new Order();
        System.out.println(order);  // Output: Order is currently in 'New Order' state.

        order.nextState();
        System.out.println(order);  // Output: Order is currently in 'Processing Order' state.

        order.nextState();
        System.out.println(order);  // Output: Order is currently in 'Shipped Order' state.

        order.nextState();
        System.out.println(order);  // Output: Order is currently in 'Delivered Order' state.

        order.prevState();
        System.out.println(order);  // Output: Order is currently in 'Shipped Order' state.

        order.prevState();
        System.out.println(order);  // Output: Order is currently in 'Processing Order' state.

        order.prevState();
        System.out.println(order);  // Output: Order is currently in 'New Order' state.
    }
}

```

---

<a id="file-design_patterns-10_state-order-js"></a>
### `design_patterns/10_State/order.js`

- **Language:** JavaScript
- **Path:** `design_patterns/10_State/order.js`
- **Lines:** 109
- [↑ Back to Top](#table-of-contents)

```javascript
class OrderState {
    nextState(order) {
        throw new Error('nextState method should be implemented');
    }
    
    prevState(order) {
        throw new Error('prevState method should be implemented');
    }

    toString() {
        throw new Error('toString method should be implemented');
    }
}

class NewOrderState extends OrderState {
    nextState(order) {
        order.state = new ProcessingOrderState();
    }

    prevState(order) {
        console.log("The order is already in the initial state.");
    }

    toString() {
        return 'New Order';
    }
}

class ProcessingOrderState extends OrderState {
    nextState(order) {
        order.state = new ShippedOrderState();
    }

    prevState(order) {
        order.state = new NewOrderState();
    }

    toString() {
        return 'Processing Order';
    }
}

class ShippedOrderState extends OrderState {
    nextState(order) {
        order.state = new DeliveredOrderState();
    }

    prevState(order) {
        order.state = new ProcessingOrderState();
    }

    toString() {
        return 'Shipped Order';
    }
}

class DeliveredOrderState extends OrderState {
    nextState(order) {
        console.log("The order is already in the final state.");
    }

    prevState(order) {
        order.state = new ShippedOrderState();
    }

    toString() {
        return 'Delivered Order';
    }
}

class Order {
    constructor() {
        this.state = new NewOrderState();
    }
    
    nextState() {
        this.state.nextState(this);
    }
    
    prevState() {
        this.state.prevState(this);
    }
    
    toString() {
        return `Order is currently in '${this.state.toString()}' state.`;
    }
}

// Example Usage
const order = new Order();
console.log(order.toString());  // Output: Order is currently in 'New Order' state.

order.nextState();
console.log(order.toString());  // Output: Order is currently in 'Processing Order' state.

order.nextState();
console.log(order.toString());  // Output: Order is currently in 'Shipped Order' state.

order.nextState();
console.log(order.toString());  // Output: Order is currently in 'Delivered Order' state.

order.prevState();
console.log(order.toString());  // Output: Order is currently in 'Shipped Order' state.

order.prevState();
console.log(order.toString());  // Output: Order is currently in 'Processing Order' state.

order.prevState();
console.log(order.toString());  // Output: Order is currently in 'New Order' state.

```

---

<a id="file-design_patterns-10_state-order-py"></a>
### `design_patterns/10_State/order.py`

- **Language:** Python
- **Path:** `design_patterns/10_State/order.py`
- **Lines:** 89
- [↑ Back to Top](#table-of-contents)

```python
from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def next_state(self, order):
        pass
    
    @abstractmethod
    def prev_state(self, order):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

class NewOrderState(OrderState):
    def next_state(self, order):
        order.state = ProcessingOrderState()

    def prev_state(self, order):
        print("The order is already in the initial state.")

    def __str__(self):
        return "New Order"

class ProcessingOrderState(OrderState):
    def next_state(self, order):
        order.state = ShippedOrderState()

    def prev_state(self, order):
        order.state = NewOrderState()

    def __str__(self):
        return "Processing Order"

class ShippedOrderState(OrderState):
    def next_state(self, order):
        order.state = DeliveredOrderState()

    def prev_state(self, order):
        order.state = ProcessingOrderState()

    def __str__(self):
        return "Shipped Order"

class DeliveredOrderState(OrderState):
    def next_state(self, order):
        print("The order is already in the final state.")

    def prev_state(self, order):
        order.state = ShippedOrderState()

    def __str__(self):
        return "Delivered Order"

class Order:
    def __init__(self):
        self.state = NewOrderState()
        
    def next_state(self):
        self.state.next_state(self)
        
    def prev_state(self):
        self.state.prev_state(self)
        
    def __str__(self):
        return f"Order is currently in '{self.state}' state."


order = Order()
print(order)  # Output: Order is currently in 'New Order' state.

order.next_state()
print(order)  # Output: Order is currently in 'Processing Order' state.

order.next_state()
print(order)  # Output: Order is currently in 'Shipped Order' state.

order.next_state()
print(order)  # Output: Order is currently in 'Delivered Order' state.

order.prev_state()
print(order)  # Output: Order is currently in 'Shipped Order' state.

order.prev_state()
print(order)  # Output: Order is currently in 'Processing Order' state.

order.prev_state()
print(order)  # Output: Order is currently in 'New Order' state.
```

---

<a id="dir-dynamic-programming"></a>
## Directory: `dynamic-programming/`

<a id="file-dynamic-programming-01_fibonacci-fib-cpp"></a>
### `dynamic-programming/01_Fibonacci/fib.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/01_Fibonacci/fib.cpp`
- **Lines:** 36
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

#define llint long long int

// O(1.618...^n) time complexity code
llint fib(int n) {
    // Base Case
    if (n == 0 || n == 1)
        return 1;
    
    // Decomposition Step
    llint a = fib(n-1);
    llint b = fib(n-2);

    // Recomposition Step
    return a + b;
}

// Driver Code
int main() {
    int n; 
    cin >> n;

    cout << fib(n) << endl;

    return 0;
}

/*

Try to put n = 45 as input and you will see a considerable time delay the code takes to compute the answer! 

Lets improve that time in fib_memo.cpp. 

*/
```

---

<a id="file-dynamic-programming-01_fibonacci-fib_memo-cpp"></a>
### `dynamic-programming/01_Fibonacci/fib_memo.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/01_Fibonacci/fib_memo.cpp`
- **Lines:** 51
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

#define llint long long int

// Memo table
llint memo[101];

// O(n) time complexity code
llint fib(int n) {
    // Base Case
    if (n == 0 || n == 1)
        return 1;
    
    // STEP 2: Before recursion, check if you know the answer
    if (memo[n] != -1)
        return memo[n];

    // Decomposition Step
    llint a = fib(n-1);
    llint b = fib(n-2);

    // Recomposition Step
    // STEP 3: Before returning the answer, store it for future
    memo[n] = a + b;
    return memo[n];
}

// Driver Code
int main() {
    int n; 
    cin >> n;

    // STEP 1: Initialize the memo table with -1
    for (int i = 0; i <= n; i++)
        memo[i] = -1;

    cout << fib(n) << endl;

    return 0;
}

/*

It is not a good practice to keep the memo table global. However, it is a decent appraoch for problem solving as you dont need to worry on passing it in your recursion and keeping its track. 

The size of the global memo table I pick it from the 'constraints' section of the problem. If 0 <= n <= 100, I create the memo table of 101 i.e. (max value of n) + 1.

Now try putting n = 45 again as input and see the time difference in which you see the answer!

*/
```

---

<a id="file-dynamic-programming-02_knapsack-lc_322-cpp"></a>
### `dynamic-programming/02_Knapsack/LC_322.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/LC_322.cpp`
- **Lines:** 42
- [↑ Back to Top](#table-of-contents)

```cpp
class Solution {
public:
    int memo[13][10001];

    int knapsack(vector<int> &coins, int n, int amount) {
        if (amount == 0)
            return 0;
        
        if (n == coins.size()) 
            return INT_MAX-1;

        if (memo[n][amount] != -1)
            return memo[n][amount];

        // You can always skip
        int skip_coin = knapsack(coins, n+1, amount);

        // You can only pick if amount > coins[n]
        int take_coin = INT_MAX-1;
        if (amount >= coins[n]) {
            take_coin = 1 + knapsack(coins, n, amount - coins[n]);
        }

        memo[n][amount] = min(skip_coin, take_coin);
        return memo[n][amount];
    }

    int coinChange(vector<int>& coins, int amount) {
        
        for (int i = 0; i <= coins.size(); i++)
            for (int j = 0; j <= amount; j++)
                memo[i][j] = -1;

        int ans = knapsack(coins, 0, amount);

        if (ans == INT_MAX-1)
            return -1;
        
        return ans;
        
    }
};
```

---

<a id="file-dynamic-programming-02_knapsack-lc_416-cpp"></a>
### `dynamic-programming/02_Knapsack/LC_416.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/LC_416.cpp`
- **Lines:** 40
- [↑ Back to Top](#table-of-contents)

```cpp
class Solution {
public:
    int memo[201][20001];

    bool subset_sum(vector<int> &nums, int n, int sum) {
        if (n == -1)     // no more items left
            return 0;

        if (sum == 0)    // leftover sum is found.
            return 1;

        // Recall step
        if (memo[n][sum] != -1)
            return memo[n][sum];

        if (nums[n] > sum) {
            memo[n][sum] = subset_sum(nums, n-1, sum);
        } else {
            memo[n][sum] = subset_sum(nums, n-1, sum) || subset_sum(nums, n-1, sum-nums[n]);
        }

        return memo[n][sum];
    }

    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (auto x: nums) 
            sum += x;

        // Initialize it to -1
        for (int i = 0; i <= nums.size(); i++)
            for (int j = 0; j <= sum; j++)
                memo[i][j] = -1;

        if (sum%2 != 0)
            return false;
        else
            return subset_sum(nums, nums.size() - 1, sum/2);
    }
};
```

---

<a id="file-dynamic-programming-02_knapsack-lc_494-cpp"></a>
### `dynamic-programming/02_Knapsack/LC_494.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/LC_494.cpp`
- **Lines:** 19
- [↑ Back to Top](#table-of-contents)

```cpp
class Solution {
public:
    int knapsack(vector<int> &arr, int n, int target) {
        if (n == arr.size()) {
            if (target == 0)
                return 1;
            return 0;
        }

        int pick = knapsack(arr, n+1, target + arr[n]);
        int skip = knapsack(arr, n+1, target - arr[n]);

        return pick + skip;
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        return knapsack(nums, 0, target);
    }
};
```

---

<a id="file-dynamic-programming-02_knapsack-lc_518-cpp"></a>
### `dynamic-programming/02_Knapsack/LC_518.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/LC_518.cpp`
- **Lines:** 32
- [↑ Back to Top](#table-of-contents)

```cpp
class Solution {
public:
    int knapsack(const vector<int>& coins, int amount, int index, vector<vector<int>>& memo) {
        // Base cases
        if (amount == 0) {
            return 1;
        }
        if (amount < 0 || index < 0) {
            return 0;
        }
        
        // Check memoization table
        if (memo[index][amount] != -1) {
            return memo[index][amount];
        }
        
        // Calculate the number of ways by including the current coin and excluding it
        int include = knapsack(coins, amount - coins[index], index, memo);
        int exclude = knapsack(coins, amount, index - 1, memo);
        
        // Store the result in the memoization table
        memo[index][amount] = include + exclude;
        
        return memo[index][amount];
    }

    int change(int amount, vector<int>& coins) {
        // Initialize the memoization table with -1
        vector<vector<int>> memo(coins.size(), vector<int>(amount + 1, -1));
        return knapsack(coins, amount, coins.size() - 1, memo);
    }
};

```

---

<a id="file-dynamic-programming-02_knapsack-knapsack-cpp"></a>
### `dynamic-programming/02_Knapsack/knapsack.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/knapsack.cpp`
- **Lines:** 56
- [↑ Back to Top](#table-of-contents)

```cpp
#include <bits/stdc++.h>
using namespace std;

int memo[1001][1001];  // max(n) = 1000, max(C) = 1000.

int knapsack(int n, int C, vector<int> price, vector<int> weight) {
    if (n == -1 || C <= 0)
        return 0;

    if (memo[n][C] != -1)
        return memo[n][C];

    int ans = INT_MIN;
    // Only choice to skip
    if (weight[n] > C)
        ans = knapsack(n-1, C, price, weight);
    else // Else, max of skip and pick
        ans = max(knapsack(n-1, C, price, weight), price[n] + knapsack(n-1, C-weight[n], price, weight)); 
    
    memo[n][C] = ans;
    return memo[n][C];
}

int main() {

    int n, C; cin >> n >> C;

    vector<int> price, weight; 

    int temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        price.push_back(temp);
    }

    for (int i = 0; i < n; i++) {
        cin >> temp;
        weight.push_back(temp);
    }

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= C; j++) {
            memo[i][j] = -1;
        }
    }

    cout << knapsack(n-1, C, price, weight) << endl;

    return 0;
}

/*

In the tabulation method, bottom up, we can space-optimize to 1D memo table and not 2D. 

*/
```

---

<a id="file-dynamic-programming-02_knapsack-knapsack_space_optimize-cpp"></a>
### `dynamic-programming/02_Knapsack/knapsack_space_optimize.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/knapsack_space_optimize.cpp`
- **Lines:** 48
- [↑ Back to Top](#table-of-contents)

```cpp
#include <bits/stdc++.h>
using namespace std;

int memo[1001];  // max(C) = 1000.

int knapsack(int n, int C, vector<int> price, vector<int> weight) {

    memo[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int w = C; w >= 0; w--) {
            if (weight[i-1] <= w)
                memo[w] = max(memo[w], memo[w-weight[i-1]] + price[i-1]);
        }
    }
    
    return memo[C];
}

int main() {

    int n, C; cin >> n >> C;

    vector<int> price, weight; 

    int temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        price.push_back(temp);
    }

    for (int i = 0; i < n; i++) {
        cin >> temp;
        weight.push_back(temp);
    }

    // NO NEED TO INITIALIZE -1 IN CASE OF TABULATION

    // for (int i = 0; i <= n; i++) {
    //     for (int j = 0; j <= C; j++) {
    //         memo[i][j] = -1;
    //     }
    // }

    // Notice that we are passing here n and not n-1.
    cout << knapsack(n, C, price, weight) << endl;

    return 0;
}

```

---

<a id="file-dynamic-programming-02_knapsack-subset_sum-cpp"></a>
### `dynamic-programming/02_Knapsack/subset_sum.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/02_Knapsack/subset_sum.cpp`
- **Lines:** 69
- [↑ Back to Top](#table-of-contents)

```cpp
/* PROBLEM STATEMENT: Subset Sum Problem

Given a set of non-negative integers and a value sum, the task is to check if there is a subset of the given set whose sum is equal to the given sum. 

For example, given set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output is True. Because there is a subset (4, 5) with sum 9.

*/

#include <bits/stdc++.h>
using namespace std;

int memo[1001][100001]; // max(n) = 1000, sum = 100000

bool subset_sum(int n, int sum, vector<int> arr) {
    // No more elements left
    if (n == -1)
        return 0;

    // Leftover sum is zero, answer found.
    if (sum == 0)
        return 1;

    if (memo[n][sum] != -1)
        return memo[n][sum];

    int ans = INT_MIN;
    // Only choice to skip
    if (arr[n] > sum)
        ans = subset_sum(n-1, sum, arr);
    else // Else, max of skip and pick
        ans = subset_sum(n-1, sum, arr) || subset_sum(n-1, sum-arr[n], arr); 
    
    memo[n][sum] = ans;
    return memo[n][sum];
}

int main() {
    int n, sum; cin >> n >> sum;

    vector<int> arr; 

    int temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        arr.push_back(temp);
    } 

    // Set the memo to -1
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= sum; j++) 
            memo[i][j] = -1;

    cout << subset_sum(n-1, sum, arr) << endl;

    return 0;
}

/*

Note: Here, we are asked if it is possible to form a subset or not. Hence, we are able to reduce the time complexity from O(2^n) to O(n*sum). If they were to actually ask you to print the subsets, in that case there is no other option but to generate all possible subsets and check for the sum and return that particular subset. This will result in O(2^n) time complexity. 

Making subsets will fall in the realm of backtracking!!

There is a variation called `Equal sum partition`. https://leetcode.com/problems/partition-equal-subset-sum/description/

This

*/
```

---

<a id="file-dynamic-programming-03_lcs-scs_1-cpp"></a>
### `dynamic-programming/03_LCS/scs_1.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/03_LCS/scs_1.cpp`
- **Lines:** 91
- [↑ Back to Top](#table-of-contents)

```cpp
class Solution {
public:
    string LCS(string &s1, string &s2) {
        // Tabulate the memo table
        int m = s1.size(); 
        int n = s2.size();

        // Smart move: Because initializing with 0, base case already covered!
        vector<vector<int>> memo(m+1, vector<int>(n+1, 0));

        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (s1[i-1] == s2[j-1]) {
                    memo[i][j] = 1 + memo[i-1][j-1];
                } else {
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1]);
                }
            }

        // I will memo table here. Here I will construct the LCS from 
        // the memo table and will return the ans from here. 

        string lcs = "";
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (s1[i-1] == s2[j-1]) {
                lcs += s1[i-1];
                i--; j--;
            } else if (memo[i-1][j] > memo[i][j-1]) 
                i--;
            else 
                j--;
        }

        reverse(lcs.begin(), lcs.end());
        return lcs;
    }

    string shortestCommonSupersequence(string str1, string str2) {
        string lcs = LCS(str1, str2);
        // cout << lcs << endl;

        // Construct the SCS using 3 pointer
        string ans = "";
        int i = 0, j = 0;

        // for each character in LCS
        for (char x: lcs) {
            // Add the extra elements in the ans before we hit x.
            while (str1[i] != x) {
                ans += str1[i];
                i++;
            }

            while (str2[j] != x) {
                ans += str2[j];
                j++;
            }

            // add the LCS character
            ans += x;
            i++; j++;
        }

        // After the final LCS character, add the leftovers.
        return ans + str1.substr(i) + str2.substr(j);
    }
};

/* Part by Part.

1. I need LCS => The actual string and not the length. 

If I go with recursion + memo -> this will fill memo table for me. 

2. I have 3 strings: s1, s2, lcs(s1, s2). 

I need to compose the resultant scs -> As long as characters in s1 and s2
are not in lcs, you append in the ans and then you take the char from LCS
and you keep the repeating the process. 


Eg. abac cab
LCS(~ab~ac, ~cab~) => ~ab~

Look the first character of lcs is a. Is there anything before a in s1 or s2?
c (not in LCS, s2) + a (LCS, skip s1 and s2) + b (LCS, skip s1 and s2) + is there any leftover? ac (s1) = cabac.

3 pointer: x (lcs), i(s1), j(s2).

*/
```

---

<a id="file-dynamic-programming-03_lcs-scs_2-cpp"></a>
### `dynamic-programming/03_LCS/scs_2.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/03_LCS/scs_2.cpp`
- **Lines:** 98
- [↑ Back to Top](#table-of-contents)

```cpp
#include<stdio.h>
#include<string.h>

class Solution {
public:
    string LCS(string &s1, string &s2) {
        int m = s1.size();
        int n = s2.size();

        vector<vector<int>> memo(m+1, vector<int>(n+1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i-1] == s2[j-1]) {
                    memo[i][j] = memo[i-1][j-1] + 1;
                } else {
                    if (memo[i-1][j] > memo[i][j-1]) 
                        memo[i][j] = memo[i-1][j];
                    else
                        memo[i][j] = memo[i][j-1];
                }
            }
        }

       // Reconstruct the LCS by traversing the memo table
       string lcs = "";
       int i = m, j = n;
       while (i > 0 && j > 0) {
            if (s1[i-1] == s2[j-1]) {
                lcs += s1[i-1];
                i--; j--;
            } else if (memo[i-1][j] > memo[i][j-1]) {
                i--;
            } else 
                j--;
       }

       reverse(lcs.begin(), lcs.end());

       return lcs;
    }

    string shortestCommonSupersequence(string str1, string str2) {
        string lcs = LCS(str1, str2);
        cout << lcs << endl;

        // I am going to use i for str1, j for str2. As long as they 
        // don't match the character of LCS, extract them, and put it
        // in the ans.

        string ans = ""; int i = 0, j = 0;
        for (auto x: lcs) {
            
            // This will add extra elements from s1 and s2 which are not in LCS
            while (str1[i] != x) {
                ans += str1[i];
                i++;
            }
            while (str2[j] != x) {
                ans += str2[j];
                j++;
            }

            ans += x;
            i++; j++;  // Increment both because lcs char is in both   
        }

        // cout << i << " " << j << endl;
        // My i and j are not m and n at the end of the loop. 
        // This means, that I need to append, the last remainings of 
        // the strings

        // cout << str1_remains << " " << str2_remains << endl;

        return ans + str1.substr(i) + str2.substr(j);
    }
};

/* Thoughts:

1. I need LCS (abac, cab) => (ab) | 4 + 3 - 2 = 5

Interesting: I dont need length of LCS, but LCS itself. 

I can calculate memo table, and then traverse it to get LCS. 
(m, n) => (0, 0), whenever there is a diagonal jump, you take the char
and that gives you LCS. 

OR (shortcut)

Let the memo table contain strings. Instead of memo table being of integers, why cant i define vector<vector<string>> memo. And I will fill this memo table without recursion. 

Why am I filling? Because first you let it fell, then anyways, you are traversing it. Lets traverse it and fill it on the go. 

2. I need to extract the elements from s1 and s2, which are not in LCS, 
and put them in right position.

*/
```

---

<a id="file-dynamic-programming-problem_set_easy-01_min_steps_to_one-cpp"></a>
### `dynamic-programming/Problem_Set_Easy/01_min_steps_to_one.cpp`

- **Language:** C++
- **Path:** `dynamic-programming/Problem_Set_Easy/01_min_steps_to_one.cpp`
- **Lines:** 70
- [↑ Back to Top](#table-of-contents)

```cpp
/*   PROBLEM STATEMENT: Minimum Steps to One

You are given a number 'n'. On this n, you can perform 3 operations.

a) If n is divisble by 3, you can divide it by 3.
b) If n is divisible by 2, you can divide it by 2. 
c) Otherwise, you can reduce the number by 1. 

What are the minimum number of operations required for n, so that it gets reduced to 1?

Example: I have number 5. It can be reduced to 1 in 3 steps. 
5 -> (reduce by 1) 4 -> (divide by 2) 2 -> (divide by 2) 1! OR
5 -> (reduce by 1) 4 -> (reduce by 1) 3 -> (divide by 3) 1!

How to solve it?

SOLUTION: 

It may look like it's a greedy question, but it is not. Consider this case when n = 10. 

You cannot divide this by 1. So greedily it is better to divide it by 2 and make it 5, than reduce it by 1 and make it 9. But,

10 -> 5 -> 4 -> 2 -> 1 (4 steps). 
10 -> 9 -> 3 -> 1 (3 steps).

min_steps_to_one(n) = 1 + min(a, b, c) 

where a = min_steps_to_one(n/3) if n is divisible by 3
      b = min_steps_to_one(n/2) if n is divisible by 2
      c = min_steps_to_one(n-1) 

*/

#include <bits/stdc++.h>
using namespace std;

int memo[100001];

int min_steps_to_one(int n) {
    if (n == 1)
        return 0;

    if (memo[n] != -1)
        return memo[n];

    int a = INT_MAX, b = INT_MAX, c = INT_MAX;

    if (n%3 == 0)
        a = min_steps_to_one(n/3) + 1;
    
    if (n%2 == 0)
        b = min_steps_to_one(n/2) + 1;
    
    c = min_steps_to_one(n-1) + 1;

    memo[n] = min(a, min(b, c));
    return memo[n];
}

int main() {
    int n; 
    cin >> n;

    for (int i = 0; i <= n; i++)
        memo[i] = -1;

    cout << min_steps_to_one(n) << endl;
    return 0;
}


```

---

<a id="dir-graphs"></a>
## Directory: `graphs/`

<a id="file-graphs-bfs-cpp"></a>
### `graphs/bfs.cpp`

- **Language:** C++
- **Path:** `graphs/bfs.cpp`
- **Lines:** 133
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

// 'u' is a node 'from', 'v' is a node 'to': from u to v
void add_edge_list(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    g[v].push_back(u);      // Delete this line if graph is directed
}

void add_edge_matrix(vector<vector<int>> &g, int u, int v) {
    g[u][v] = 1;
    g[v][u] = 1;            // Delete this line for directed graph
}

// Two functions to perform the BFS

// LIST
void bfs_list(vector<vector<int>> &g, int start) {
    cout << "BFS LIST:\n";

    int n = g.size();
    bool* visited = new bool[n]();
    int* level = new int[n]();
    int* parent = new int[n]();
    queue<int> q;
    int i = 1;
    
    // process the start node
    q.push(start);
    visited[start] = true;
    level[start] = i-1;
    parent[start] = -1;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << " ";      // Printing: Anything with the node, should be done here.
        for (auto v: g[u]) {
            // Anything with the edge, should be done here.
            if (!visited[v]) {
                q.push(v);
                visited[v] = true;
                level[v] = i;
                parent[v] = u;
            }
        }
        i++;
    }

    cout << endl << endl;

    for (int i = 0; i < n; i++)
        cout << i << " ";
    cout << endl;

    for (int i = 0; i < n; i++) {
        cout << level[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < n; i++) {
        cout << parent[i] << " ";
    }
    cout << endl;

    // Shortest path logic
    int dest = 2; vector<int> path;
    while (dest != -1) {
        path.push_back(dest);
        dest = parent[dest];
    }
    reverse(path.begin(), path.end());

    for (auto x: path)
        cout << x << " ";
    cout << endl;
}

// MATRIX
void bfs_matrix(vector<vector<int>> &g, int start) {
    cout << "BFS MATRIX:\n";

    int n = g.size();
    bool* visited = new bool[n]();
    int* level = new int[n]();
    int* parent = new int[n]();
    queue<int> q;
    int i = 1;
    
    // process the start node
    q.push(start);
    visited[start] = true;
    level[start] = i-1;
    parent[start] = -1;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << " ";
        for (int v = 0; v < n; v++) {
            if (g[u][v] == 1 && !visited[v]) {
                q.push(v);
                visited[v] = true;
                level[v] = i;
                parent[v] = u;
            }
        }
        i++;
    }

    cout << endl;
}

int main() {
    int n, e; cin >> n >> e;

    // Adjacency list
    vector<vector<int>> adj_list(n, vector<int>());

    // Adjacency matrix
    vector<vector<int>> adj_matrix(n, vector<int>(n, 0));   // nxn matrix all zeros

    // Our nodes are from 0 to n-1
    while (e--) {
        int u, v; cin >> u >> v;
        add_edge_list(adj_list, u, v);
        add_edge_matrix(adj_matrix, u, v);
    }

    // Note: If you have a disconnected graph, go for DFS. Try to avoid BFS.
    bfs_list(adj_list, 0);
    bfs_matrix(adj_matrix, 0);

    return 0;
}
```

---

<a id="file-graphs-bfs-py"></a>
### `graphs/bfs.py`

- **Language:** Python
- **Path:** `graphs/bfs.py`
- **Lines:** 115
- [↑ Back to Top](#table-of-contents)

```python
from collections import deque

def add_edge_list(g, u, v):
    g[u].append(v)
    g[v].append(u)  # Delete this line if the graph is directed

def add_edge_matrix(g, u, v):
    g[u][v] = 1
    g[v][u] = 1  # Delete this line for directed graph

# Two functions to perform the BFS

# LIST
def bfs_list(g, start):
    print("BFS LIST:")

    n = len(g)
    visited = [False] * n
    level = [0] * n
    parent = [-1] * n
    q = deque()
    i = 1
    
    # process the start node
    q.append(start)
    visited[start] = True
    level[start] = i - 1

    while q:
        u = q.popleft()
        print(u, end=" ")  # Printing: Anything with the node, should be done here.
        for v in g[u]:
            # Anything with the edge, should be done here.
            if not visited[v]:
                q.append(v)
                visited[v] = True
                level[v] = i
                parent[v] = u
        i += 1

    print("\n")

    for i in range(n):
        print(i, end=" ")
    print()

    for i in range(n):
        print(level[i], end=" ")
    print()

    for i in range(n):
        print(parent[i], end=" ")
    print()

    dest = 2
    path = []
    while dest != -1:
        path.append(dest)
        dest = parent[dest]
    path.reverse()

    for x in path:
        print(x, end=" ")
    print()

# MATRIX
def bfs_matrix(g, start):
    print("BFS MATRIX:")

    n = len(g)
    visited = [False] * n
    level = [0] * n
    parent = [-1] * n
    q = deque()
    i = 1
    
    # process the start node
    q.append(start)
    visited[start] = True
    level[start] = i - 1

    while q:
        u = q.popleft()
        print(u, end=" ")
        for v in range(n):
            if g[u][v] == 1 and not visited[v]:
                q.append(v)
                visited[v] = True
                level[v] = i
                parent[v] = u
        i += 1

    print()

def main():
    n, e = map(int, input().split())

    # Adjacency list
    adj_list = [[] for _ in range(n)]

    # Adjacency matrix
    adj_matrix = [[0] * n for _ in range(n)]  # nxn matrix all zeros

    # Our nodes are from 0 to n-1
    for _ in range(e):
        u, v = map(int, input().split())
        add_edge_list(adj_list, u, v)
        add_edge_matrix(adj_matrix, u, v)

    # Note: If you have a disconnected graph, go for DFS. Try to avoid BFS.
    bfs_list(adj_list, 0)
    bfs_matrix(adj_matrix, 0)

if __name__ == "__main__":
    main()

```

---

<a id="file-graphs-create_graph-cpp"></a>
### `graphs/create_graph.cpp`

- **Language:** C++
- **Path:** `graphs/create_graph.cpp`
- **Lines:** 67
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

// 'u' is a node 'from', 'v' is a node 'to': from u to v
void add_edge_list(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    g[v].push_back(u);      // Delete this line if graph is directed
}

void add_edge_matrix(vector<vector<int>> &g, int u, int v) {
    g[u][v] = 1;
    g[v][u] = 1;            // Delete this line for directed graph
}

// Two helper functions to print the graphs
void print_graph_list(vector<vector<int>> g) {
    cout << "ADJ LIST:\n";
    for (int i = 0; i < g.size(); i++) {
        cout << i << ": ";
        for (auto v: g[i]) {
            cout << v << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void print_graph_matrix(vector<vector<int>> g) {
    cout << "ADJ MATRIX:\n";
    cout << "  ";
    for (int i = 0; i < g.size(); i++) {
        cout << " " << i;
    }
    cout << endl;

    for (int i = 0; i < g.size(); i++) {
        cout << i << ": ";
        for (int j = 0; j < g[i].size(); j++) {
            cout << g[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

int main() {

    int n, e; cin >> n >> e;

    // Adjacency list
    vector<vector<int>> adj_list(n, vector<int>());

    // Adjacency matrix
    vector<vector<int>> adj_matrix(n, vector<int>(n, 0));   // nxn matrix all zeros

    // Our nodes are from 0 to n-1
    while (e--) {
        int u, v; cin >> u >> v;
        add_edge_list(adj_list, u, v);
        add_edge_matrix(adj_matrix, u, v);
    }

    print_graph_list(adj_list);
    print_graph_matrix(adj_matrix);

    return 0;
}
```

---

<a id="file-graphs-cycles-cpp"></a>
### `graphs/cycles.cpp`

- **Language:** C++
- **Path:** `graphs/cycles.cpp`
- **Lines:** 93
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

// 'u' is a node 'from', 'v' is a node 'to': from u to v
void add_edge_list(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    // g[v].push_back(u);      // Delete this line if graph is directed
}

void add_edge_list_undirected(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    g[v].push_back(u);      // Delete this line if graph is directed
}

// Check if the undirected graph has a cycle. DFS
bool has_cycle_visit(vector<vector<int>> &g, int u, bool* visited, int parent) {
    visited[u] = true;
    for (auto v: g[u]) {
        if (!visited[v]) 
            return has_cycle_visit(g, v, visited, u);
        else if (v != parent)
            return true;
    }
    return false;
}

bool has_cycle(vector<vector<int>> &g) {
    int n = g.size();
    bool* visited = new bool[n]();
    for (int i = 0; i < n; i++) {
        if (!visited[i]) 
            return has_cycle_visit(g, i, visited, -1);
    }
    return false;
}

// Check if the directed graph has a cycle. DFS
bool has_cycle_visit_directed(vector<vector<int>> g, int u, bool* visited, bool* recursion_stack) {
    if (!visited[u]) {
        visited[u] = true;
        recursion_stack[u] = true;

        for (auto v: g[u]) {
            if (!visited[v] && has_cycle_visit_directed(g, v, visited, recursion_stack))
                return true;
            else if (recursion_stack[v])
                return true;
        }

        recursion_stack[u] = false;
        return false;
    }
}

bool has_cycle_directed(vector<vector<int>> &g) {
    int n = g.size();

    bool* visited = new bool[n]();
    bool* recursion_stack = new bool[n]();

    for (int i = 0; i < n; i++) {
        return has_cycle_visit_directed(g, i, visited, recursion_stack);
    }

    return false;
}

int main() {
    int n, e; cin >> n >> e;

    // Adjacency list
    vector<vector<int>> adj_list(n, vector<int>());
    vector<vector<int>> adj_list2(n, vector<int>());

    // Our nodes are from 0 to n-1
    while (e--) {
        int u, v; cin >> u >> v;
        add_edge_list(adj_list, u, v);
        add_edge_list_undirected(adj_list2, u, v);
    }

    if (has_cycle_directed(adj_list))
        cout << "Has cycle.\n"; 
    else 
        cout << "Doesn't have cycle.\n";

    if (has_cycle(adj_list2)) 
        cout << "Has cycle.\n";
    else   
        cout << "Doesn't have cycle.\n";

    return 0;
}
```

---

<a id="file-graphs-cycles-py"></a>
### `graphs/cycles.py`

- **Language:** Python
- **Path:** `graphs/cycles.py`
- **Lines:** 96
- [↑ Back to Top](#table-of-contents)

```python
def add_edge(graph, u, v):
    """
    Add an edge from node u to node v in the graph.
    """
    graph[u].append(v)


def add_edge_undirected(graph, u, v):
    """
    Add an undirected edge between node u and node v in the graph.
    """
    graph[u].append(v)
    graph[v].append(u)


def has_cycle_visit(graph, u, visited, parent):
    """
    Helper function to check if there is a cycle in an undirected graph using DFS.
    """
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            if has_cycle_visit(graph, v, visited, u):
                return True
        elif v != parent:
            return True
    return False


def has_cycle(graph):
    """
    Check if the undirected graph has a cycle using DFS.
    """
    n = len(graph)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if has_cycle_visit(graph, i, visited, -1):
                return True
    return False


def has_cycle_visit_directed(graph, u, visited, recursion_stack):
    """
    Helper function to check if there is a cycle in a directed graph using DFS.
    """
    visited[u] = True
    recursion_stack[u] = True
    for v in graph[u]:
        if not visited[v]:
            if has_cycle_visit_directed(graph, v, visited, recursion_stack):
                return True
        elif recursion_stack[v]:
            return True
    recursion_stack[u] = False
    return False


def has_cycle_directed(graph):
    """
    Check if the directed graph has a cycle using DFS.
    """
    n = len(graph)
    visited = [False] * n
    recursion_stack = [False] * n
    for i in range(n):
        if not visited[i]:
            if has_cycle_visit_directed(graph, i, visited, recursion_stack):
                return True
    return False


if __name__ == "__main__":
    # Input number of nodes and edges
    n, e = map(int, input().split())

    # Adjacency list for the directed and undirected graphs
    adj_list = [[] for _ in range(n)]
    adj_list_undirected = [[] for _ in range(n)]

    # Adding edges to the graphs
    for _ in range(e):
        u, v = map(int, input().split())
        add_edge(adj_list, u, v)
        add_edge_undirected(adj_list_undirected, u, v)

    # Checking for cycles in directed and undirected graphs
    if has_cycle_directed(adj_list):
        print("Has cycle in directed graph.")
    else:
        print("Doesn't have cycle in directed graph.")

    if has_cycle(adj_list_undirected):
        print("Has cycle in undirected graph.")
    else:
        print("Doesn't have cycle in undirected graph.")

```

---

<a id="file-graphs-dfs-cpp"></a>
### `graphs/dfs.cpp`

- **Language:** C++
- **Path:** `graphs/dfs.cpp`
- **Lines:** 134
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

// 'u' is a node 'from', 'v' is a node 'to': from u to v
void add_edge_list(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    // g[v].push_back(u);      // Delete this line if graph is directed
}

void add_edge_matrix(vector<vector<int>> &g, int u, int v) {
    g[u][v] = 1;
    // g[v][u] = 1;            // Delete this line for directed graph
}

// Two functions to perform the DFS

// LIST
void dfs_list_visit(vector<vector<int>> &g, int start, bool* visited){
    stack <int> s;
    
    s.push(start);
    visited[start] = true;

    while (!s.empty()) {
        int u = s.top(); s.pop();
        cout << u << " ";
        for (auto v: g[u]) {
            if (!visited[v]) {
                s.push(v);
                visited[v] = true;
            }
        }
    }
    cout << endl;
}

void dfs_list(vector<vector<int>> &g) {
    cout << "DFS LIST:\n";

    int n = g.size();
    bool* visited = new bool[n]();

    for (int i = 0; i < n; i++) {
        if (!visited[i])
            dfs_list_visit(g, i, visited);
    }
}

// MATRIX
void dfs_matrix_visit(vector<vector<int>> &g, int start, bool* visited) {
    stack<int> s;

    s.push(start);
    visited[start] = true;

    while (!s.empty()) {
        int u = s.top(); s.pop();
        cout << u << " ";

        for (int v = 0; v < g.size(); v++) {
            if (g[u][v] == 1 && !visited[v]) {
                s.push(v);
                visited[v] = true;
            }
        }
    }

    cout << endl;
}

void dfs_matrix(vector<vector<int>> &g) {
    cout << "DFS MATRIX:\n";

    int n = g.size();
    bool* visited = new bool[n]();

    // This for loop is only beneficial when your graph is disconnected
    for (int i = 0; i < n; i++) {
        if (!visited[i])
            dfs_matrix_visit(g, i, visited);
    }

    // If connected, you can do it in single call:
    // dfs_matrix_visit(g, 2, visited);
}


// 2 functions: dfs_visit, dfs

void dfs_visit(vector<vector<int>> &g, int u, bool* visited) {
    visited[u] = true;
    cout << u << " ";

    for (auto v: g[u]) {
        if (!visited[v])
            dfs_visit(g, v, visited);
    }
}

void dfs(vector<vector<int>> &g) {
    cout << "RECURSIVE DFS LIST:\n";

    int n = g.size();
    bool* visited = new bool[n]();

    for (int i = 0; i < n; i++) {
        if (!visited[i])
            dfs_visit(g, i, visited);
    }
    cout << endl;
}

int main() {
    int n, e; cin >> n >> e;

    // Adjacency list
    vector<vector<int>> adj_list(n, vector<int>());

    // Adjacency matrix
    vector<vector<int>> adj_matrix(n, vector<int>(n, 0));   // nxn matrix all zeros

    // Our nodes are from 0 to n-1
    while (e--) {
        int u, v; cin >> u >> v;
        add_edge_list(adj_list, u, v);
        add_edge_matrix(adj_matrix, u, v);
    }

    dfs_list(adj_list);
    dfs_matrix(adj_matrix);
    dfs(adj_list);

    return 0;
}
```

---

<a id="file-graphs-dfs-py"></a>
### `graphs/dfs.py`

- **Language:** Python
- **Path:** `graphs/dfs.py`
- **Lines:** 93
- [↑ Back to Top](#table-of-contents)

```python
def add_edge_list(g, u, v):
    g[u].append(v)
    g[v].append(u)  # Delete this line if the graph is directed

def add_edge_matrix(g, u, v):
    g[u][v] = 1
    g[v][u] = 1  # Delete this line for directed graph

def dfs_list_visit(g, start, visited):
    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        u = stack.pop()
        print(u, end=" ")
        for v in g[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
    print()

def dfs_list(g):
    print("DFS LIST:")
    n = len(g)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs_list_visit(g, i, visited)

def dfs_matrix_visit(g, start, visited):
    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        u = stack.pop()
        print(u, end=" ")
        for v in range(len(g)):
            if g[u][v] == 1 and not visited[v]:
                stack.append(v)
                visited[v] = True
    print()

def dfs_matrix(g):
    print("DFS MATRIX:")
    n = len(g)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs_matrix_visit(g, i, visited)

def dfs_visit(g, u, visited):
    visited[u] = True
    print(u, end=" ")

    for v in g[u]:
        if not visited[v]:
            dfs_visit(g, v, visited)

def dfs(g):
    print("RECURSIVE DFS LIST:")
    n = len(g)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs_visit(g, i, visited)
    print()

def main():
    n, e = map(int, input().split())

    # Adjacency list
    adj_list = [[] for _ in range(n)]

    # Adjacency matrix
    adj_matrix = [[0] * n for _ in range(n)]

    # Our nodes are from 0 to n-1
    for _ in range(e):
        u, v = map(int, input().split())
        add_edge_list(adj_list, u, v)
        add_edge_matrix(adj_matrix, u, v)

    dfs_list(adj_list)
    dfs_matrix(adj_matrix)
    dfs(adj_list)

if __name__ == "__main__":
    main()

```

---

<a id="file-graphs-largest_island_dfs_grid-cpp"></a>
### `graphs/largest_island_dfs_grid.cpp`

- **Language:** C++
- **Path:** `graphs/largest_island_dfs_grid.cpp`
- **Lines:** 71
- [↑ Back to Top](#table-of-contents)

```cpp
/*  PROBLEM:

    Given a 2D square matrix of size N that contains 0s and 1s. 1 represents land
    and 0 represents water. Two lands with 1s belong to same island, if
    they share an edge with each other. Find the size of the largest island.

    Input:
    Line 1 : An integer N denoting the size of graph
    Next N lines : N characters denoting the graph

    Output:
    Size of the biggest piece of '1's and no '0's

    Constraints:
    1 <= N <= 50
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX 51   // constraints

// Main Logic of Code  (DFSVisit)
int dfs (char graph[MAX][MAX], int n, bool** visited, int i, int j, int count) {
    visited[i][j] = true;

    if (i > 0 && graph[i-1][j] == '1' && !visited[i-1][j])
        count = dfs (graph, n, visited, i-1, j, count) + 1;
    if (j < n-1 && graph[i][j+1] == '1' && !visited[i][j+1])
        count = dfs (graph, n, visited, i, j+1, count) + 1;
    if (i < n-1 && graph[i+1][j] == '1' && !visited[i+1][j])
        count = dfs (graph, n, visited, i+1, j, count) + 1;
    if (j > 0 && graph[i][j-1] == '1' && !visited[i][j-1])
        count = dfs (graph, n, visited, i, j-1, count) + 1;

    return count;
}

// DFS
int largestIsland(char graph[MAX][MAX], int n) {
    bool** visited = new bool*[n];
    for (int i = 0; i < n; i++)
        visited[i] =  new bool[n]();

    int max = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (!visited[i][j] && graph[i][j] == '1') {
                int count = 0;
                int n = dfs(graph, n, visited, i, j, count) + 1;
                if (n > max)
                    max = n;
            }
            for (int k = 0; k < n; k++)
                for (int m = 0; m < n; m++)
                    visited[k][m] = false;
        }
    return max;
}

/* -------------- MAIN DRIVER CODE --------------- */
int main() {
    char graph[MAX][MAX];
    int n;
    cin >> n;
    for(int i=0; i<n; i++)
        scanf("%s", graph[i]);

    cout << largestIsland(graph, n) << endl;
    return 0;
}
```

---

<a id="file-graphs-minimum_moves_knight_bfs_grid-py"></a>
### `graphs/minimum_moves_knight_bfs_grid.py`

- **Language:** Python
- **Path:** `graphs/minimum_moves_knight_bfs_grid.py`
- **Lines:** 34
- [↑ Back to Top](#table-of-contents)

```python
from collections import deque

def min_knight_moves(start_x, start_y, target_x, target_y):
    # define the moves
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    visited = set()
    visited.add((start_x, start_y))
    q = deque([(start_x, start_y, 0)])

    while q:
        curr_x, curr_y, steps = q.popleft()

        if curr_x == target_x and curr_y == target_y:
            return steps
        
        for move in moves:
            new_x = curr_x + move[0]
            new_y = curr_y + move[1]

            if (new_x, new_y) not in visited and 1 <= new_x <= 8 and 1 <= new_y <= 8:
                q.append((new_x, new_y, steps+1))
                visited.add((new_x, new_y))

    return -1
    
start_x, start_y = 2, 1
target_x, target_y = 8, 5
result = min_knight_moves(start_x, start_y, target_x, target_y)

print(result)
```

---

<a id="file-graphs-mst-cpp"></a>
### `graphs/mst.cpp`

- **Language:** C++
- **Path:** `graphs/mst.cpp`
- **Lines:** 67
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Edge {
    public:
        int src, dest, weight;
};

bool compare(Edge e1, Edge e2) {
    return e1.weight < e2.weight;
}

int root(int v, int* parent) {
    if (parent[v] == v)
        return v;
    return root(parent[v], parent);
}

Edge* kruskal(Edge* edges, int n, int e) {
    Edge* output = new Edge[n-1];

    // Sort the edges
    sort(edges, edges + e, compare);

    // We need to have a parent array (for maintaining DSU)
    int* parent = new int[n];
    for (int i = 0; i < n; i++)
        parent[i] = i;

    int count = 0, i = 0;  // to break the loop when I have picked n-1 edges
    while (count < n-1) {
        Edge current_edge = edges[i];

        int src_parent = root(current_edge.src, parent);
        int dest_parent = root(current_edge.dest, parent);
        
        if (src_parent != dest_parent) {
            output[count] = current_edge;
            parent[src_parent] = dest_parent;
            count++;
        }

        i++;
    }

    return output;
}

int main() {

    int n, e; cin >> n >> e;

    Edge* edges = new Edge[e];
    for (int i = 0; i < e; i++) {
        cin >> edges[i].src >> edges[i].dest >> edges[i].weight;
    }

    cout << "Edges in MST:\n";

    Edge* output = kruskal(edges, n, e);

    for (int i = 0; i < n-1; i++) {
        cout << output[i].src << " " << output[i].dest << " " << output[i].weight << endl;
    }

    return 0;
}
```

---

<a id="file-graphs-path-cpp"></a>
### `graphs/path.cpp`

- **Language:** C++
- **Path:** `graphs/path.cpp`
- **Lines:** 226
- [↑ Back to Top](#table-of-contents)

```cpp
// PS: Given src node and dest node, give me a path between them

#include<bits/stdc++.h>
using namespace std;

// 'u' is a node 'from', 'v' is a node 'to': from u to v
void add_edge_list(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    g[v].push_back(u);      // Delete this line if graph is directed
}

void add_edge_matrix(vector<vector<int>> &g, int u, int v) {
    g[u][v] = 1;
    g[v][u] = 1;            // Delete this line for directed graph
}

// GET PATH CODES

bool get_path_list_dfs_rec(vector<vector<int>> &g, int src, int dest, vector<int> &path) {
    static bool* visited = new bool[g.size()](); 
    
    path.push_back(src);
    visited[src] = true;

    if (src == dest)
        return true;

    for (auto v: g[src]) {
        if (!visited[v]) {
            if (get_path_list_dfs_rec(g, v, dest, path))
                return true;
        }
    }

    path.pop_back();
    return false;
}

void get_path_list_dfs_itr(vector<vector<int>> &g, int src, int dest, vector<int> &path) {
    int n = g.size();
    bool* visited = new bool[n]();

    stack<int> s;
    s.push(src);
    visited[src] = true;

    while (!s.empty()) {
        int u = s.top();
        s.pop();
        path.push_back(u);

        if (u == dest) // If destination reached, break out of the loop
            break;

        bool found = false; // Flag to indicate if a neighbor leads to destination
        for (auto v : g[u]) {
            if (!visited[v]) {
                s.push(v);
                visited[v] = true;
                found = true;
                break; // Break after pushing the first unvisited neighbor
            }
        }

        if (!found) {
            path.pop_back(); // Remove the last node from path if no unvisited neighbor leads to destination
        }
    }    
}


void get_path_list_bfs(vector<vector<int>> &g, int src, int dest, vector<int> &path) {
    int n = g.size();
    bool* visited = new bool[n]();
    int* level = new int[n]();
    int* parent = new int[n]();
    queue<int> q;
    int i = 1;
    
    // process the start node
    q.push(src);
    visited[src] = true;
    level[src] = i-1;
    parent[src] = -1;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        // cout << u << " ";
        for (auto v: g[u]) {
            if (!visited[v]) {
                q.push(v);
                visited[v] = true;
                level[v] = i;
                parent[v] = u;
            }
        }
        i++;
    }
    // cout << endl;

    // To get the path, we will use parent array
    while (dest != -1) {
        path.push_back(dest);
        dest = parent[dest];
    }

    reverse(path.begin(), path.end());
}

void get_path_matrix_dfs(vector<vector<int>> &g, int src, int dest, vector<int> &path) {
    int n = g.size();
    bool* visited = new bool[n]();

    stack<int> s;
    s.push(src);
    visited[src] = true;

    while (!s.empty()) {
        int u = s.top();
        s.pop();
        path.push_back(u);

        if (u == dest) // If destination reached, break out of the loop
            break;

        bool found = false; // Flag to indicate if a neighbor leads to destination
        for (int v = 0; v < n; v++) {
            if (g[u][v] == 1 && !visited[v]) {
                s.push(v);
                visited[v] = true;
                found = true;
                break; // Break after pushing the first unvisited neighbor
            }
        }

        if (!found) {
            path.pop_back(); // Remove the last node from path if no unvisited neighbor leads to destination
        }
    }    
}

void get_path_matrix_bfs(vector<vector<int>> &g, int src, int dest, vector<int> &path) {
    int n = g.size();
    bool* visited = new bool[n]();
    int* level = new int[n]();
    int* parent = new int[n]();
    queue<int> q;
    int i = 1;
    
    // process the start node
    q.push(src);
    visited[src] = true;
    level[src] = i-1;
    parent[src] = -1;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        // cout << u << " ";
        for (int v = 0; v < n; v++) {
            if (g[u][v] == 1 && !visited[v]) {
                q.push(v);
                visited[v] = true;
                level[v] = i;
                parent[v] = u;
            }
        }
        i++;
    }
    // cout << endl;

    // To get the path, we will use parent array
    while (dest != -1) {
        path.push_back(dest);
        dest = parent[dest];
    }

    reverse(path.begin(), path.end());
}

int main() {
    int n, e; cin >> n >> e;

    // Adjacency list
    vector<vector<int>> adj_list(n, vector<int>());

    // Adjacency matrix
    vector<vector<int>> adj_matrix(n, vector<int>(n, 0));   // nxn matrix all zeros

    // Our nodes are from 0 to n-1
    while (e--) {
        int u, v; cin >> u >> v;
        add_edge_list(adj_list, u, v);
        add_edge_matrix(adj_matrix, u, v);
    }

    vector<int> path_1, path_2, path_3, path_4, path_5;
    get_path_list_dfs_rec(adj_list, 2, 5, path_1);
    get_path_list_dfs_itr(adj_list, 2, 5, path_2);
    get_path_list_bfs(adj_list, 2, 5, path_3);

    for (auto x: path_1)
        cout << x << " ";
    cout << endl;

    for (auto x: path_2)
        cout << x << " ";
    cout << endl;

    for (auto x: path_3)
        cout << x << " ";
    cout << endl;

    get_path_matrix_dfs(adj_matrix, 2, 5, path_4);
    get_path_matrix_bfs(adj_matrix, 2, 5, path_5);

    for (auto x: path_4)
        cout << x << " ";
    cout << endl;

    for (auto x: path_5)
        cout << x << " ";
    cout << endl;

}

// Note: List is more popular, so practice that!!
```

---

<a id="file-graphs-topo_sort-cpp"></a>
### `graphs/topo_sort.cpp`

- **Language:** C++
- **Path:** `graphs/topo_sort.cpp`
- **Lines:** 105
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

// 'u' is a node 'from', 'v' is a node 'to': from u to v
void add_edge_list(vector<vector<int>> &g, int u, int v) {
    g[u].push_back(v);      
    // g[v].push_back(u);      // Delete this line if graph is directed
}

void add_edge_matrix(vector<vector<int>> &g, int u, int v) {
    g[u][v] = 1;
    // g[v][u] = 1;            // Delete this line for directed graph
}

// Two functions to perform the DFS

// LIST
void topo_sort_list_visit(vector<vector<int>> &g, int start, bool* visited, stack<int> &s){
    visited[start] = true;

    for (auto v: g[start]) {
        if (!visited[v])
            topo_sort_list_visit(g, v, visited, s);
    }

    s.push(start);
}

void topo_sort_list(vector<vector<int>> &g) {
    cout << "Topo LIST:\n";

    int n = g.size();
    bool* visited = new bool[n]();
    stack<int> s;

    for (int i = 1; i < n; i++) {
        if (!visited[i])
            topo_sort_list_visit(g, i, visited, s);
    }

    // Print the stack
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}

// MATRIX
void topo_sort_matrix_visit(vector<vector<int>> &g, int start, bool* visited, stack<int> &s) {
    visited[start] = true;

    for (int v = 1; v < g.size(); v++) {
        if (g[start][v] == 1 && !visited[v])
            topo_sort_matrix_visit(g, v, visited, s);
    }

    s.push(start);
}

void topo_sort_matrix(vector<vector<int>> &g) {
    cout << "Topo MATRIX:\n";

    int n = g.size();
    bool* visited = new bool[n]();
    stack<int> s;

    // This for loop is only beneficial when your graph is disconnected
    for (int i = 1; i < n; i++) {
        if (!visited[i])
            topo_sort_matrix_visit(g, i, visited, s);
    }

    // If connected, you can do it in single call:
    // dfs_matrix_visit(g, 2, visited);

    // Print the stack
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;    
}

int main() {
    int n, e; cin >> n >> e;

    // Adjacency list
    vector<vector<int>> adj_list(n, vector<int>());

    // Adjacency matrix
    vector<vector<int>> adj_matrix(n, vector<int>(n, 0));   // nxn matrix all zeros

    // Our nodes are from 0 to n-1
    while (e--) {
        int u, v; cin >> u >> v;
        add_edge_list(adj_list, u, v);
        add_edge_matrix(adj_matrix, u, v);
    }

    topo_sort_list(adj_list);
    topo_sort_matrix(adj_matrix);

    return 0;
}
```

---

<a id="dir-interview-questions"></a>
## Directory: `interview questions/`

<a id="file-interview-questions-google_log_truncate-cpp"></a>
### `interview questions/google_log_truncate.cpp`

- **Language:** C++
- **Path:** `interview questions/google_log_truncate.cpp`
- **Lines:** 114
- [↑ Back to Top](#table-of-contents)

```cpp
/**
 * Google Log Truncation Problem:
 * There is a logging system kept inside a machine. Which logs all the logs and saves in a file.
Truncate the logs with fair manner and save it.

Class Logs{
String filename;
String log;
}

Max = 30
List<Logs>

Output:
A: 15
B: 10
C: 5


Input : A: 50, B: 20, C: 5  size = 30

Output: A:12, B:13,C:5

A:”SOme log”
B:”log2”
C:”Log”
A:”SOme l”
C:lslsa”
A:”asd”












 */


#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

class LogTruncator {
private:
    const int MAX_TOTAL = 30;
    int currentTotal = 0;
    
    // Tracks count per filename/source
    std::unordered_map<std::string, int> usageMap;

public:
    void processLog(const std::string& source) {
        // 1. Check if the entire machine is full
        if (currentTotal >= MAX_TOTAL) {
            return; 
        }

        // Initialize source if it's the first time we see it (D, E, F...)
        if (usageMap.find(source) == usageMap.end()) {
            usageMap[source] = 0;
        }

        int sourceCount = usageMap[source];
        int numSources = usageMap.size();
        
        // 2. Calculate the fair share based on current unique sources
        // Using double for precision, then floor/cast for the limit
        int fairShare = MAX_TOTAL / numSources;

        /* Logic for "A:12, B:13, C:5":
           - C only takes 5.
           - A and B are allowed to exceed the 'fairShare' (10) 
             because the global 'currentTotal' hasn't hit 30 yet.
        */
        if (sourceCount < fairShare || currentTotal < MAX_TOTAL) {
            usageMap[source]++;
            currentTotal++;
            std::cout << "Saved " << source << " | Global: " << currentTotal << std::endl;
        }
    }

    void printFinalStats() {
        std::cout << "\n--- Final Allocation ---" << std::endl;
        for (const auto& pair : usageMap) {
            std::cout << pair.first << ": " << pair.second << std::endl;
        }
    }
};

int main() {
    LogTruncator tracker;

    // Simulated stream: A and B are heavy, C is light, D appears later
    std::vector<std::string> stream = {
        "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", // C hits 5 here
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", // A and B flooding
        "D", "E", "F" // These arrive but system might be full
    };

    for (const std::string& s : stream) {
        tracker.processLog(s);
    }

    tracker.printFinalStats();

    return 0;
}
```

---

<a id="dir-linked_list"></a>
## Directory: `linked_list/`

<a id="file-linked_list-crud_ll-py"></a>
### `linked_list/crud_ll.py`

- **Language:** Python
- **Path:** `linked_list/crud_ll.py`
- **Lines:** 140
- [↑ Back to Top](#table-of-contents)

```python
class Node:
    # Data  (In py, the data is always put in the __init__ function)
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    # Data
    def __init__(self):
        self.head = None

    # Functions

    # --------------- CREATE ------------------

    # Adds node with data at the end
    def append(self, data):
        new_node = Node(data)
        # If the linked list is empty
        if self.head is None:
            self.head = new_node
            return
        # If the head is not empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  
        last_node.next = new_node


    # Insert a node at a specific position
    def insert(self, data, pos):
        new_node = Node(data)
        # Add at the start
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return 
        
        current_node = self.head
        count = 1
        while current_node and count < pos:
            current_node = current_node.next
            count += 1

        # If your current node is null, you must have gone beyond the list
        if not current_node:
            print("Error: Your position is longer than the linked list.")
            return

        new_node.next = current_node.next
        current_node.next = new_node

    # ------------------ READ -------------------------

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # ------------------ UPDATE -----------------------

    def replace(self, new_data, pos):
        current_node = self.head
        count = 0
        while current_node and count < pos:
            current_node = current_node.next
            count += 1

        # If your current node is null, you must have gone beyond the list
        if not current_node:
            print("Error: Your position is longer than the linked list.")
            return
    
        current_node.data = new_data
    
    # ----------------- DELETE -------------------------
    
    def delete(self, value):
        current_node = self.head

        # If the first element needs to be deleted
        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("Error: Value to be deleted not found.")
            return
        
        prev_node.next = current_node.next
        current_node = None
    
    # ------------ Overriding Python's existing functions -------------------

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            length += 1
        return length
    
        
def main():
    ll = LinkedList()

    ll.append(1)     # 1 -> null
    ll.append(2)     # 1 -> 2 -> null
    for i in range(3, 6):
        ll.append(i)    # 1-> 2 -> 3 -> 4 -> 5 -> null

    ll.print()   # 1 2 3 4 5

    ll.insert(6, 2)   # 1-> 2 -> 6 -> 3 -> 4 -> 5 -> null
    ll.insert(7, 4)   # 1-> 2 -> 6 -> 3 -> 7 -> 4 -> 5 -> null

    ll.print()  # 1 2 6 3 7 4 5

    ll.replace(16, 2)  

    ll.print()  # 1 2 16 3 7 4 5

    ll.delete(16)
    ll.delete(5)
    ll.delete(7)

    ll.print()  # 1 2 3 4

    print(len(ll))   # 4

if __name__ == "__main__":
    main()
```

---

<a id="file-linked_list-loops_intersections-py"></a>
### `linked_list/loops_intersections.py`

- **Language:** Python
- **Path:** `linked_list/loops_intersections.py`
- **Lines:** 107
- [↑ Back to Top](#table-of-contents)

```python
from crud_ll import LinkedList, Node

class LinkedListLoop(LinkedList):

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False


    def remove_loop(self):
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):    # You are at meeting point
                # We have found the loop
                fast = self.head

                # We will increment both by 1 step, till their next matches
                while slow.next != fast.next:
                    fast = fast.next
                    slow = slow.next

                # slow is just one step before the looping point
                slow.next = None
                return True
            
        return False
    

    def find_intersection(self, l2):
        visited  = set()

        current = self.head
        while current:
            visited.add(current)
            current = current.next

        current = l2.head
        while current:
            if current in visited:
                return current
            current = current.next

        return None

def main():
    ll = LinkedListLoop()

    for i in range(1, 7):
        ll.append(i)
    ll.print()   # 1 2 3 4 5 6

    print(ll.detect_loop())   # false

    # loop is created
    last_node = ll.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = ll.head.next.next.next   # 6 is pointing back to 4

    print(ll.detect_loop())  # true

    ll.remove_loop()  

    print(ll.detect_loop())  # false


    l1 = LinkedListLoop()
    l2 = LinkedListLoop()
    intersection_node = Node(4)

    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.head.next.next.next = intersection_node
    l1.append(5)
    l1.append(6)
    l1.append(8)

    l2.append(2)
    l2.head.next = intersection_node

    l1.print()
    l2.print()

    ins_node = l1.find_intersection(l2)

    # Print will give you error if no intersection exists, 
    # because you will be trying to find None.data which doesnt make sense
    print(ins_node.data, ins_node)    



if __name__ == "__main__":
    main()
```

---

<a id="file-linked_list-ops_ll-py"></a>
### `linked_list/ops_ll.py`

- **Language:** Python
- **Path:** `linked_list/ops_ll.py`
- **Lines:** 108
- [↑ Back to Top](#table-of-contents)

```python
from loops_intersections import LinkedListLoop

class LinkedListOps(LinkedListLoop):

    # ---------------- REVERSE ---------------------
    def reverse(self):
        prev_node = None
        current_node = self.head
        next_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    # ------------------- SORTING -------------------
    def middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    
    def merge(self, left, right):
        result = None

        if not left:
            return right
        
        if not right:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    
    # Mergesort implementation
    def merge_sort(self, head):
        # Base condition (0 or 1 node): return
        if not head or not head.next: 
            return head
        
        # Get the middle node
        middle_node = self.middle(head)

        # Split the linked lists
        right_half = middle_node.next
        middle_node.next = None
        left_half = head

        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        result = self.merge(left, right)
        return result
    

    # Wrapper function that manipulates the head
    def sort(self):
        self.head = self.merge_sort(self.head)
    

def main():
    ll = LinkedListOps()

    for i in range(1, 7):
        ll.append(i)
    ll.print()
    ll.reverse()
    ll.print()

    l1 = LinkedListOps()

    l1.append(4)
    l1.append(3)
    l1.append(7)
    l1.append(2)
    l1.append(9)
    l1.append(5)
    l1.append(1)
    l1.append(6)
    l1.append(8)

    l1.print()
    l1.sort()
    l1.print()

    # print(l1.detect_loop())


if __name__ == "__main__":
    main()
```

---

<a id="dir-my_codes"></a>
## Directory: `my_codes/`

<a id="file-my_codes-two_pointer-cpp"></a>
### `my_codes/two_pointer.cpp`

- **Language:** C++
- **Path:** `my_codes/two_pointer.cpp`
- **Lines:** 7
- [↑ Back to Top](#table-of-contents)

```cpp
#include <iostream>
using namespace std;

int main() {
    // Your code here
    return 0;
}

```

---

<a id="dir-range-queries"></a>
## Directory: `range queries/`

<a id="file-range-queries-segment_tree-cpp"></a>
### `range queries/segment_tree.cpp`

- **Language:** C++
- **Path:** `range queries/segment_tree.cpp`
- **Lines:** 120
- [↑ Back to Top](#table-of-contents)

```cpp
#include <bits/stdc++.h>
using namespace std;

class SegmentTree
{
private:
    vector<int> tree;
    vector<int> lazy;
    int n;

    void build(const vector<int>& data, int node, int start, int end) {
        if (start == end) {
            tree[node] = data[start];
        } else {
            int mid = (start + end) / 2;
            build(data, 2 * node, start, mid);
            build(data, 2 * node + 1, mid + 1, end);
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }

    void updateRangeUtil(int node, int start, int end, int l, int r, int value) 
    {
        // Previous updates are not propagated
        if (lazy[node] != 0) {
             // Consider for a second root node: 0 to n-1 => +x
             // lazy[node] => x
             // tree[node] => ??? x*(#values => e-s+1 => n*x)
            tree[node] += (end - start + 1) * lazy[node];
            if (start != end) {
                lazy[2 * node] += lazy[node];
                lazy[2 * node + 1] += lazy[node];
            }
            // Because previous updates are applied => Convert lazy[node] = 0 (no more updates for future)
            lazy[node] = 0;
        }

        // When there is no overlap
        if (start > end || start > r || end < l) {
            return;
        }

        // Complete overlap
        if (start >= l && end <= r) {
            tree[node] += (end - start + 1) * value;
            if (start != end) {
                lazy[2 * node] += value;
                lazy[2 * node + 1] += value;
            }
            return;
        }

        // Partial overlaps scenario
        int mid = (start + end) / 2;
        updateRangeUtil(2 * node, start, mid, l, r, value);
        updateRangeUtil(2 * node + 1, mid + 1, end, l, r, value);
        tree[node] = tree[2 * node] + tree[2 * node + 1];tree[2 * node + 1];
    }

    int queryRangeUtil(int node, int start, int end, int l, int r) 
    {
        if (start > end || start > r || end < l) {
            return 0;
        }

        // pending updates
        if (lazy[node] != 0) {
            tree[node] += (end - start + 1) * lazy[node];
            if (start != end) {
                lazy[2 * node] += lazy[node];
                lazy[2 * node + 1] += lazy[node];
            }
            lazy[node] = 0;
        }

        // complete overlap
        if (start >= l && end <= r) {
            return tree[node];
        }

        // Partial overlap recursion
        int mid = (start + end) / 2;
        int leftSum = queryRangeUtil(2 * node, start, mid, l, r);
        int rightSum = queryRangeUtil(2 * node + 1, mid + 1, end, l, r);
        return leftSum + rightSum;
    }

public:
    // constructor
    SegmentTree(const vector<int> &data)
    {
        n = data.size();
        tree.resize(4 * n);
        lazy.resize(4 * n, 0);
        build(data, 1, 0, n - 1);
    }

    void updateRange(int l, int r, int value) {
        updateRangeUtil(1, 0, n - 1, l, r, value);
    }

    int queryRange(int l, int r) {
        return queryRangeUtil(1, 0, n - 1, l, r);
    }
};

int main()
{
    vector<int> data = {1, 3, 5, 7, 9, 11};
    SegmentTree segTree(data);

    // Range sum query from index 1 to 3 (inclusive)
    cout << segTree.queryRange(1, 3) << endl; // Output: 15 (3 + 5 + 7)

    // Range update: Increment elements from index 1 to 3 by 10
    segTree.updateRange(1, 3, 10);
    cout << segTree.queryRange(1, 3) << endl; // Output: 45 (13 + 15 + 17)

    return 0;
}
```

---

<a id="dir-recursion_backtracking"></a>
## Directory: `recursion_backtracking/`

<a id="file-recursion_backtracking-02_backtracking-knights_tour-cpp"></a>
### `recursion_backtracking/02_Backtracking/knights_tour.cpp`

- **Language:** C++
- **Path:** `recursion_backtracking/02_Backtracking/knights_tour.cpp`
- **Lines:** 72
- [↑ Back to Top](#table-of-contents)

```cpp
#include <bits/stdc++.h>
using namespace std;

#define N 5

// --------- Helper functions ----------
void print(int board[N][N]) {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            printf(" %2d", board[x][y]);
        }
        cout << endl;
    }
}

bool is_safe(int x, int y, int board[N][N]) {
    // 2 things to check: x, y is a valid position on the board and 
    // the cell is not visited before. 
    return (x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1);
}


// ------------ MAIN LOGIC ---------------
// level is the move in the case. You have to cover, N*N moves. 
bool knights_tour(int x, int y, int move, int board[N][N], int x_move[N], int y_move[N]) {
    if (move == N*N) 
        return true;

    bool is_valid = false;

    // For a knight, there are always 8 possible jumps given any square
    for (int i = 0; i < 8; i++) {
        int next_x = x + x_move[i];
        int next_y = y + y_move[i];

        if (is_safe(next_x, next_y, board)) {
            board[next_x][next_y] = move;

            if (knights_tour(next_x, next_y, move+1, board, x_move, y_move)) {
                is_valid = true;
                return is_valid;
            }

            board[next_x][next_y] = -1;
        }
    }

    return is_valid;
}



int main() {
    int board[N][N];

    for (int x = 0; x < N; x++)
        for (int y = 0; y < N; y++)
            board[x][y] = -1;

    // The way knight moves
    int x_move[8] = {2, 2, 1, 1, -2, -2, -1, -1};
    int y_move[8] = {1, -1, 2, -2, 1, -1, 2, -2};

    board[0][0] = 0;  // knight starts at (0, 0)

    if (!knights_tour(0, 0, 1, board, x_move, y_move))
        cout << "Solution doesn't exist for this n." << endl;
    else 
        print(board);

    return 0;
}
```

---

<a id="file-recursion_backtracking-02_backtracking-n_queens-cpp"></a>
### `recursion_backtracking/02_Backtracking/n_queens.cpp`

- **Language:** C++
- **Path:** `recursion_backtracking/02_Backtracking/n_queens.cpp`
- **Lines:** 86
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

// -------- Helper functions ----------
// print() just prints the board.
void print(vector<vector<int>> &board) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// is_safe() checks if the queen is safe at board[i][col].
bool is_safe(int row, int col, vector<vector<int>> &board) {
    // Check if there is any queen in same row on previous columns
    for (int i = 0; i < col; i++) 
        if (board[row][i])
            return false;

    // Check for upper diagonal  
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) 
        if (board[i][j])
            return false;

    // Check for lower diagonal
    for (int i = row, j = col; i < board.size() && j >= 0; i++, j--)
        if (board[i][j])
            return false;

    return true;
}


// --------- MAIN LOGIC ---------------
// Level in this game is about columns.
bool n_queens(int col, vector<vector<int>> &board) {
    if (col >= board.size()) {
        print(board);
        return true;
    }

    bool is_valid = false;

    // Checking all possibilities
    for (int i = 0; i < board.size(); i++) {
        // Checking if constraint is satisfied
        if (is_safe(i, col, board)) {
            // Considering this to be a potential possibility
            board[i][col] = 1;

            // Try to solve for further levels
            if (n_queens(col+1, board)) {
                is_valid = true;
                // return is_valid;   // This commented means all possibilities
            }

            // If unable to solve for further levels, remove the potential possibility
            board[i][col] = 0;
        }
    }

    return is_valid;
}


int main() {
    int n; cin >> n;

    // nxn board with all zeros
    vector<vector<int>> board(n, vector<int>(n, 0));

    if (!n_queens(0, board))
        cout << "Solution doesn't exist for this value of n." << endl;

    return 0;
}

/*

Note: If you comment, the return is_valid statement inside if block, you will print 
all the solutions!!

*/
```

---

<a id="file-recursion_backtracking-02_backtracking-subset_sum_with_subsets-cpp"></a>
### `recursion_backtracking/02_Backtracking/subset_sum_with_subsets.cpp`

- **Language:** C++
- **Path:** `recursion_backtracking/02_Backtracking/subset_sum_with_subsets.cpp`
- **Lines:** 49
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;


void subset_sum_with_subsets(int n, int sum, vector<int> &arr, vector<vector<int>> &result, vector<int> &path) {
    if (sum == 0) {
        result.push_back(path);
        return;
    }

    if (n < 0 || sum < 0)
        return;

    // Exclude/Skip the current element
    subset_sum_with_subsets(n-1, sum, arr, result, path);

    // Include/Pick the current element
    if (sum >= arr[n]) {
        path.push_back(arr[n]);
        subset_sum_with_subsets(n-1, sum-arr[n], arr, result, path);
        path.pop_back();
    }
}


int main() {
    int n, sum; cin >> n >> sum;
    vector<int> arr; 

    int temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        arr.push_back(temp);
    } 

    vector<vector<int>> result;
    vector<int> path;

    subset_sum_with_subsets(n-1, sum, arr, result, path);

    for (auto subset: result) {
        for (int x: subset) {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}
```

---

<a id="dir-stacks_queues"></a>
## Directory: `stacks_queues/`

<a id="file-stacks_queues-max_area_hist-cpp"></a>
### `stacks_queues/max_area_hist.cpp`

- **Language:** C++
- **Path:** `stacks_queues/max_area_hist.cpp`
- **Lines:** 92
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> nsr_i(vector<int> arr) {
    int n = arr.size();
    // first element is the array value, second element is index
    stack<pair<int, int>> s;

    vector<int> result;

    for (int i = n-1; i >= 0; i--) {

        while (!s.empty() && s.top().first >= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(n);
        else 
            result.push_back(s.top().second);

        s.push({arr[i], i});
    }

    reverse(result.begin(), result.end());

    return result;
}

vector<int> nsl_i(vector<int> arr) {
    int n = arr.size();
    stack<pair<int, int>> s;

    vector<int> result;

    for (int i = 0; i < n; i++) {

        while (!s.empty() && s.top().first >= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top().second);

        s.push({arr[i], i});
    }

    // reverse(result.begin(), result.end());

    return result;
}


int main() {

    vector<int> hist = {6, 2, 5, 4, 5, 1, 6};

    vector<int> nsr_index = nsr_i(hist);
    vector<int> nsl_index = nsl_i(hist);

    // cout << "NSR_i: ";
    // for (auto x: ans) 
    //     cout << x  << " ";
    // cout << endl;

    // cout << "NSL_i: ";
    // for (auto x: ans2) 
    //     cout << x << " ";
    // cout << endl;

    vector<int> width;

    for (int i = 0; i < hist.size(); i++) {
        int w = nsr_index[i] - nsl_index[i] - 1;
        width.push_back(w);
    }

    // cout << "WIDTH: ";
    // for (auto x: width)
    //     cout << x << " ";
    // cout << endl;

    int max_area = 0;
    for (int i = 0; i < width.size(); i++) {
        int area = hist[i]*width[i];
        max_area = max(max_area, area);
    }

    cout << max_area << endl;

    return 0;
} 
```

---

<a id="file-stacks_queues-max_area_hist-java"></a>
### `stacks_queues/max_area_hist.java`

- **Language:** Java
- **Path:** `stacks_queues/max_area_hist.java`
- **Lines:** 65
- [↑ Back to Top](#table-of-contents)

```java
import java.util.*;

public class Main {
    
    static List<Integer> nsr_i(List<Integer> arr) {
        int n = arr.size();
        Stack<Pair<Integer, Integer>> s = new Stack<>();
        List<Integer> result = new ArrayList<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!s.isEmpty() && s.peek().getKey() >= arr.get(i))
                s.pop();

            if (s.isEmpty())
                result.add(n);
            else
                result.add(s.peek().getValue());

            s.push(new Pair<>(arr.get(i), i));
        }

        Collections.reverse(result);
        return result;
    }

    static List<Integer> nsl_i(List<Integer> arr) {
        int n = arr.size();
        Stack<Pair<Integer, Integer>> s = new Stack<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            while (!s.isEmpty() && s.peek().getKey() >= arr.get(i))
                s.pop();

            if (s.isEmpty())
                result.add(-1);
            else
                result.add(s.peek().getValue());

            s.push(new Pair<>(arr.get(i), i));
        }

        return result;
    }

    public static void main(String[] args) {
        List<Integer> hist = Arrays.asList(6, 2, 5, 4, 5, 1, 6);
        List<Integer> nsr_index = nsr_i(hist);
        List<Integer> nsl_index = nsl_i(hist);

        List<Integer> width = new ArrayList<>();
        for (int i = 0; i < hist.size(); i++) {
            int w = nsr_index.get(i) - nsl_index.get(i) - 1;
            width.add(w);
        }

        int max_area = 0;
        for (int i = 0; i < width.size(); i++) {
            int area = hist.get(i) * width.get(i);
            max_area = Math.max(max_area, area);
        }

        System.out.println(max_area);
    }
}

```

---

<a id="file-stacks_queues-max_area_hist-py"></a>
### `stacks_queues/max_area_hist.py`

- **Language:** Python
- **Path:** `stacks_queues/max_area_hist.py`
- **Lines:** 57
- [↑ Back to Top](#table-of-contents)

```python
def nsr_i(arr):
    n = len(arr)
    s = []
    result = []

    for i in range(n - 1, -1, -1):
        while s and s[-1][0] >= arr[i]:
            s.pop()

        if not s:
            result.append(n)
        else:
            result.append(s[-1][1])

        s.append((arr[i], i))

    result.reverse()
    return result

def nsl_i(arr):
    n = len(arr)
    s = []
    result = []

    for i in range(n):
        while s and s[-1][0] >= arr[i]:
            s.pop()

        if not s:
            result.append(-1)
        else:
            result.append(s[-1][1])

        s.append((arr[i], i))

    return result

def main():
    hist = [6, 2, 5, 4, 5, 1, 6]

    nsr_index = nsr_i(hist)
    nsl_index = nsl_i(hist)

    width = []
    for i in range(len(hist)):
        w = nsr_index[i] - nsl_index[i] - 1
        width.append(w)

    max_area = 0
    for i in range(len(width)):
        area = hist[i] * width[i]
        max_area = max(max_area, area)

    print(max_area)

if __name__ == "__main__":
    main()

```

---

<a id="file-stacks_queues-mergerods-java"></a>
### `stacks_queues/mergeRods.java`

- **Language:** Java
- **Path:** `stacks_queues/mergeRods.java`
- **Lines:** 28
- [↑ Back to Top](#table-of-contents)

```java
import java.util.PriorityQueue;

public class mergeRods {
    public static int minCostRodsMerge(int[] arr) {
        int cost = 0;

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int x : arr)
            minHeap.add(x);

        while (minHeap.size() > 1) {
            int rod1 = minHeap.poll();
            int rod2 = minHeap.poll();

            cost += rod1 + rod2;

            minHeap.add(rod1 + rod2);
        }

        return cost;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 1, 4};

        System.out.println(minCostRodsMerge(arr));
    }
}

```

---

<a id="file-stacks_queues-merge_rods-cpp"></a>
### `stacks_queues/merge_rods.cpp`

- **Language:** C++
- **Path:** `stacks_queues/merge_rods.cpp`
- **Lines:** 29
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

int min_cost_rods_merge(vector<int> arr) {
    int cost = 0;

    priority_queue<int, vector<int>, greater<int>> min_heap;
    for (auto x: arr)
        min_heap.push(x);

    while (min_heap.size() > 1) {
        int rod1 = min_heap.top(); min_heap.pop();
        int rod2 = min_heap.top(); min_heap.pop();

        cost += rod1 + rod2;

        min_heap.push(rod1+rod2);
    }

    return cost;
}

int main() {
    vector<int> arr = {1, 2, 3, 2, 1, 4};

    cout << min_cost_rods_merge(arr) << endl;

    return 0;
}
```

---

<a id="file-stacks_queues-merge_rods-py"></a>
### `stacks_queues/merge_rods.py`

- **Language:** Python
- **Path:** `stacks_queues/merge_rods.py`
- **Lines:** 20
- [↑ Back to Top](#table-of-contents)

```python
import heapq

def min_cost_rods_merge(arr):
    cost = 0

    min_heap = arr[:]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        rod1 = heapq.heappop(min_heap)
        rod2 = heapq.heappop(min_heap)

        cost += rod1 + rod2

        heapq.heappush(min_heap, rod1 + rod2)

    return cost

arr = [1, 2, 3, 2, 1, 4]
print(min_cost_rods_merge(arr))

```

---

<a id="file-stacks_queues-ngr_ngl-cpp"></a>
### `stacks_queues/ngr_ngl.cpp`

- **Language:** C++
- **Path:** `stacks_queues/ngr_ngl.cpp`
- **Lines:** 64
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> ngr(vector<int> arr) {
    int n = arr.size();
    stack<int> s;

    vector<int> result;

    for (int i = n-1; i >= 0; i--) {

        while (!s.empty() && s.top() <= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top());

        s.push(arr[i]);
    }

    reverse(result.begin(), result.end());

    return result;
}

vector<int> ngl(vector<int> arr) {
    int n = arr.size();
    stack<int> s;

    vector<int> result;

    for (int i = 0; i < n; i++) {

        while (!s.empty() && s.top() <= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top());

        s.push(arr[i]);
    }

    // reverse(result.begin(), result.end());

    return result;
}


int main() {

    vector<int> arr = {1, 3, 2, 2, 4, 1, 2, 1, 6};

    vector<int> ans = ngr(arr);

    for (auto x: ans) 
        cout << x  << " ";
    cout << endl;

    return 0;
} 
```

---

<a id="file-stacks_queues-ngr_ngl_index-cpp"></a>
### `stacks_queues/ngr_ngl_index.cpp`

- **Language:** C++
- **Path:** `stacks_queues/ngr_ngl_index.cpp`
- **Lines:** 64
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> ngr_i(vector<int> arr) {
    int n = arr.size();
    stack<int> s; // put the index in the stack

    vector<int> result; // put the index in the stack

    for (int i = n-1; i >= 0; i--) {

        while (!s.empty() && arr[s.top()] <= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top());

        s.push(i);
    }

    reverse(result.begin(), result.end());

    return result;
}

vector<int> ngl_i(vector<int> arr) {
    int n = arr.size();
    stack<int> s;

    vector<int> result;

    for (int i = 0; i < n; i++) {

        while (!s.empty() && arr[s.top()] <= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top());

        s.push(i);
    }

    // reverse(result.begin(), result.end());

    return result;
}


int main() {

    vector<int> arr = {1, 3, 2, 2, 4, 1, 2, 1, 6};

    vector<int> ans = ngl_i(arr);

    for (auto x: ans) 
        cout << x  << " ";
    cout << endl;

    return 0;
} 
```

---

<a id="file-stacks_queues-nsr_nsl-cpp"></a>
### `stacks_queues/nsr_nsl.cpp`

- **Language:** C++
- **Path:** `stacks_queues/nsr_nsl.cpp`
- **Lines:** 64
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> nsr(vector<int> arr) {
    int n = arr.size();
    stack<int> s;

    vector<int> result;

    for (int i = n-1; i >= 0; i--) {

        while (!s.empty() && s.top() >= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top());

        s.push(arr[i]);
    }

    reverse(result.begin(), result.end());

    return result;
}

vector<int> nsl(vector<int> arr) {
    int n = arr.size();
    stack<int> s;

    vector<int> result;

    for (int i = 0; i < n; i++) {

        while (!s.empty() && s.top() >= arr[i])
            s.pop();

        if (s.empty())
            result.push_back(-1);
        else 
            result.push_back(s.top());

        s.push(arr[i]);
    }

    // reverse(result.begin(), result.end());

    return result;
}


int main() {

    vector<int> arr = {1, 3, 2, 2, 4, 1, 2, 1, 6};

    vector<int> ans = nsl(arr);

    for (auto x: ans) 
        cout << x  << " ";
    cout << endl;

    return 0;
} 
```

---

<a id="file-stacks_queues-queues-cpp"></a>
### `stacks_queues/queues.cpp`

- **Language:** C++
- **Path:** `stacks_queues/queues.cpp`
- **Lines:** 36
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
    queue<int> q1;
    queue<string> q2;

    q1.push(1);
    q1.push(3);
    q1.push(7);

    for (int i = 4; i < 7; i++)
        q1.push(i);         // I am pushing 4, 5, 6

    // Total 6 elements in q1: Order of push: 1 3 7 4 5 6

    while (!q1.empty()) {
        int temp = q1.front();
        cout <<temp << " ";
        q1.pop();
    }
    cout << endl;

    q2.push("sagar");
    q2.push("vishnu");
    q2.push("shreya");

    while (!q2.empty()) {
        string temp = q2.front();
        cout << temp << " ";
        q2.pop();
    }
    cout << endl;

    return 0;
}
```

---

<a id="file-stacks_queues-queues-java"></a>
### `stacks_queues/queues.java`

- **Language:** Java
- **Path:** `stacks_queues/queues.java`
- **Lines:** 36
- [↑ Back to Top](#table-of-contents)

```java
import java.util.LinkedList;
import java.util.Queue;

public class queues {
    public static void main(String[] args) {
        Queue<Integer> q1 = new LinkedList<>();
        Queue<String> q2 = new LinkedList<>();

        q1.add(1);
        q1.add(3);
        q1.add(7);

        for (int i = 4; i < 7; i++)
            q1.add(i); // Pushing 4, 5, 6

        // Total 6 elements in q1: Order of push: 1 3 7 4 5 6

        while (!q1.isEmpty()) {
            int temp = q1.peek();
            System.out.print(temp + " ");
            q1.poll();
        }
        System.out.println();

        q2.add("sagar");
        q2.add("vishnu");
        q2.add("shreya");

        while (!q2.isEmpty()) {
            String temp = q2.peek();
            System.out.print(temp + " ");
            q2.poll();
        }
        System.out.println();
    }
}

```

---

<a id="file-stacks_queues-queues-py"></a>
### `stacks_queues/queues.py`

- **Language:** Python
- **Path:** `stacks_queues/queues.py`
- **Lines:** 29
- [↑ Back to Top](#table-of-contents)

```python
from collections import deque

q1 = deque()
q2 = deque()

q1.append(1)
q1.append(3)
q1.append(7)

for i in range(4, 7):
    q1.append(i)  # Pushing 4, 5, 6

# Total 6 elements in q1: Order of push: 1 3 7 4 5 6

while q1:
    temp = q1[0]
    print(temp, end=" ")
    q1.popleft()
print()

q2.append("sagar")
q2.append("vishnu")
q2.append("shreya")

while q2:
    temp = q2[0]
    print(temp, end=" ")
    q2.popleft()
print()

```

---

<a id="file-stacks_queues-stacks-cpp"></a>
### `stacks_queues/stacks.cpp`

- **Language:** C++
- **Path:** `stacks_queues/stacks.cpp`
- **Lines:** 36
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
    stack<int> s1;
    stack<string> s2;

    s1.push(1);
    s1.push(3);
    s1.push(7);

    for (int i = 4; i < 7; i++)
        s1.push(i);         // I am pushing 4, 5, 6

    // Total 6 elements in s1: Order of push: 1 3 7 4 5 6

    while (!s1.empty()) {
        int temp = s1.top();
        cout <<temp << " ";
        s1.pop();
    }
    cout << endl;

    s2.push("sagar");
    s2.push("vishnu");
    s2.push("shreya");

    while (!s2.empty()) {
        string temp = s2.top();
        cout << temp << " ";
        s2.pop();
    }
    cout << endl;

    return 0;
}
```

---

<a id="file-stacks_queues-stacks-java"></a>
### `stacks_queues/stacks.java`

- **Language:** Java
- **Path:** `stacks_queues/stacks.java`
- **Lines:** 33
- [↑ Back to Top](#table-of-contents)

```java
import java.util.Stack;

public class stacks {
    public static void main(String[] args) {
        Stack<Integer> s1 = new Stack<>();
        Stack<String> s2 = new Stack<>();

        s1.push(1);
        s1.push(3);
        s1.push(7);

        for (int i = 4; i < 7; i++)
            s1.push(i); // Pushing 4, 5, 6

        // Total 6 elements in s1: Order of push: 1 3 7 4 5 6

        while (!s1.isEmpty()) {
            int temp = s1.pop();
            System.out.print(temp + " ");
        }
        System.out.println();

        s2.push("sagar");
        s2.push("vishnu");
        s2.push("shreya");

        while (!s2.isEmpty()) {
            String temp = s2.pop();
            System.out.print(temp + " ");
        }
        System.out.println();
    }
}

```

---

<a id="file-stacks_queues-stacks-py"></a>
### `stacks_queues/stacks.py`

- **Language:** Python
- **Path:** `stacks_queues/stacks.py`
- **Lines:** 25
- [↑ Back to Top](#table-of-contents)

```python
s1 = []
s2 = []

s1.append(1)
s1.append(3)
s1.append(7)

for i in range(4, 7):
    s1.append(i)  # Pushing 4, 5, 6

# Total 6 elements in s1: Order of push: 1 3 7 4 5 6

while s1:
    temp = s1.pop()
    print(temp, end=" ")
print()

s2.append("sagar")
s2.append("vishnu")
s2.append("shreya")

while s2:
    temp = s2.pop()
    print(temp, end=" ")
print()

```

---

<a id="dir-strings"></a>
## Directory: `strings/`

<a id="file-strings-replace_words-py"></a>
### `strings/replace_words.py`

- **Language:** Python
- **Path:** `strings/replace_words.py`
- **Lines:** 57
- [↑ Back to Top](#table-of-contents)

```python
class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with children as a dictionary and is_end flag as False
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        # Initialize a root TrieNode
        self.new_node = TrieNode()
    
    def check(self, word: str) -> str:
        # Check the shortest prefix of the word in the Trie
        t = self.new_node
        s = ""
        
        for char in word:
            if char not in t.children:
                break
            s += char
            t = t.children[char]
            if t.is_end:
                return s
        
        return word
    
    def insert(self, word: str) -> None:
        # Insert a word into the Trie
        temp = self.new_node
        
        for char in word:
            if char not in temp.children:
                temp.children[char] = TrieNode()
            temp = temp.children[char]
        
        temp.is_end = True
    
    def replaceWords(self, dict, sentence: str) -> str:
        # Build the Trie from the dictionary and replace words in the sentence
        for word in dict:
            self.insert(word)
        
        words = sentence.split()
        ans = ""
        
        for word in words:
            ans += self.check(word) + " "
        
        return ans.strip()



# Example usage
solution = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(solution.replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"
```

---

<a id="file-strings-trie-py"></a>
### `strings/trie.py`

- **Language:** Python
- **Path:** `strings/trie.py`
- **Lines:** 56
- [↑ Back to Top](#table-of-contents)

```python
class TrieNode:
    def __init__(self):
        # Initialize a node with children as an empty dictionary and end_of_word flag as False
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert a word into the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                # If the character is not a child of the current node, add it
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # After inserting all characters, mark the end of the word
        node.end_of_word = True

    def search(self, word: str) -> bool:
        # Search for a word in the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                # If the character is not found, return False
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if the end_of_word flag is set, meaning the word is found
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Check if there is any word in the Trie that starts with the given prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                # If the character is not found, return False
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if the prefix is found
        return True

# Example usage
# # Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))   # return True
print(obj.search("app"))     # return False
print(obj.startsWith("app")) # return True
obj.insert("app")
print(obj.search("app"))     # return True

```

---

<a id="file-strings-z-py"></a>
### `strings/z.py`

- **Language:** Python
- **Path:** `strings/z.py`
- **Lines:** 48
- [↑ Back to Top](#table-of-contents)

```python
def calculate_z(s):
    n = len(s)  # Length of the input string
    Z = [0] * n  # Initialize the Z-array with zeros
    L, R, K = 0, 0, 0  # Initialize left and right pointers of the Z-box

    for i in range(1, n):
        if i > R:
            # Case 1: i is outside the current Z-box
            L, R = i, i
            while R < n and s[R] == s[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            # Case 2: i is inside the current Z-box
            K = i - L
            if Z[K] < R - i + 1:
                Z[i] = Z[K]
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

def z_algorithm_search(text, pattern):
    # Concatenate pattern, special character, and text
    concat = pattern + "$" + text
    # Compute Z-array for the concatenated string
    Z = calculate_z(concat)
    print(Z)
    pattern_length = len(pattern)  # Length of the pattern
    result = []  # List to store the indices of pattern occurrences

    for i in range(len(Z)):
        if Z[i] == pattern_length:
            # If Z[i] is equal to the length of the pattern, it means a match is found
            result.append(i - pattern_length - 1)

    return result

# Example usage
text = "ababcababcababc"
pattern = "ababc"
occurrences = z_algorithm_search(text, pattern)

print("Pattern found at indices:", occurrences)

```

---

<a id="dir-trees"></a>
## Directory: `trees/`

<a id="file-trees-01_recursion-basic_tree_recusion-cpp"></a>
### `trees/01_Recursion/basic_tree_recusion.cpp`

- **Language:** C++
- **Path:** `trees/01_Recursion/basic_tree_recusion.cpp`
- **Lines:** 71
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Node {
    public:
        int data;
        Node* left;
        Node* right;

        Node(int data) {
            this->data = data;
            this->left = this->right = NULL;
        }
};

int sum(Node* root) {
    if (root == NULL)
        return 0;
    return root->data + sum(root->left) + sum(root->right);
}

int height(Node* root) {
    if (root == NULL)
        return 0;

    return 1 + max(height(root->left), height(root->right));
}

int maximum(Node* root) {
    if (root == NULL)
        return 0;

    return max(root->data, max(maximum(root->left), maximum(root->right)));
}

bool search(Node* root, int key) {
    if (root == NULL)
        return false;

    if (root->data == key)
        return true;

    return search(root->left, key) || search(root->right, key);
}

int main() {

    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(7);
    root->left->right = new Node(3);
    root->right->left = new Node(4);
    root->right->right = new Node (5);
    root->right->right->right = new Node(6);

    /*
                 1
              2     7
                3  4  5
                        6 
    */

    cout << sum(root) << endl;
    cout << height(root) << endl;
    cout << maximum(root) << endl;

    cout << search(root, 4) << endl;
    cout << search(root, 9) << endl;

    return 0;
}
```

---

<a id="file-trees-01_recursion-trees_recursion-py"></a>
### `trees/01_Recursion/trees_recursion.py`

- **Language:** Python
- **Path:** `trees/01_Recursion/trees_recursion.py`
- **Lines:** 113
- [↑ Back to Top](#table-of-contents)

```python
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # P1: sum of all nodes in BT
    def sum_of_nodes(self, root):
        if root is None:
            return 0
        return root.data + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right)
    
    # Wrapper
    def sum(self):
        return self.sum_of_nodes(self.root)
    
    # P2: Height of the tree
    def height_of_tree(self, root):
        if root is None:
            return 0
        return 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))
    
    # P3: Finding the max element
    def max_element(self, root):
        if root is None:
            return 0
        return max(root.data, self.max_element(root.left), self.max_element(root.right))
    
    # P4: Check if the node exists or not
    def search(self, root, key):
        if root is None: 
            return False
        
        if root.data == key:
            return True
        
        return self.search(root.left, key) or self.search(root.right, key)
    
    # P5-P8: Check if a tree is of particular type
    def is_full(self, root):
        if root is None:
            return True
        
        if root.left is None and root.right is None: 
            return True
        
        if root.left is not None and root.right is not None: 
            return self.is_full(root.left) and self.is_full(root.right)

        return False
    
    def is_skewed(self, root):
        if root is None or (root.left is None and root.right is None):
            return True
        
        if root.left is None:
            return self.is_skewed(root.right)
        
        if root.right is None:
            return self.is_skewed(root.left)
        
        return False

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def is_perfect(self):
        height = self.height_of_tree(self.root)
        count = self.count_nodes(self.root)
        return count == 2**height - 1
    
    # Suggested:
    # 1. Get the height of tree
    # 2. Go on a level order traversal. Wait for the moment, till you find the first incomplete node (leaf node). 
    # If your incomplete node is on level < height - 1, tree is incomplete. 

    # Recursion:
    def is_complete(self, root, index, node_count):
        if root is None:
            return True
        
        if index >= node_count:
            return False
        
        return self.is_complete(root.left, 2*index + 1, node_count) and self.is_complete(root.right, 2*index+2, node_count)

tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)


print(tree.sum())
print(tree.height_of_tree(tree.root))
print(tree.max_element(tree.root))
print(tree.search(tree.root, 4))
print(tree.is_full(tree.root))
print(tree.is_skewed(tree.root))
print(tree.is_perfect())
print(tree.is_complete(tree.root, 0, tree.count_nodes(tree.root)))
```

---

<a id="file-trees-01_recursion-types_of_trees-cpp"></a>
### `trees/01_Recursion/types_of_trees.cpp`

- **Language:** C++
- **Path:** `trees/01_Recursion/types_of_trees.cpp`
- **Lines:** 127
- [↑ Back to Top](#table-of-contents)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Node {
    public:
        int data;
        Node* left;
        Node* right;

        Node(int data) {
            this->data = data;
            this->left = this->right = NULL;
        }
};

// check if tree is full
bool is_full(Node* root) {
    // If tree is empty
    if (root == NULL)
        return true;

    // If we are at a leaf node
    if (root->left == NULL && root->right == NULL)
        return true;

    // If left and right both should exist
    if (root->left && root->right)
        return is_full(root->left) && is_full(root->right);

    return false;
}

// check if tree is complete
int node_count(Node* root) {
    if (root == NULL) 
        return 0;
    return 1 + node_count(root->left) + node_count(root->right);
}

bool is_complete_helper(Node* root, int index, int num_nodes) {
    if (root == NULL)
        return true;
    
    if (index >= num_nodes)
        return false;
    
    return is_complete_helper(root->left, 2*index+1, num_nodes) && \
        is_complete_helper(root->right, 2*index+2, num_nodes);
}

bool is_complete(Node* root) {
    return is_complete_helper(root, 0, node_count(root));
}


// check if tree is perfect
int height(Node* root) {
    if (root == NULL)
        return 0;
    return 1 + max(height(root->left), height(root->right));
}

// All leaves should be at level = height - 1
bool is_perfect_helper(Node* root, int h, int level) {
    if (root == NULL)
        return true;
    
    if (root->left == NULL && root->right == NULL)
        return (level == h-1);
    
    if (root->left == NULL || root->right == NULL) 
        return false;

    return is_perfect_helper(root->left, h, level+1) && \
        is_perfect_helper(root->right, h, level+1);

}

bool is_perfect(Node* root) {
    int h = height(root);
    return is_perfect_helper(root, h, 0);
}


// check if tree is skewed
bool is_skewed(Node* root) {
    if (root == NULL || (root->left == NULL && root->right == NULL))
        return true;
    
    if (root->left && root->right)
        return false;

    if (root->left)
        return is_skewed(root->left);
    
    return is_skewed(root->right);
}



int main() {
    // First tree that is full

    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(7);
    root->left->right = new Node(3);
    root->left->left = new Node(8);
    root->right->left = new Node(4);
    root->right->right = new Node (5);
    root->left->left->left = new Node(6);
    root->left->left->right = new Node(9);

    /*
                 1
              2     7
           8    3  4  5
         6   9             
    */

    cout << is_full(root) << endl;
    cout << is_complete(root) << endl;
    cout << is_perfect(root) << endl;
    cout << is_skewed(root) << endl;
  
    return 0;
}
```

---

<a id="file-trees-diameter-py"></a>
### `trees/diameter.py`

- **Language:** Python
- **Path:** `trees/diameter.py`
- **Lines:** 39
- [↑ Back to Top](#table-of-contents)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter(root):
    if root is None:
        return 0
    
    diameter = 0

    left_height = height(root.left)
    right_height = height(root.right)

    diameter = max(diameter, left_height + right_height+1)

    return diameter

tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print(diameter(tree.root))
```

---

<a id="file-trees-lca-py"></a>
### `trees/lca.py`

- **Language:** Python
- **Path:** `trees/lca.py`
- **Lines:** 40
- [↑ Back to Top](#table-of-contents)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def find_lca(root, n1, n2):
    if root is None:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    
    if left_lca is not None: 
        return left_lca
    else:
        return right_lca


tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print(find_lca(tree.root, 7, 5).data)
```

---

<a id="file-trees-root_to_leaf_path-py"></a>
### `trees/root_to_leaf_path.py`

- **Language:** Python
- **Path:** `trees/root_to_leaf_path.py`
- **Lines:** 42
- [↑ Back to Top](#table-of-contents)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def root_to_leaf_paths(root):
    all_paths = []

    def traverse(node, path):
        if node is None: 
            return 
        
        path.append(node.data)

        if node.left is None and node.right is None:
            all_paths.append(list(path))
        else:
            traverse(node.left, path)
            traverse(node.right, path)

        path.pop()
        
    traverse(root, [])
    return all_paths        


tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print(root_to_leaf_paths(tree.root))
```

---

<a id="file-trees-root_to_node_path-py"></a>
### `trees/root_to_node_path.py`

- **Language:** Python
- **Path:** `trees/root_to_node_path.py`
- **Lines:** 45
- [↑ Back to Top](#table-of-contents)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def root_to_node_path(root, key):
    ans = []
    
    def traverse(node, key, path):
        nonlocal ans
        
        if node is None:
            return

        path.append(node.data)

        if node.data == key:
            ans = path.copy()
            return
        else:
            traverse(node.left, key, path)
            traverse(node.right, key, path)

        path.pop()

    traverse(root, key, [])
    return ans


tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print(root_to_node_path(tree.root, 7))
```

---

<a id="file-trees-trees-py"></a>
### `trees/trees.py`

- **Language:** Python
- **Path:** `trees/trees.py`
- **Lines:** 93
- [↑ Back to Top](#table-of-contents)

```python
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order_traversal(self):
        # Formalities/Edge Cases
        if self.root is None:
            return []

        result = []

        # Main logic
        q = deque()
        q.append(self.root)

        while q:
            level_nodes = []
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()
                # This is the place where you edit your elements
                level_nodes.append(curr.data)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            # This is the place where level shift happens
            result.append(level_nodes)

        return result
    
    def levels(self):
        result = self.level_order_traversal()
        return len(result)
    
    def preorder_traversal(self, root):
        # formalities
        if root is None:
            return []
        
        result = []
        result.append(root.data)
        result.extend(self.preorder_traversal(root.left))
        result.extend(self.preorder_traversal(root.right))
        return result

    def inorder_traversal(self, root):
        # formalities
        if root is None:
            return []
        
        result = []
        result.extend(self.inorder_traversal(root.left))
        result.append(root.data)
        result.extend(self.inorder_traversal(root.right))
        return result
    
    def postorder_traversal(self, root):
        # formalities
        if root is None:
            return []
        
        result = []
        result.extend(self.postorder_traversal(root.left))
        result.extend(self.postorder_traversal(root.right))
        result.append(root.data)
        return result

tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.left = Node(5)
tree.root.right.left.right = Node(6)

print(tree.level_order_traversal())
print(tree.levels())
print(tree.preorder_traversal(tree.root))
print(tree.inorder_traversal(tree.root))
print(tree.postorder_traversal(tree.root))
```

---

<a id="companion-data-files"></a>
## Companion Input & Data Files

> Supporting data and test inputs for factory pattern readers and graph algorithms.

<a id="file-design_patterns-04_factory-data-csv"></a>
### `design_patterns/04_Factory/data.csv`

- **Type:** CSV
- **Path:** `design_patterns/04_Factory/data.csv`
- **Lines:** 5
- [↑ Back to Top](#table-of-contents)

```csv
Name,Age,City
John,25,New York
Alice,30,Los Angeles
Bob,28,Chicago
Emily,35,San Francisco
```

---

<a id="file-design_patterns-04_factory-data-json"></a>
### `design_patterns/04_Factory/data.json`

- **Type:** JSON
- **Path:** `design_patterns/04_Factory/data.json`
- **Lines:** 22
- [↑ Back to Top](#table-of-contents)

```json
{
  "01":  {
      "name": "John",
      "age": 25,
      "city": "New York"
    },
  "02":{
      "name": "Alice",
      "age": 30,
      "city": "Los Angeles"
    },
  "03":{
      "name": "Bob",
      "age": 28,
      "city": "Chicago"
    },
  "04":{
      "name": "Emily",
      "age": 35,
      "city": "San Francisco"
    }
}
```

---

<a id="file-design_patterns-04_factory-data-xml"></a>
### `design_patterns/04_Factory/data.xml`

- **Type:** XML
- **Path:** `design_patterns/04_Factory/data.xml`
- **Lines:** 22
- [↑ Back to Top](#table-of-contents)

```xml
<people>
    <person>
        <name>John</name>
        <age>25</age>
        <city>New York</city>
    </person>
    <person>
        <name>Alice</name>
        <age>30</age>
        <city>Los Angeles</city>
    </person>
    <person>
        <name>Bob</name>
        <age>28</age>
        <city>Chicago</city>
    </person>
    <person>
        <name>Emily</name>
        <age>35</age>
        <city>San Francisco</city>
    </person>
</people>

```

---

<a id="file-graphs-in-txt"></a>
### `graphs/in.txt`

- **Type:** Plain Text
- **Path:** `graphs/in.txt`
- **Lines:** 11
- [↑ Back to Top](#table-of-contents)

```text
6 10
0 1 3
1 2 4
2 5 1
3 4 3
3 0 4
4 1 3
4 2 2
0 4 3
1 5 5
2 3 3
```

---

<a id="file-graphs-in2-txt"></a>
### `graphs/in2.txt`

- **Type:** Plain Text
- **Path:** `graphs/in2.txt`
- **Lines:** 5
- [↑ Back to Top](#table-of-contents)

```text
5 4
0 1
1 2
2 3
3 4
```

---

<a id="file-graphs-in3-txt"></a>
### `graphs/in3.txt`

- **Type:** Plain Text
- **Path:** `graphs/in3.txt`
- **Lines:** 6
- [↑ Back to Top](#table-of-contents)

```text
5 5
0 1
1 2
0 2
2 3
3 4
```

---
