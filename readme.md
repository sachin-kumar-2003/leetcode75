
# LeetCode 75 - Complete Solutions Collection

A comprehensive collection of solutions for the **LeetCode 75** study plan, covering fundamental algorithms and data structures essential for technical interviews.


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
├── 01-25/           # Easy problems
├── 26-50/           # Medium problems  
├── 51-75/           # Hard problems
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- No external dependencies required

### Running Solutions
```bash
# Clone the repository
git clone https://github.com/sachin-kumar-2003/leetcode75.git
cd leetcode75
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
| 31 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [31_reverseList.py](31_reverseList.py) | Linked List |
| 32 | [Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) | [32_pairSum.py](32_pairSum.py) | Linked List |
| 33 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [33_maxDepth.py](33_maxDepth.py) | Binary Tree |
| 34 | [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | [34_leafSimilar.py](34_leafSimilar.py) | Binary Tree |
| 35 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [35_goodNodes.py](35_goodNodes.py) | Binary Tree |
| 36 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | [36_pathSum.py](36_pathSum.py) | Binary Tree |
| 37 | [Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | [37_longestZigZag.py](37_longestZigZag.py) | Binary Tree |
| 38 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [38_lowestCommonAncestor.py](38_lowestCommonAncestor.py) | Binary Tree |
| 39 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | [39_rightSideView.py](39_rightSideView.py) | Binary Tree |
| 40 | [Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | [40_maxLevelSum.py](40_maxLevelSum.py) | Binary Tree |
| 41 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | [41_searchBST.py](41_searchBST.py) | Binary Search Tree |
| 42 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | [42_deleteNode.py](42_deleteNode.py) | Binary Search Tree |
| 43 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | [43_canVisitAllRooms.py](43_canVisitAllRooms.py) | Graph |
| 44 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | [44_findCircleNum.py](44_findCircleNum.py) | Graph |
| 45 | [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [45_minReorder.py](45_minReorder.py) | Graph |
| 46 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | [46_calcEquation.py](46_calcEquation.py) | Graph |
| 47 | [Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) | [47_nearestExit.py](47_nearestExit.py) | Graph |
| 48 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [48_orangesRotting.py](48_orangesRotting.py) | Graph |
| 49 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [49_findKthLargest.py](49_findKthLargest.py) | Heap |
| 50 | [Smallest Infinite Set](https://leetcode.com/problems/smallest-infinite-set/) | [50_SmallestInfiniteSet.py](50_SmallestInfiniteSet.py) | Heap |
| 51 | [Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) | [51_maxScore.py](51_maxScore.py) | Greedy |
| 52 | [Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/) | [52_totalCost.py](52_totalCost.py) | Heap |
| 53 | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | [53_guessNumber.py](53_guessNumber.py) | Binary Search |
| 54 | [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/) | [54_successfulPairs.py](54_successfulPairs.py) | Binary Search |
| 55 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | [55_findPeakElement.py](55_findPeakElement.py) | Binary Search |
| 56 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [56_minEatingSpeed.py](56_minEatingSpeed.py) | Binary Search |
| 57 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [57_letterCombinations.py](57_letterCombinations.py) | Backtracking |
| 58 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | [58_combinationSum3.py](58_combinationSum3.py) | Backtracking |
| 59 | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | [59_tribonacci.py](59_tribonacci.py) | Dynamic Programming |
| 60 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [60_minCostClimbingStairs.py](60_minCostClimbingStairs.py) | Dynamic Programming |
| 61 | [House Robber](https://leetcode.com/problems/house-robber/) | [61_rob.py](61_rob.py) | Dynamic Programming |
| 62 | [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) | [62_numTilings.py](62_numTilings.py) | Dynamic Programming |
| 63 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | [63_uniquePaths.py](63_uniquePaths.py) | Dynamic Programming |
| 64 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | [64_longestCommonSubsequence.py](64_longestCommonSubsequence.py) | Dynamic Programming |
| 65 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [65_maxProfit.py](65_maxProfit.py) | Dynamic Programming |
| 66 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | [66_minDistance.py](66_minDistance.py) | Dynamic Programming |
| 67 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | [67_countBits.py](67_countBits.py) | Bit Manipulation |
| 68 | [Single Number](https://leetcode.com/problems/single-number/) | [68_singleNumber.py](68_singleNumber.py) | Bit Manipulation |
| 69 | [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) | [69_minFlips.py](69_minFlips.py) | Bit Manipulation |
| 70 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | [70_Trie.py](70_Trie.py) | Trie |
| 71 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | [71_suggestedProducts.py](71_suggestedProducts.py) | Trie |
| 72 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [72_eraseOverlapIntervals.py](72_eraseOverlapIntervals.py) | Intervals |
| 73 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [73_findMinArrowShots.py](73_findMinArrowShots.py) | Intervals |
| 74 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | [74_dailyTemperatures.py](74_dailyTemperatures.py) | Stack |
| 75 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | [75_StockSpanner.py](75_StockSpanner.py) | Stack |



## 🎯 Problem-Solving Patterns

### Array/String Patterns
- **Two Pointers**: Use two indices moving towards/away from each other
- **Sliding Window**: Maintain a window of elements with left/right pointers
- **Prefix Sum**: Pre-calculate cumulative sums for range queries

### Tree Patterns
- **DFS**: Depth-first traversal (preorder, inorder, postorder)
- **BFS**: Level-order traversal using queue
- **Recursion**: Natural fit for tree problems

### Dynamic Programming Patterns
- **1D DP**: Single dimension state
- **2D DP**: Two dimensions state (strings, grids)
- **State transitions**: Build solution from smaller subproblems



## 🚀 Performance Optimization Tips

### Time Optimization
- **Avoid nested loops** when possible
- **Use hash maps** for O(1) lookups
- **Pre-calculate** values that are used multiple times

### Space Optimization
- **In-place modifications** to reduce extra space
- **Re-use data structures** instead of creating new ones
- **Bit manipulation** for compact storage

## 📚 Learning Path

### Beginner Path (Problems 1-25)
Start with easy problems to build fundamentals:
1. Array manipulation techniques
2. Two pointer patterns
3. Basic data structures (stack, queue)

### Intermediate Path (Problems 26-50)
Progress to medium problems:
1. Linked list operations
2. Tree traversals and operations
3. Graph algorithms (DFS, BFS)

### Advanced Path (Problems 51-75)
Master complex algorithms:
1. Dynamic programming patterns
2. Backtracking techniques
3. Advanced data structures (trie, heap)
