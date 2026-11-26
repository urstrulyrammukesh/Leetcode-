# Leetcode-

My solutions to LeetCode (including 30 Hard problems) and classic DSA problems in Python. Every file runs its own tests:

```bash
python3 leetcode/lc0033_search_rotated_sorted_array.py
```

## LeetCode

| # | Problem | Technique | Time |
|---|---------|-----------|------|
| 33 | [Search in Rotated Sorted Array](leetcode/lc0033_search_rotated_sorted_array.py) | Modified binary search | O(log n) |
| 69 | [Sqrt(x)](leetcode/lc0069_sqrt_x.py) | Binary search on the answer | O(log x) |
| 209 | [Minimum Size Subarray Sum](leetcode/lc0209_minimum_size_subarray_sum.py) | Sliding window | O(n) |
| 222 | [Count Complete Tree Nodes](leetcode/lc0222_count_complete_tree_nodes.py) | Tree height comparison | O(log² n) |
| 300 | [Longest Increasing Subsequence](leetcode/lc0300_longest_increasing_subsequence.py) | Binary search + tails array | O(n log n) |

## LeetCode Hard

| # | Problem | Approach | Time |
|---|---------|----------|------|
| 4 | [Median of Two Sorted Arrays](hard/lc0004_median_of_two_sorted_arrays.py) | Binary search a partition of the shorter array so the left halves hold the smaller half of all numbers | O(log(min(m, n))) |
| 10 | [Regular Expression Matching](hard/lc0010_regular_expression_matching.py) | Bottom-up DP | O(m * n) |
| 23 | [Merge k Sorted Lists](hard/lc0023_merge_k_sorted_lists.py) | Min-heap holding the current head of every list | O(N log k) |
| 25 | [Reverse Nodes in k-Group](hard/lc0025_reverse_nodes_in_k_group.py) | Find the k-th node of each group, reverse that group in place, reconnect, move on | O(n) |
| 32 | [Longest Valid Parentheses](hard/lc0032_longest_valid_parentheses.py) | Stack of indices | O(n) |
| 37 | [Sudoku Solver](hard/lc0037_sudoku_solver.py) | Backtracking over empty cells, with sets for rows, columns and boxes so each check is O(1) | Exponential worst case |
| 41 | [First Missing Positive](hard/lc0041_first_missing_positive.py) | Cyclic sort | O(n) |
| 42 | [Trapping Rain Water](hard/lc0042_trapping_rain_water.py) | Two pointers | O(n) |
| 44 | [Wildcard Matching](hard/lc0044_wildcard_matching.py) | DP | O(m * n) |
| 51 | [N-Queens](hard/lc0051_n_queens.py) | Backtracking row by row, tracking used columns and both diagonals (r - c and r + c) | O(n!) |
| 52 | [N-Queens II](hard/lc0052_n_queens_ii.py) | Same backtracking as N-Queens, but only count the boards | O(n!) |
| 76 | [Minimum Window Substring](hard/lc0076_minimum_window_substring.py) | Sliding window with a count of characters still missing | O(|s| + |t|) |
| 84 | [Largest Rectangle in Histogram](hard/lc0084_largest_rectangle_in_histogram.py) | Monotonic increasing stack of (start index, height) | O(n) |
| 85 | [Maximal Rectangle](hard/lc0085_maximal_rectangle.py) | Treat each row as the base of a histogram of consecutive '1's above it, then reuse Largest Rectangle in Histogram | O(rows * cols) |
| 115 | [Distinct Subsequences](hard/lc0115_distinct_subsequences.py) | 1-D DP | O(|s| * |t|) |
| 124 | [Binary Tree Maximum Path Sum](hard/lc0124_binary_tree_maximum_path_sum.py) | Post-order DFS | O(n) |
| 127 | [Word Ladder](hard/lc0127_word_ladder.py) | BFS from beginWord | O(N * L * 26) |
| 135 | [Candy](hard/lc0135_candy.py) | Two passes | O(n) |
| 140 | [Word Break II](hard/lc0140_word_break_ii.py) | DFS with memoisation |  |
| 149 | [Max Points on a Line](hard/lc0149_max_points_on_a_line.py) | For each point, count the others by reduced slope (dx, dy) using gcd so no floating point is needed | O(n^2 log C) |
| 154 | [Find Minimum in Rotated Sorted Array II](hard/lc0154_find_minimum_in_rotated_sorted_array_ii.py) | Binary search against the right end | O(log n) on average |
| 188 | [Best Time to Buy and Sell Stock IV](hard/lc0188_best_time_to_buy_and_sell_stock_iv.py) | DP over transactions | O(n * k) |
| 212 | [Word Search II](hard/lc0212_word_search_ii.py) | Build a trie of the words, then DFS from every cell, walking the trie and the board together | O(rows * cols * 4^L) |
| 239 | [Sliding Window Maximum](hard/lc0239_sliding_window_maximum.py) | Monotonic deque of indices with decreasing values | O(n) |
| 295 | [Find Median from Data Stream](hard/lc0295_find_median_from_data_stream.py) | Two heaps | O(log n) per add |
| 297 | [Serialize and Deserialize Binary Tree](hard/lc0297_serialize_and_deserialize_binary_tree.py) | Pre-order traversal with '#' for empty children | O(n) |
| 312 | [Burst Balloons](hard/lc0312_burst_balloons.py) | Interval DP | O(n^3) |
| 329 | [Longest Increasing Path in a Matrix](hard/lc0329_longest_increasing_path_in_a_matrix.py) | DFS with memoisation | O(rows * cols) |
| 354 | [Russian Doll Envelopes](hard/lc0354_russian_doll_envelopes.py) | Sort by width ascending and height descending (so equal widths cannot nest), then LIS on heights | O(n log n) |
| 410 | [Split Array Largest Sum](hard/lc0410_split_array_largest_sum.py) | Binary search on the answer | O(n log(sum)) |

## Classic DSA

| # | Problem | Technique |
|---|---------|-----------|
| 1 | [Two Sum](solutions/p01_two_sum.py) | Hash map |
| 2 | [Valid Parentheses](solutions/p02_valid_parentheses.py) | Stack |
| 3 | [Reverse Linked List](solutions/p03_reverse_linked_list.py) | Pointers |
| 4 | [Maximum Subarray](solutions/p04_max_subarray.py) | Kadane's algorithm |
| 5 | [Binary Search](solutions/p05_binary_search.py) | Divide and conquer |
| 6 | [Climbing Stairs](solutions/p06_climbing_stairs.py) | Dynamic programming |
| 7 | [Group Anagrams](solutions/p07_group_anagrams.py) | Hashing sorted keys |
| 8 | [Longest Substring Without Repeating Characters](solutions/p08_longest_substring.py) | Sliding window |
| 9 | [Number of Islands](solutions/p09_number_of_islands.py) | BFS on a grid |
| 10 | [Merge Intervals](solutions/p10_merge_intervals.py) | Sorting |
