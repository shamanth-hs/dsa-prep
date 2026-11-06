# LeetCode 76: Minimum Window Substring

- **Source File:** `[arrays/leetcode_sliding_window_map_76.cpp](file:///Users/shamanth/Desktop/DSA/problem-solving/arrays/leetcode_sliding_window_map_76.cpp)`
- **Language:** C++
- **Category:** Arrays / Sliding Window & Hash Maps
- **Navigation:** [← Back to Master Documentation Index](../README.md)

---

## 1. Problem Statement / Question

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`  
**Output:** `"BANC"`  
**Constraints:** $m, n \le 10^5$, English uppercase and lowercase letters.

---

## 2. Algorithm & Approach

1. Build frequency map of target string `t` in `target_map`. Track required distinct characters in `required`.
2. Expand window with right pointer `r`:
   - Decrement frequency in map; if count reaches 0, decrement `required`.
3. When `required == 0` (valid window found):
   - Check if current window `r - l + 1` is smaller than `min_len`.
   - Shrink window from left (`l++`): increment frequency in map; if character count becomes > 0, increment `required`.
4. Continue until right pointer reaches end of string.

---

## 3. Flowchart

```mermaid
graph TD
    Start[Init: target_map, l=0, r=0, min_len=INF] --> Expand[Read s[r], update map]
    Expand --> CheckReq{All chars in t matched?}
    CheckReq -- No --> IncR[r++]
    IncR --> EndCheck{r < s.length?}
    EndCheck -- Yes --> Expand
    CheckReq -- Yes --> UpdateMin[Update min_len and start_idx]
    UpdateMin --> Shrink[Shrink window: s[l], l++]
    Shrink --> CheckReq
    EndCheck -- No --> Finish[Return s.substr start_idx, min_len]
```

---

## 4. Source Code

```c++
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

## 5. Simple Dry Run

Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
- Target freq: `A:1, B:1, C:1`, `required = 3`
- Window expands to `"ADOBEC"` at index 5: all matched! Window size = 6.
- Window shrinks from left, removing `'A'`: `required` becomes 1.
- Expanding further until index 12 `"BANC"`: size = 4 < 6.
- Minimum window found is `"BANC"`.

---

## 6. Sample Output

```text
Minimum Window Substring: "BANC"
```

---

## 7. Complexity Analysis

- **Time Complexity:** $O(|s| + |t|)$ — each character is visited at most twice (by left and right pointers)
- **Space Complexity:** $O(|\Sigma|)$ where $\Sigma$ is the alphabet size (at most 128 for ASCII/hash map)

---
[← Back to Master Documentation Index](../README.md)
