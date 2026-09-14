# 2273. Find Resultant Array After Removing Anagrams

**Difficulty:** Easy  
**Topics:** Array, String, Sorting, Hash Table  

## Problem Description

You are given a **0-indexed** string array `words`, where `words[i]` consists of lowercase English letters.

In one operation, select any index `i` such that `0 < i < words.length` and `words[i - 1]` and `words[i]` are **anagrams**, and **delete** `words[i]` from `words`. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return `words` *after performing all operations*. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, `"dacb"` is an anagram of `"abdc"`.

---

### Example 1:

**Input:** `words = ["abba","baba","bbaa","cd","cd"]`  
**Output:** `["abba","cd"]`  
**Explanation:**  
One of the ways we can obtain the resultant array is by using the following operations:
- Since `words[2] = "bbaa"` and `words[1] = "baba"` are anagrams, we choose index 2 and delete `words[2]`.  
  Now `words = ["abba","baba","cd","cd"]`.
- Since `words[1] = "baba"` and `words[0] = "abba"` are anagrams, we choose index 1 and delete `words[1]`.  
  Now `words = ["abba","cd","cd"]`.
- Since `words[2] = "cd"` and `words[1] = "cd"` are anagrams, we choose index 2 and delete `words[2]`.  
  Now `words = ["abba","cd"]`.  
We can no longer perform any operations, so `["abba","cd"]` is the final answer.

### Example 2:

**Input:** `words = ["a","b","c","d","e"]`  
**Output:** `["a","b","c","d","e"]`  
**Explanation:**  
No two adjacent strings in `words` are anagrams of each other, so no operations are performed.

---

### Constraints:

- $1 \le \text{words.length} \le 100$
- $1 \le \text{words}[i]\text{.length} \le 10$
- `words[i]` consists of lowercase English letters.

---

## Solution Approach

### Sequential Anagram Filtering

1. **Key Insight:**
   - Any contiguous block of consecutive strings that are anagrams of each other will be collapsed to only its first string.
   - When consecutive elements are anagrams, deleting the right neighbor will bring the next element next to the left neighbor.
   - Therefore, a word `words[i]` is retained if and only if it is **not an anagram** of the previously retained word.

2. **Algorithm:**
   - Initialize an empty result list `res`.
   - Iterate through each `word` in `words`:
     - If `res` is empty, append `word`.
     - Otherwise, check if `sorted(word) == sorted(res[-1])`.
       - If they are **not equal**, append `word` to `res`.
       - If they **are equal**, skip `word` (it would be deleted).
   - Return `res`.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \cdot k \log k)$, where $n$ is the number of words in `words` and $k$ is the maximum length of a word ($k \le 10$). Sorting each word of length at most 10 takes $\mathcal{O}(1)$ time in practice.
- **Space Complexity:** $\mathcal{O}(n \cdot k)$ to store the output array.
