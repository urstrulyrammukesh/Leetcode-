# Leetcode-

105 solutions in Python: LeetCode problems grouped by topic, 30 LeetCode Hard problems, and classic DSA problems. Every file runs its own tests:

```bash
python3 leetcode/lc0033_search_rotated_sorted_array.py
```

## LeetCode by topic

### Arrays & Hashing (12)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 36 | [Valid Sudoku](arrays/lc0036_valid_sudoku.py) | Medium | One pass with sets for each row, column and 3x3 box |
| 48 | [Rotate Image](arrays/lc0048_rotate_image.py) | Medium | Transpose the matrix, then reverse each row. That is a 90 degree clockwise rotation, in place |
| 54 | [Spiral Matrix](arrays/lc0054_spiral_matrix.py) | Medium | Walk the outer layer with four boundaries (top, bottom, left, right) and shrink them after each side |
| 73 | [Set Matrix Zeroes](arrays/lc0073_set_matrix_zeroes.py) | Medium | First record which rows and columns hold a zero, then clear them in a second pass |
| 128 | [Longest Consecutive Sequence](arrays/lc0128_longest_consecutive_sequence.py) | Medium | Put numbers in a set and only start counting at x when x - 1 is missing (the start of a run) |
| 169 | [Majority Element](arrays/lc0169_majority_element.py) | Easy | Boyer-Moore voting. The majority survives every pairwise cancellation |
| 189 | [Rotate Array](arrays/lc0189_rotate_array.py) | Medium | Reverse the whole array, then reverse the first k and the rest |
| 217 | [Contains Duplicate](arrays/lc0217_contains_duplicate.py) | Easy | A set drops repeats, so a duplicate exists when the set is smaller than the list |
| 238 | [Product of Array Except Self](arrays/lc0238_product_of_array_except_self.py) | Medium | Prefix products from the left, then multiply by suffix products from the right, no division |
| 242 | [Valid Anagram](arrays/lc0242_valid_anagram.py) | Easy | Two strings are anagrams when every character appears the same number of times |
| 347 | [Top K Frequent Elements](arrays/lc0347_top_k_frequent_elements.py) | Medium | Bucket sort by frequency |
| 448 | [Find All Numbers Disappeared in an Array](arrays/lc0448_find_all_numbers_disappeared_in_an_array.py) | Easy | For every value v, mark index v-1 by making it negative |

### Two Pointers (6)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 11 | [Container With Most Water](two_pointers/lc0011_container_with_most_water.py) | Medium | Two pointers at both ends |
| 15 | [3Sum](two_pointers/lc0015_3sum.py) | Medium | Sort, fix one number, then two pointers on the rest |
| 75 | [Sort Colors](two_pointers/lc0075_sort_colors.py) | Medium | Dutch national flag. Three pointers keep 0s on the left, 2s on the right, 1s in the middle |
| 125 | [Valid Palindrome](two_pointers/lc0125_valid_palindrome.py) | Easy | Two pointers from both ends, skipping anything that is not a letter or digit |
| 167 | [Two Sum II - Input Array Is Sorted](two_pointers/lc0167_two_sum_ii_input_array_is_sorted.py) | Medium | Two pointers. If the sum is too small move left up, if too big move right down |
| 283 | [Move Zeroes](two_pointers/lc0283_move_zeroes.py) | Easy | A write pointer swaps every non-zero forward, so zeros drift to the end in place |

### Sliding Window (4)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 121 | [Best Time to Buy and Sell Stock](sliding_window/lc0121_best_time_to_buy_and_sell_stock.py) | Easy | Keep the lowest price seen so far |
| 424 | [Longest Repeating Character Replacement](sliding_window/lc0424_longest_repeating_character_replacement.py) | Medium | Sliding window. A window is fine while (length - count of its most common letter) <= k |
| 438 | [Find All Anagrams in a String](sliding_window/lc0438_find_all_anagrams_in_a_string.py) | Medium | Fixed-size sliding window of letter counts |
| 567 | [Permutation in String](sliding_window/lc0567_permutation_in_string.py) | Medium | Slide a window of len(s1) over s2 and compare letter counts |

### Stack (5)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 22 | [Generate Parentheses](stack/lc0022_generate_parentheses.py) | Medium | Backtracking. Add '(' while some are left, and ')' only when it would not close more than opened |
| 150 | [Evaluate Reverse Polish Notation](stack/lc0150_evaluate_reverse_polish_notation.py) | Medium | Push numbers on a stack |
| 155 | [Min Stack](stack/lc0155_min_stack.py) | Medium | Store (value, minimum so far) pairs so getMin is the top pair's second item |
| 739 | [Daily Temperatures](stack/lc0739_daily_temperatures.py) | Medium | Monotonic decreasing stack of indices |
| 853 | [Car Fleet](stack/lc0853_car_fleet.py) | Medium | Go from the car nearest the target backwards |

