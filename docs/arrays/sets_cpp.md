# Set Operations and Membership Testing in C++

- **Source File:** `[arrays/sets.cpp](file:///Users/shamanth/Desktop/DSA/problem-solving/arrays/sets.cpp)`
- **Language:** C++
- **Category:** Arrays / Hash Maps & Sets
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Demonstrate ordered set insertion, deduplication, size retrieval, and element membership lookup using `std::set<char>` in C++.

**Input:** A string with duplicate characters (e.g., `"banana"`).  
**Output:** Unique sorted characters, set size, and presence check for a query character.

---

## 2. Algorithm & Approach

1. Instantiate `std::set<char> s`.
2. Iterate through input characters and insert each into `s` (automatically deduplicated and ordered via Red-Black Tree).
3. Print unique sorted characters using range-based for loop.
4. Perform lookup using `s.find(c1)`: if iterator equals `s.end()`, element does not exist; otherwise it exists.

---

## 3. Flowchart

```mermaid
graph TD
    In[Read String] --> Loop[Iterate chars: s.insert c]
    Loop --> Print[Print unique sorted elements]
    Print --> Find[Check s.find query_char]
    Find --> Cond{iter == s.end()?}
    Cond -- Yes --> NotPres[Print: Not Present]
    Cond -- No --> Pres[Print: Present]
```

---

## 4. Source Code

```c++
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

## 5. Simple Dry Run

Input: `"banana"`, Query: `'z'`
1. Insert `'b'`: set = `{'b'}`
2. Insert `'a'`: set = `{'a', 'b'}`
3. Insert `'n'`: set = `{'a', 'b', 'n'}`
4. Duplicate `'a'`, `'n'`, `'a'` ignored.
5. Unique sorted: `a b n` (size: 3)
6. Search `'z'`: `s.find('z') == s.end()` -> `'z' is not present`.

---

## 6. Sample Output

```text
Unique Characters:
a b n 
Set Size: 3
z is not present in set
```

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n \log k)$ where $n$ is string length and $k$ is number of unique characters
- **Space Complexity:** $O(k)$ for Red-Black tree storage

---
[← Back to Master Documentation Index](../README.md)
