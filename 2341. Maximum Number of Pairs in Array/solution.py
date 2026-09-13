from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """
        Calculates the maximum number of pairs formed and the number of leftover integers.

        Approach:
        1. Count the occurrences of each number in `nums` using a frequency map / hash map (Counter).
        2. For each unique number with frequency `count`:
           - The number of pairs that can be formed is `count // 2`.
           - The leftover element (if any) is `count % 2`.
        3. Sum up the formed pairs and leftover elements.
        4. Return [pairs, leftovers].

        Complexity:
        - Time Complexity: O(n), where n is the length of `nums`.
        - Space Complexity: O(n) or O(u) auxiliary space, where u is the number of distinct elements (u <= min(n, 101)).
        """
        counts = Counter(nums)
        pairs = sum(count // 2 for count in counts.values())
        leftovers = sum(count % 2 for count in counts.values())
        return [pairs, leftovers]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: nums = [1,3,2,1,3,2,2]
    # Output: [3,1]
    assert sol.numberOfPairs([1, 3, 2, 1, 3, 2, 2]) == [3, 1], "Failed Example 1"

    # Example 2
    # Input: nums = [1,1]
    # Output: [1,0]
    assert sol.numberOfPairs([1, 1]) == [1, 0], "Failed Example 2"

    # Example 3
    # Input: nums = [0]
    # Output: [0,1]
    assert sol.numberOfPairs([0]) == [0, 1], "Failed Example 3"

    # Additional Test Cases
    assert sol.numberOfPairs([1, 1, 1, 1]) == [2, 0]
    assert sol.numberOfPairs([1, 2, 3, 4, 5]) == [0, 5]
    assert sol.numberOfPairs([100, 100, 100]) == [1, 1]

    print("All test cases passed successfully!")