### Binary Search (5)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 34 | [Find First and Last Position of Element in Sorted Array](binary_search/lc0034_find_first_and_last_position_of_element_in_sorted_array.py) | Medium | Two binary searches: the first index >= target, and the first index > target |
| 74 | [Search a 2D Matrix](binary_search/lc0074_search_a_2d_matrix.py) | Medium | The rows join into one sorted list, so binary search index i as cell (i // cols, i % cols) |
| 153 | [Find Minimum in Rotated Sorted Array](binary_search/lc0153_find_minimum_in_rotated_sorted_array.py) | Medium | Binary search against the right end |
| 875 | [Koko Eating Bananas](binary_search/lc0875_koko_eating_bananas.py) | Medium | Binary search on the eating speed k |
| 981 | [Time Based Key-Value Store](binary_search/lc0981_time_based_key_value_store.py) | Medium | Per key, keep timestamps (always increasing) and values in lists |

### Linked List (6)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 2 | [Add Two Numbers](linked_list/lc0002_add_two_numbers.py) | Medium | Add digit by digit like on paper, carrying into the next node |
| 19 | [Remove Nth Node From End of List](linked_list/lc0019_remove_nth_node_from_end_of_list.py) | Medium | Move a fast pointer n steps ahead, then move both |
| 21 | [Merge Two Sorted Lists](linked_list/lc0021_merge_two_sorted_lists.py) | Easy | Walk both lists with a dummy head, always attaching the smaller node |
| 141 | [Linked List Cycle](linked_list/lc0141_linked_list_cycle.py) | Easy | Floyd's tortoise and hare. A fast pointer catches the slow one only if there is a loop |
| 143 | [Reorder List](linked_list/lc0143_reorder_list.py) | Medium | Find the middle, reverse the second half, then weave the two halves together |
| 146 | [LRU Cache](linked_list/lc0146_lru_cache.py) | Medium | An OrderedDict keeps keys in use order |

### Trees (12)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 98 | [Validate Binary Search Tree](trees/lc0098_validate_binary_search_tree.py) | Medium | Pass down the allowed (low, high) range |
| 100 | [Same Tree](trees/lc0100_same_tree.py) | Easy | Two trees match if the roots match and both pairs of subtrees match |
| 102 | [Binary Tree Level Order Traversal](trees/lc0102_binary_tree_level_order_traversal.py) | Medium | BFS with a queue, handling one whole level per loop |
| 104 | [Maximum Depth of Binary Tree](trees/lc0104_maximum_depth_of_binary_tree.py) | Easy | Depth of a node is 1 + the deeper of its two subtrees |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](trees/lc0105_construct_binary_tree_from_preorder_and_inorder_traversal.py) | Medium | The next preorder value is the root |
| 110 | [Balanced Binary Tree](trees/lc0110_balanced_binary_tree.py) | Easy | DFS returns the height, or -1 as soon as any subtree is unbalanced |
| 199 | [Binary Tree Right Side View](trees/lc0199_binary_tree_right_side_view.py) | Medium | BFS level by level and keep the last node of each level |
| 226 | [Invert Binary Tree](trees/lc0226_invert_binary_tree.py) | Easy | Swap the left and right child of every node, recursively |
| 230 | [Kth Smallest Element in a BST](trees/lc0230_kth_smallest_element_in_a_bst.py) | Medium | In-order traversal of a BST visits values in sorted order |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](trees/lc0235_lowest_common_ancestor_of_a_binary_search_tree.py) | Medium | Walk down from the root |
| 543 | [Diameter of Binary Tree](trees/lc0543_diameter_of_binary_tree.py) | Easy | DFS returns each height |
| 572 | [Subtree of Another Tree](trees/lc0572_subtree_of_another_tree.py) | Easy | At every node of root, check whether the tree starting there is the same as subRoot |

### Graphs (5)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 133 | [Clone Graph](graphs/lc0133_clone_graph.py) | Medium | DFS with a map from each original node to its copy, so cycles are copied once |
| 207 | [Course Schedule](graphs/lc0207_course_schedule.py) | Medium | Kahn's topological sort. If every course can be taken once its prerequisites are done, there is no cycle |
| 210 | [Course Schedule II](graphs/lc0210_course_schedule_ii.py) | Medium | Kahn's topological sort, recording the order courses are taken |
| 695 | [Max Area of Island](graphs/lc0695_max_area_of_island.py) | Medium | DFS from every unvisited land cell, counting cells and sinking them so they are not counted twice |
| 994 | [Rotting Oranges](graphs/lc0994_rotting_oranges.py) | Medium | Multi-source BFS starting from every rotten orange at once |

### Dynamic Programming (5)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 62 | [Unique Paths](dp/lc0062_unique_paths.py) | Medium | DP row by row. Paths to a cell = paths from above + paths from the left |
| 198 | [House Robber](dp/lc0198_house_robber.py) | Medium | DP. At each house, either skip it or rob it plus the best from two houses back |
| 213 | [House Robber II](dp/lc0213_house_robber_ii.py) | Medium | Houses form a circle, so the first and last cannot both be robbed: solve House Robber without the |
| 322 | [Coin Change](dp/lc0322_coin_change.py) | Medium | Bottom-up DP. dp[a] is the fewest coins for amount a, trying each coin as the last one |
| 1143 | [Longest Common Subsequence](dp/lc1143_longest_common_subsequence.py) | Medium | 2-D DP. Matching characters extend the diagonal |

## More LeetCode

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
