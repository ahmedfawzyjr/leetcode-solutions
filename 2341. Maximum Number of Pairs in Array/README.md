# 2341. Maximum Number of Pairs in Array

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Counting  

## Problem Description

You are given a **0-indexed** integer array `nums`. In one operation, you may do the following:

- Choose **two** integers in `nums` that are **equal**.
- Remove both integers from `nums`, forming a **pair**.

The operation is done on `nums` as many times as possible.

Return *a **0-indexed** integer array* `answer` *of size* `2` *where* `answer[0]` *is the number of pairs that are formed and* `answer[1]` *is the number of leftover integers in* `nums` *after doing the operation as many times as possible*.

---

### Example 1:

**Input:** `nums = [1,3,2,1,3,2,2]`  
**Output:** `[3,1]`  
**Explanation:**  
- Form a pair with `nums[0]` and `nums[3]` and remove them from `nums`. Now, `nums = [3,2,3,2,2]`.  
- Form a pair with `nums[0]` and `nums[2]` and remove them from `nums`. Now, `nums = [2,2,2]`.  
- Form a pair with `nums[0]` and `nums[1]` and remove them from `nums`. Now, `nums = [2]`.  
No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in `nums`.

### Example 2:

**Input:** `nums = [1,1]`  
**Output:** `[1,0]`  
**Explanation:** Form a pair with `nums[0]` and `nums[1]` and remove them from `nums`. Now, `nums = []`.  
No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in `nums`.

### Example 3:

**Input:** `nums = [0]`  
**Output:** `[0,1]`  
**Explanation:** No pairs can be formed, and there is 1 number leftover in `nums`.

---

### Constraints:

- $1 \le \text{nums.length} \le 100$
- $0 \le \text{nums}[i] \le 100$

---

## Solution Approach

### Frequency Counting (Hash Map)

1. **Count Frequencies:**
   - Use a hash map or `Counter` to determine the frequency of each unique number in `nums`.

2. **Form Pairs and Collect Leftovers:**
   - For each unique element with frequency $c$:
     - The number of disjoint pairs formed is $\lfloor c / 2 \rfloor$ (integer division `c // 2`).
     - The number of leftover elements is $c \pmod 2$ (`c % 2`).

3. **Aggregate:**
   - Sum up the pairs and leftovers across all unique numbers and return `[total_pairs, total_leftovers]`.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of elements in `nums`. Counting frequencies takes $\mathcal{O}(n)$ time, and iterating over the unique keys takes at most $\mathcal{O}(n)$ time.
- **Space Complexity:** $\mathcal{O}(u)$ auxiliary space, where $u$ is the number of distinct elements in `nums` ($u \le \min(n, 101)$).
