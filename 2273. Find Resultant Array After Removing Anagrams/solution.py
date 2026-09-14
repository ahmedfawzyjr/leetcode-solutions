from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Removes adjacent anagrams from the string array `words` sequentially.

        Approach:
        1. In any contiguous block of words that are anagrams of one another,
           all words except the first one will be deleted sequentially.
        2. Maintain a result list `res`.
        3. Iterate through each `word` in `words`:
           - If `res` is empty or `sorted(word) != sorted(res[-1])`, append `word` to `res`.
           - Otherwise, `word` is an anagram of the most recently retained word (`res[-1]`) and is discarded.
        4. Return `res`.

        Complexity:
        - Time Complexity: O(n * k log k), where n is the length of `words` and k is the max word length (k <= 10).
        - Space Complexity: O(n * k) for storing the resultant words.
        """
        res = []
        for word in words:
            if not res or sorted(word) != sorted(res[-1]):
                res.append(word)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: words = ["abba","baba","bbaa","cd","cd"]
    # Output: ["abba","cd"]
    assert sol.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]) == ["abba", "cd"], "Failed Example 1"

    # Example 2
    # Input: words = ["a","b","c","d","e"]
    # Output: ["a","b","c","d","e"]
    assert sol.removeAnagrams(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"], "Failed Example 2"

    # Additional Test Cases
    # Single element
    assert sol.removeAnagrams(["hello"]) == ["hello"], "Failed Single Element"

    # All anagrams
    assert sol.removeAnagrams(["abc", "bca", "cab", "acb"]) == ["abc"], "Failed All Anagrams"

    # Alternating anagrams
    assert sol.removeAnagrams(["a", "b", "a"]) == ["a", "b", "a"], "Failed Alternating"

    print("All test cases passed successfully!")
