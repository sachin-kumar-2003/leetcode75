# LeetCode 75 - Complete Solutions Collection

A comprehensive collection of solutions for the **LeetCode 75** study plan, covering fundamental algorithms and data structures essential for technical interviews.

## 📋 Table of Contents
- [Overview](#overview)
- [Problem Categories](#problem-categories)
- [Solutions Structure](#solutions-structure)
- [Getting Started](#getting-started)
- [Problem List](#problem-list)
- [Time & Space Complexity](#time--space-complexity)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains **75 carefully selected LeetCode problems** that cover the most important concepts in algorithms and data structures. 

## 📊 Problem Categories

| Category | Count | Problems |
|----------|-------|----------|
| **Array/String** | 20 | Two pointers, sliding window, prefix sum |
| **Two Pointers** | 8 | Array manipulation, collision detection |
| **Sliding Window** | 7 | Fixed/variable window techniques |
| **Stack** | 5 | Monotonic stack, parentheses matching |
| **Binary Tree** | 12 | DFS, BFS, tree traversals |
| **Binary Search Tree** | 3 | Search, insertion, deletion |
| **Graph** | 5 | DFS, BFS, shortest path |
| **Heap/Priority Queue** | 3 | K-largest elements, scheduling |
| **Backtracking** | 3 | Combinations, permutations |
| **Dynamic Programming** | 12 | 1D/2D DP, state transitions |
| **Greedy** | 3 | Optimal choices at each step |
| **Bit Manipulation** | 3 | XOR, bit masking |
| **Trie** | 2 | Prefix matching, autocomplete |
| **Intervals** | 2 | Merging, scheduling |

## 🗂️ Solutions Structure

```
leetcode75/
├── 01-10/           # Array/String problems
├── 11-20/           # Two pointers & sliding window
├── 21-30/           # Linked lists
├── 31-40/           # Trees & BST
├── 41-50/           # Graphs & heaps
├── 51-60/           # Backtracking & DP
├── 61-75/           # Advanced topics
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- No external dependencies required

### Running Solutions
```bash
# Clone the repository
git clone https://github.com/yourusername/leetcode75.git
cd leetcode75

# Run any solution
python 01_mergeAlternately.py
```

### Testing
Each solution includes test cases that can be run directly:
```python
# Example for testing mergeAlternately
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
```

## 📋 Problem List

### 🟢 Easy Problems (25)
| # | Problem | Solution | Topics |
|---|---------|----------|--------|
| 1 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | [01_mergeAlternately.py](01_mergeAlternately.py) | Two Pointers |
| 2 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | [02_gcdOfStrings.py](02_gcdOfStrings.py) | Math |
| 3 | [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | [03_kidsWithCandies.py](03_kidsWithCandies.py) | Array |
| 4 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | [04_canPlaceFlowers.py](04_canPlaceFlowers.py) | Greedy |
| 5 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | [05_reverseWords.py](05_reverseWords.py) | Two Pointers |
| 6 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | [06_reverseVowels.py](06_reverseVowels.py) | Two Pointers |
| 7 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [07_productExceptSelf.py](07_productExceptSelf.py) | Array |
| 8 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | [08_increasingTriplet.py](08_increasingTriplet.py) | Greedy |
| 9 | [String Compression](https://leetcode.com/problems/string-compression/) | [09_compress.py](09_compress.py) | Two Pointers |
| 10 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [10_moveZeroes.py](10_moveZeroes.py) | Array |
| 11 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | [11_isSubsequence.py](11_isSubsequence.py) | Two Pointers |
| 12 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [12_maxArea.py](12_maxArea.py) | Two Pointers |
| 13 | [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | [13_maxOperations.py](13_maxOperations.py) | Hash Table |
| 14 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [14_findMaxAverage.py](14_findMaxAverage.py) | Sliding Window |
| 15 | [Maximum Number of Vowels in a Substring](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | [15_maxVowels.py](15_maxVowels.py) | Sliding Window |
| 16 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | [16_longestOnes.py](16_longestOnes.py) | Sliding Window |
| 17 | [Longest Subarray With Maximum Bitwise AND](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) | [17_longestSubarray.py](17_longestSubarray.py) | Bit Manipulation |
| 18 | [Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/) | [18_largestAltitude.py](18_largestAltitude.py) | Prefix Sum |
| 19 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | [19_pivotIndex.py](19_pivotIndex.py) | Prefix Sum |
| 20 | [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | [20_findDifference.py](20_findDifference.py) | Hash Table |
| 21 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | [21_uniqueOccurrences.py](21_uniqueOccurrences.py) | Hash Table |
| 22 | [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/) | [22_closeStrings.py](22_closeStrings.py) | Hash Table |
| 23 | [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) | [23_equalPairs.py](23_equalPairs.py) | Hash Table |
| 24 | [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/) | [24_removeStars.py](24_removeStars.py) | Stack |
| 25 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | [25_asteroidCollision.py](25_asteroidCollision.py) | Stack |

### 🟡 Medium Problems (35)
| # | Problem | Solution | Topics |
|---|---------|----------|--------|
| 26 | [Decode String](https://leetcode.com/problems/decode-string/) | [26_decodeString.py](26_decodeString.py) | Stack |
| 27 | [Recent Counter](https://leetcode.com/problems/recent-counter/) | [27_RecentCounter.py](27_RecentCounter.py) | Queue |
| 28 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | [28_predictPartyVictory.py](28_predictPartyVictory.py) | DP |
| 29 | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) | [29_deleteMiddle.py](29_deleteMiddle.py) | Linked List |
| 30 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | [30_oddEvenList.py](30_oddEvenList.py) | Linked List |
| 31 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [31The current readme.md file is empty. I will now search the codebase for any documentation or comments that describe the LeetCode 75 project to help me generate a comprehensive README file.
