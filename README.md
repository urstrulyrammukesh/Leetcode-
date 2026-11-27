# Leetcode-

[![Run all solutions](https://github.com/urstrulyrammukesh/Leetcode-/actions/workflows/tests.yml/badge.svg)](https://github.com/urstrulyrammukesh/Leetcode-/actions/workflows/tests.yml)

233 solutions in Python: LeetCode problems grouped by topic, 30 LeetCode Hard problems, and classic DSA problems. Every file runs its own tests:

```bash
python3 leetcode/lc0033_search_rotated_sorted_array.py
```

## How I use this repo

Each file has the approach and its time/space cost at the top, and tests at the bottom; GitHub runs every file on each push (badge above).
Many of the newer solutions were written together with an AI pair programmer as worked examples. I read the approach, run it, and then re-solve the problem myself on LeetCode without looking.

## LeetCode by topic

188 problems in 14 topics.

### Arrays & Hashing (28)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 1 | [Two Sum](arrays/lc0001_two_sum.py) | Easy | One pass with a hash map from value to index; look up target - x before storing x |
| 14 | [Longest Common Prefix](arrays/lc0014_longest_common_prefix.py) | Easy | Sort the words; the common prefix of the whole list is the common prefix of the first and last word |
| 26 | [Remove Duplicates from Sorted Array](arrays/lc0026_remove_duplicates_from_sorted_array.py) | Easy | A write pointer keeps the next free slot; copy each value that differs from the last kept one |
| 27 | [Remove Element](arrays/lc0027_remove_element.py) | Easy | Write pointer: copy every value that is not val to the front |
| 36 | [Valid Sudoku](arrays/lc0036_valid_sudoku.py) | Medium | One pass with sets for each row, column and 3x3 box |
| 48 | [Rotate Image](arrays/lc0048_rotate_image.py) | Medium | Transpose the matrix, then reverse each row. That is a 90 degree clockwise rotation, in place |
| 49 | [Group Anagrams](arrays/lc0049_group_anagrams.py) | Medium | Words that are anagrams share the same sorted letters; group by that key |
| 54 | [Spiral Matrix](arrays/lc0054_spiral_matrix.py) | Medium | Walk the outer layer with four boundaries (top, bottom, left, right) and shrink them after each side |
| 56 | [Merge Intervals](arrays/lc0056_merge_intervals.py) | Medium | Sort by start; extend the last merged interval while the next one overlaps it |
| 57 | [Insert Interval](arrays/lc0057_insert_interval.py) | Medium | Copy intervals that end before the new one, merge every overlapping one into it, then copy the rest |
| 73 | [Set Matrix Zeroes](arrays/lc0073_set_matrix_zeroes.py) | Medium | First record which rows and columns hold a zero, then clear them in a second pass |
| 88 | [Merge Sorted Array](arrays/lc0088_merge_sorted_array.py) | Easy | Fill nums1 from the back with the larger of the two tails, so nothing is overwritten |
| 118 | [Pascal's Triangle](arrays/lc0118_pascals_triangle.py) | Easy | Each row starts and ends with 1; every inner value is the sum of the two values above it |
| 128 | [Longest Consecutive Sequence](arrays/lc0128_longest_consecutive_sequence.py) | Medium | Put numbers in a set and only start counting at x when x - 1 is missing (the start of a run) |
| 136 | [Single Number](arrays/lc0136_single_number.py) | Easy | XOR of all numbers: pairs cancel out (x ^ x = 0), only the single one is left |
| 169 | [Majority Element](arrays/lc0169_majority_element.py) | Easy | Boyer-Moore voting. The majority survives every pairwise cancellation |
| 189 | [Rotate Array](arrays/lc0189_rotate_array.py) | Medium | Reverse the whole array, then reverse the first k and the rest |
| 205 | [Isomorphic Strings](arrays/lc0205_isomorphic_strings.py) | Easy | Map characters both ways; a clash in either map means the strings are not isomorphic |
| 217 | [Contains Duplicate](arrays/lc0217_contains_duplicate.py) | Easy | A set drops repeats, so a duplicate exists when the set is smaller than the list |
| 238 | [Product of Array Except Self](arrays/lc0238_product_of_array_except_self.py) | Medium | Prefix products from the left, then multiply by suffix products from the right, no division |
| 242 | [Valid Anagram](arrays/lc0242_valid_anagram.py) | Easy | Two strings are anagrams when every character appears the same number of times |
| 290 | [Word Pattern](arrays/lc0290_word_pattern.py) | Easy | Same idea as isomorphic strings, with letters on one side and words on the other |
| 347 | [Top K Frequent Elements](arrays/lc0347_top_k_frequent_elements.py) | Medium | Bucket sort by frequency |
| 380 | [Insert Delete GetRandom O(1)](arrays/lc0380_insert_delete_getrandom_o_1.py) | Medium | A list for random picks plus a map value -> index; delete by swapping with the last element |
| 435 | [Non-overlapping Intervals](arrays/lc0435_non_overlapping_intervals.py) | Medium | Greedy: sort by end and keep every interval that starts after the last kept end; the rest must go |
| 448 | [Find All Numbers Disappeared in an Array](arrays/lc0448_find_all_numbers_disappeared_in_an_array.py) | Easy | For every value v, mark index v-1 by making it negative |
| 560 | [Subarray Sum Equals K](arrays/lc0560_subarray_sum_equals_k.py) | Medium | Count prefix sums seen so far; a subarray ending here sums to k when prefix - k was seen before |
| 605 | [Can Place Flowers](arrays/lc0605_can_place_flowers.py) | Easy | Walk the bed and plant greedily wherever the spot and both neighbours are empty |

### Two Pointers (12)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 11 | [Container With Most Water](two_pointers/lc0011_container_with_most_water.py) | Medium | Two pointers at both ends |
| 15 | [3Sum](two_pointers/lc0015_3sum.py) | Medium | Sort, fix one number, then two pointers on the rest |
| 18 | [4Sum](two_pointers/lc0018_4sum.py) | Medium | Sort, fix two numbers with two loops, then two pointers on the rest, skipping duplicates |
| 75 | [Sort Colors](two_pointers/lc0075_sort_colors.py) | Medium | Dutch national flag. Three pointers keep 0s on the left, 2s on the right, 1s in the middle |
| 80 | [Remove Duplicates from Sorted Array II](two_pointers/lc0080_remove_duplicates_from_sorted_array_ii.py) | Medium | Write pointer: keep x unless it equals the value two slots back (that would make three) |
| 125 | [Valid Palindrome](two_pointers/lc0125_valid_palindrome.py) | Easy | Two pointers from both ends, skipping anything that is not a letter or digit |
| 167 | [Two Sum II - Input Array Is Sorted](two_pointers/lc0167_two_sum_ii_input_array_is_sorted.py) | Medium | Two pointers. If the sum is too small move left up, if too big move right down |
| 283 | [Move Zeroes](two_pointers/lc0283_move_zeroes.py) | Easy | A write pointer swaps every non-zero forward, so zeros drift to the end in place |
| 344 | [Reverse String](two_pointers/lc0344_reverse_string.py) | Easy | Swap the two ends and move both pointers inward |
| 392 | [Is Subsequence](two_pointers/lc0392_is_subsequence.py) | Easy | Walk t once and advance a pointer in s on every match |
| 680 | [Valid Palindrome II](two_pointers/lc0680_valid_palindrome_ii.py) | Easy | Two pointers; on the first mismatch try skipping either the left or the right character |
| 977 | [Squares of a Sorted Array](two_pointers/lc0977_squares_of_a_sorted_array.py) | Easy | The biggest square is at one of the two ends; fill the answer from the back |

### Sliding Window (8)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 3 | [Longest Substring Without Repeating Characters](sliding_window/lc0003_longest_substring_without_repeating_characters.py) | Medium | Keep the last index of each character; when a repeat appears inside the window, move the left edge past it |
| 121 | [Best Time to Buy and Sell Stock](sliding_window/lc0121_best_time_to_buy_and_sell_stock.py) | Easy | Keep the lowest price seen so far |
| 424 | [Longest Repeating Character Replacement](sliding_window/lc0424_longest_repeating_character_replacement.py) | Medium | Sliding window. A window is fine while (length - count of its most common letter) <= k |
| 438 | [Find All Anagrams in a String](sliding_window/lc0438_find_all_anagrams_in_a_string.py) | Medium | Fixed-size sliding window of letter counts |
| 567 | [Permutation in String](sliding_window/lc0567_permutation_in_string.py) | Medium | Slide a window of len(s1) over s2 and compare letter counts |
| 643 | [Maximum Average Subarray I](sliding_window/lc0643_maximum_average_subarray_i.py) | Easy | Fixed window of size k: add the new number, drop the one leaving |
| 904 | [Fruit Into Baskets](sliding_window/lc0904_fruit_into_baskets.py) | Medium | Longest window with at most two distinct values: shrink from the left when a third type appears |
| 1004 | [Max Consecutive Ones III](sliding_window/lc1004_max_consecutive_ones_iii.py) | Medium | Longest window with at most k zeros: move the left edge whenever there are too many zeros |

### Stack (11)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 20 | [Valid Parentheses](stack/lc0020_valid_parentheses.py) | Easy | Push opening brackets; every closing bracket must match the top of the stack |
| 22 | [Generate Parentheses](stack/lc0022_generate_parentheses.py) | Medium | Backtracking. Add '(' while some are left, and ')' only when it would not close more than opened |
| 71 | [Simplify Path](stack/lc0071_simplify_path.py) | Medium | Split on '/', push folder names, pop on '..', ignore '.' and empty parts |
| 150 | [Evaluate Reverse Polish Notation](stack/lc0150_evaluate_reverse_polish_notation.py) | Medium | Push numbers on a stack |
| 155 | [Min Stack](stack/lc0155_min_stack.py) | Medium | Store (value, minimum so far) pairs so getMin is the top pair's second item |
| 232 | [Implement Queue using Stacks](stack/lc0232_implement_queue_using_stacks.py) | Easy | Push onto an in-stack; when popping, refill the out-stack only when it is empty (amortised O(1)) |
| 394 | [Decode String](stack/lc0394_decode_string.py) | Medium | On '[' push the current text and repeat count; on ']' pop and repeat the inner text |
| 496 | [Next Greater Element I](stack/lc0496_next_greater_element_i.py) | Easy | Monotonic decreasing stack over nums2 gives every number's next greater element in one pass |
| 735 | [Asteroid Collision](stack/lc0735_asteroid_collision.py) | Medium | Stack of survivors; a left-moving asteroid destroys smaller right-movers on top of the stack |
| 739 | [Daily Temperatures](stack/lc0739_daily_temperatures.py) | Medium | Monotonic decreasing stack of indices |
| 853 | [Car Fleet](stack/lc0853_car_fleet.py) | Medium | Go from the car nearest the target backwards |

### Binary Search (12)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 34 | [Find First and Last Position of Element in Sorted Array](binary_search/lc0034_find_first_and_last_position_of_element_in_sorted_array.py) | Medium | Two binary searches: the first index >= target, and the first index > target |
| 35 | [Search Insert Position](binary_search/lc0035_search_insert_position.py) | Easy | Lower-bound binary search: the first index whose value is >= target |
| 74 | [Search a 2D Matrix](binary_search/lc0074_search_a_2d_matrix.py) | Medium | The rows join into one sorted list, so binary search index i as cell (i // cols, i % cols) |
| 153 | [Find Minimum in Rotated Sorted Array](binary_search/lc0153_find_minimum_in_rotated_sorted_array.py) | Medium | Binary search against the right end |
| 162 | [Find Peak Element](binary_search/lc0162_find_peak_element.py) | Medium | If nums[mid] < nums[mid + 1] a peak lies to the right, otherwise at mid or to the left |
| 278 | [First Bad Version](binary_search/lc0278_first_bad_version.py) | Easy | Binary search for the first version where isBadVersion is true |
| 367 | [Valid Perfect Square](binary_search/lc0367_valid_perfect_square.py) | Easy | Binary search for an integer r with r * r == num, without using sqrt |
| 704 | [Binary Search](binary_search/lc0704_binary_search.py) | Easy | Classic binary search on a closed range [lo, hi] |
| 852 | [Peak Index in a Mountain Array](binary_search/lc0852_peak_index_in_a_mountain_array.py) | Medium | Climb toward the bigger neighbour: if arr[mid] < arr[mid + 1] the peak is to the right |
| 875 | [Koko Eating Bananas](binary_search/lc0875_koko_eating_bananas.py) | Medium | Binary search on the eating speed k |
| 981 | [Time Based Key-Value Store](binary_search/lc0981_time_based_key_value_store.py) | Medium | Per key, keep timestamps (always increasing) and values in lists |
| 1011 | [Capacity To Ship Packages Within D Days](binary_search/lc1011_capacity_to_ship_packages_within_d_days.py) | Medium | Binary search on the answer: the smallest capacity whose greedy loading needs at most `days` days |

### Linked List (18)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 2 | [Add Two Numbers](linked_list/lc0002_add_two_numbers.py) | Medium | Add digit by digit like on paper, carrying into the next node |
| 19 | [Remove Nth Node From End of List](linked_list/lc0019_remove_nth_node_from_end_of_list.py) | Medium | Move a fast pointer n steps ahead, then move both |
| 21 | [Merge Two Sorted Lists](linked_list/lc0021_merge_two_sorted_lists.py) | Easy | Walk both lists with a dummy head, always attaching the smaller node |
| 24 | [Swap Nodes in Pairs](linked_list/lc0024_swap_nodes_in_pairs.py) | Medium | Use a dummy head and rewire each pair: prev -> b -> a -> rest |
| 61 | [Rotate List](linked_list/lc0061_rotate_list.py) | Medium | Make the list a ring, then cut it len - k % len steps from the old head |
| 82 | [Remove Duplicates from Sorted List II](linked_list/lc0082_remove_duplicates_from_sorted_list_ii.py) | Medium | Dummy head; when a run of equal values starts, skip the whole run |
| 83 | [Remove Duplicates from Sorted List](linked_list/lc0083_remove_duplicates_from_sorted_list.py) | Easy | Skip the next node while it holds the same value |
| 92 | [Reverse Linked List II](linked_list/lc0092_reverse_linked_list_ii.py) | Medium | Walk to the node before `left`, then move each next node to the front of the sublist (head insertion) |
| 141 | [Linked List Cycle](linked_list/lc0141_linked_list_cycle.py) | Easy | Floyd's tortoise and hare. A fast pointer catches the slow one only if there is a loop |
| 142 | [Linked List Cycle II](linked_list/lc0142_linked_list_cycle_ii.py) | Medium | Floyd: after slow and fast meet, a pointer from the head and one from the meeting point meet at the cycle start |
| 143 | [Reorder List](linked_list/lc0143_reorder_list.py) | Medium | Find the middle, reverse the second half, then weave the two halves together |
| 146 | [LRU Cache](linked_list/lc0146_lru_cache.py) | Medium | An OrderedDict keeps keys in use order |
| 160 | [Intersection of Two Linked Lists](linked_list/lc0160_intersection_of_two_linked_lists.py) | Easy | Two pointers that switch to the other list at the end meet at the intersection (or both reach None) |
| 203 | [Remove Linked List Elements](linked_list/lc0203_remove_linked_list_elements.py) | Easy | Dummy head so the first node can be removed like any other |
| 206 | [Reverse Linked List](linked_list/lc0206_reverse_linked_list.py) | Easy | Walk the list and point each node back at the previous one |
| 234 | [Palindrome Linked List](linked_list/lc0234_palindrome_linked_list.py) | Easy | Find the middle with slow/fast pointers, reverse the second half, compare both halves |
| 328 | [Odd Even Linked List](linked_list/lc0328_odd_even_linked_list.py) | Medium | Build the odd and even chains in one pass, then attach the even chain after the odd one |
| 876 | [Middle of the Linked List](linked_list/lc0876_middle_of_the_linked_list.py) | Easy | Slow moves one step, fast moves two; when fast ends, slow is in the middle |

### Trees (25)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 94 | [Binary Tree Inorder Traversal](trees/lc0094_binary_tree_inorder_traversal.py) | Easy | Iterative: go left as far as possible pushing nodes, then visit and turn right |
| 98 | [Validate Binary Search Tree](trees/lc0098_validate_binary_search_tree.py) | Medium | Pass down the allowed (low, high) range |
| 100 | [Same Tree](trees/lc0100_same_tree.py) | Easy | Two trees match if the roots match and both pairs of subtrees match |
| 101 | [Symmetric Tree](trees/lc0101_symmetric_tree.py) | Easy | Two subtrees mirror each other when their roots match and outer/inner children mirror too |
| 102 | [Binary Tree Level Order Traversal](trees/lc0102_binary_tree_level_order_traversal.py) | Medium | BFS with a queue, handling one whole level per loop |
| 103 | [Binary Tree Zigzag Level Order Traversal](trees/lc0103_binary_tree_zigzag_level_order_traversal.py) | Medium | Normal BFS by levels; reverse every second level |
| 104 | [Maximum Depth of Binary Tree](trees/lc0104_maximum_depth_of_binary_tree.py) | Easy | Depth of a node is 1 + the deeper of its two subtrees |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](trees/lc0105_construct_binary_tree_from_preorder_and_inorder_traversal.py) | Medium | The next preorder value is the root |
| 108 | [Convert Sorted Array to Binary Search Tree](trees/lc0108_convert_sorted_array_to_binary_search_tree.py) | Easy | The middle element becomes the root; build both halves the same way (height-balanced) |
| 110 | [Balanced Binary Tree](trees/lc0110_balanced_binary_tree.py) | Easy | DFS returns the height, or -1 as soon as any subtree is unbalanced |
| 111 | [Minimum Depth of Binary Tree](trees/lc0111_minimum_depth_of_binary_tree.py) | Easy | BFS: the first leaf reached gives the minimum depth |
| 112 | [Path Sum](trees/lc0112_path_sum.py) | Easy | Subtract each value on the way down; at a leaf the remainder must be zero |
| 113 | [Path Sum II](trees/lc0113_path_sum_ii.py) | Medium | Backtracking DFS that keeps the current path and records it at leaves that hit the target |
| 144 | [Binary Tree Preorder Traversal](trees/lc0144_binary_tree_preorder_traversal.py) | Easy | Iterative with a stack: visit the node, push right then left |
| 199 | [Binary Tree Right Side View](trees/lc0199_binary_tree_right_side_view.py) | Medium | BFS level by level and keep the last node of each level |
| 226 | [Invert Binary Tree](trees/lc0226_invert_binary_tree.py) | Easy | Swap the left and right child of every node, recursively |
| 230 | [Kth Smallest Element in a BST](trees/lc0230_kth_smallest_element_in_a_bst.py) | Medium | In-order traversal of a BST visits values in sorted order |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](trees/lc0235_lowest_common_ancestor_of_a_binary_search_tree.py) | Medium | Walk down from the root |
| 236 | [Lowest Common Ancestor of a Binary Tree](trees/lc0236_lowest_common_ancestor_of_a_binary_tree.py) | Medium | Post-order: a node whose left and right searches both found something is the LCA |
| 257 | [Binary Tree Paths](trees/lc0257_binary_tree_paths.py) | Easy | DFS carrying the path so far as text; save it at every leaf |
| 543 | [Diameter of Binary Tree](trees/lc0543_diameter_of_binary_tree.py) | Easy | DFS returns each height |
| 572 | [Subtree of Another Tree](trees/lc0572_subtree_of_another_tree.py) | Easy | At every node of root, check whether the tree starting there is the same as subRoot |
| 617 | [Merge Two Binary Trees](trees/lc0617_merge_two_binary_trees.py) | Easy | Recursively add overlapping nodes; where only one tree has a node, reuse it |
| 700 | [Search in a Binary Search Tree](trees/lc0700_search_in_a_binary_search_tree.py) | Easy | Go left or right by comparing with the node value |
| 1448 | [Count Good Nodes in Binary Tree](trees/lc1448_count_good_nodes_in_binary_tree.py) | Medium | DFS carrying the largest value seen on the path; a node is good when it is at least that big |

### Heap / Priority Queue (7)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 215 | [Kth Largest Element in an Array](heap/lc0215_kth_largest_element_in_an_array.py) | Medium | Keep a min-heap of the k largest numbers; its top is the answer |
| 621 | [Task Scheduler](heap/lc0621_task_scheduler.py) | Medium | Formula: the most frequent task sets (maxCount - 1) frames of length n + 1, plus the tasks tied for the max |
| 692 | [Top K Frequent Words](heap/lc0692_top_k_frequent_words.py) | Medium | Count words, then take the k smallest by (-count, word) so ties sort alphabetically |
| 703 | [Kth Largest Element in a Stream](heap/lc0703_kth_largest_element_in_a_stream.py) | Easy | A min-heap of size k: the smallest of the k largest is the k-th largest |
| 767 | [Reorganize String](heap/lc0767_reorganize_string.py) | Medium | Always place the most frequent remaining letter that differs from the last one placed (max-heap) |
| 973 | [K Closest Points to Origin](heap/lc0973_k_closest_points_to_origin.py) | Medium | heapq.nsmallest by squared distance (no square roots needed) |
| 1046 | [Last Stone Weight](heap/lc1046_last_stone_weight.py) | Easy | Max-heap (negated values): smash the two heaviest and push back the difference |

### Backtracking (11)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 17 | [Letter Combinations of a Phone Number](backtracking/lc0017_letter_combinations_of_a_phone_number.py) | Medium | Build combinations digit by digit (iterative product over the phone letters) |
| 39 | [Combination Sum](backtracking/lc0039_combination_sum.py) | Medium | Backtrack over sorted candidates; reuse is allowed, so recurse from the same index |
| 40 | [Combination Sum II](backtracking/lc0040_combination_sum_ii.py) | Medium | Sort; each number used once, and skip equal numbers at the same depth to avoid duplicate sets |
| 46 | [Permutations](backtracking/lc0046_permutations.py) | Medium | Swap each remaining number into the current position and recurse |
| 47 | [Permutations II](backtracking/lc0047_permutations_ii.py) | Medium | Count each value and place values from the counter, so duplicates never produce the same permutation twice |
| 77 | [Combinations](backtracking/lc0077_combinations.py) | Medium | Pick numbers in increasing order; stop early when not enough numbers are left |
| 78 | [Subsets](backtracking/lc0078_subsets.py) | Medium | Start with the empty set; each number doubles the list by adding itself to every subset so far |
| 79 | [Word Search](backtracking/lc0079_word_search.py) | Medium | DFS from every cell, marking cells as used on the current path and restoring them on the way back |
| 90 | [Subsets II](backtracking/lc0090_subsets_ii.py) | Medium | Sort; when a number repeats, only extend the subsets made in the previous step |
| 131 | [Palindrome Partitioning](backtracking/lc0131_palindrome_partitioning.py) | Medium | Cut off every palindromic prefix and partition the rest recursively |
| 216 | [Combination Sum III](backtracking/lc0216_combination_sum_iii.py) | Medium | Choose k distinct digits 1-9 in increasing order that add up to n |

### Graphs (16)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 130 | [Surrounded Regions](graphs/lc0130_surrounded_regions.py) | Medium | Mark every 'O' connected to the border as safe; flip the rest to 'X' |
| 133 | [Clone Graph](graphs/lc0133_clone_graph.py) | Medium | DFS with a map from each original node to its copy, so cycles are copied once |
| 200 | [Number of Islands](graphs/lc0200_number_of_islands.py) | Medium | For each unvisited land cell, flood-fill its island and count one |
| 207 | [Course Schedule](graphs/lc0207_course_schedule.py) | Medium | Kahn's topological sort. If every course can be taken once its prerequisites are done, there is no cycle |
| 210 | [Course Schedule II](graphs/lc0210_course_schedule_ii.py) | Medium | Kahn's topological sort, recording the order courses are taken |
| 417 | [Pacific Atlantic Water Flow](graphs/lc0417_pacific_atlantic_water_flow.py) | Medium | Flood uphill from each ocean's edge; cells reached from both oceans are the answer |
| 547 | [Number of Provinces](graphs/lc0547_number_of_provinces.py) | Medium | Union-find over the adjacency matrix; count the distinct roots |
| 684 | [Redundant Connection](graphs/lc0684_redundant_connection.py) | Medium | Union-find: the first edge whose two ends already share a root closes the cycle |
| 695 | [Max Area of Island](graphs/lc0695_max_area_of_island.py) | Medium | DFS from every unvisited land cell, counting cells and sinking them so they are not counted twice |
| 733 | [Flood Fill](graphs/lc0733_flood_fill.py) | Easy | DFS from the start pixel, recolouring every connected pixel of the old colour |
| 743 | [Network Delay Time](graphs/lc0743_network_delay_time.py) | Medium | Dijkstra from k; the answer is the longest shortest path, or -1 if a node is unreachable |
| 785 | [Is Graph Bipartite?](graphs/lc0785_is_graph_bipartite.py) | Medium | Two-colour every component with BFS; an edge between equal colours means not bipartite |
| 841 | [Keys and Rooms](graphs/lc0841_keys_and_rooms.py) | Medium | DFS from room 0 collecting keys; check every room was visited |
| 994 | [Rotting Oranges](graphs/lc0994_rotting_oranges.py) | Medium | Multi-source BFS starting from every rotten orange at once |
| 1584 | [Min Cost to Connect All Points](graphs/lc1584_min_cost_to_connect_all_points.py) | Medium | Prim's algorithm on the complete graph with Manhattan distances (O(n^2), no heap needed) |
| 1971 | [Find if Path Exists in Graph](graphs/lc1971_find_if_path_exists_in_graph.py) | Easy | Union-find over the edges, then check whether source and destination share a root |

### Trie (2)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 208 | [Implement Trie (Prefix Tree)](trie/lc0208_implement_trie_prefix_tree.py) | Medium | Nested dicts, one level per letter; a special key marks the end of a word |
| 211 | [Design Add and Search Words Data Structure](trie/lc0211_design_add_and_search_words_data_structure.py) | Medium | A trie; '.' branches into every child during search |

### Dynamic Programming (23)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 5 | [Longest Palindromic Substring](dp/lc0005_longest_palindromic_substring.py) | Medium | Expand around every centre (one letter and between two letters) and keep the longest |
| 45 | [Jump Game II](dp/lc0045_jump_game_ii.py) | Medium | BFS by layers: each jump covers a range; count how many ranges until the end is reached |
| 55 | [Jump Game](dp/lc0055_jump_game.py) | Medium | Track the furthest index reachable so far; fail if we ever stand beyond it |
| 62 | [Unique Paths](dp/lc0062_unique_paths.py) | Medium | DP row by row. Paths to a cell = paths from above + paths from the left |
| 63 | [Unique Paths II](dp/lc0063_unique_paths_ii.py) | Medium | One row of DP: paths into a cell = paths from above + from the left, zero on obstacles |
| 64 | [Minimum Path Sum](dp/lc0064_minimum_path_sum.py) | Medium | Each cell's best cost is its value plus the cheaper of the cells above and to the left |
| 70 | [Climbing Stairs](dp/lc0070_climbing_stairs.py) | Easy | Ways to reach step n = ways(n - 1) + ways(n - 2): Fibonacci with two variables |
| 72 | [Edit Distance](dp/lc0072_edit_distance.py) | Medium | dp[i][j] = edits to turn word1[:i] into word2[:j]: keep on a match, else 1 + min(insert, delete, replace) |
| 91 | [Decode Ways](dp/lc0091_decode_ways.py) | Medium | Ways to decode s[:i] = ways(i - 1) if the last digit is 1-9, plus ways(i - 2) if the last two form 10-26 |
| 96 | [Unique Binary Search Trees](dp/lc0096_unique_binary_search_trees.py) | Medium | Catalan numbers: pick each value as root, multiply the counts of left and right subtrees |
| 120 | [Triangle](dp/lc0120_triangle.py) | Medium | Bottom-up: each cell becomes itself plus the smaller of the two cells below it |
| 139 | [Word Break](dp/lc0139_word_break.py) | Medium | ok[i] is true when some word ends at i and ok[i - len(word)] is true |
| 152 | [Maximum Product Subarray](dp/lc0152_maximum_product_subarray.py) | Medium | Track both the largest and smallest product ending here, since a negative number swaps them |
| 198 | [House Robber](dp/lc0198_house_robber.py) | Medium | DP. At each house, either skip it or rob it plus the best from two houses back |
| 213 | [House Robber II](dp/lc0213_house_robber_ii.py) | Medium | Houses form a circle, so the first and last cannot both be robbed: solve House Robber without the |
| 279 | [Perfect Squares](dp/lc0279_perfect_squares.py) | Medium | dp[n] = 1 + min(dp[n - k^2]) over all squares k^2 <= n |
| 322 | [Coin Change](dp/lc0322_coin_change.py) | Medium | Bottom-up DP. dp[a] is the fewest coins for amount a, trying each coin as the last one |
| 416 | [Partition Equal Subset Sum](dp/lc0416_partition_equal_subset_sum.py) | Medium | 0/1 knapsack as a bitset: bit k is set when some subset sums to k; check half the total |
| 494 | [Target Sum](dp/lc0494_target_sum.py) | Medium | Count sign choices with a map from running sum to number of ways |
| 518 | [Coin Change II](dp/lc0518_coin_change_ii.py) | Medium | Unbounded knapsack counting: loop over coins outside so each combination is counted once |
| 647 | [Palindromic Substrings](dp/lc0647_palindromic_substrings.py) | Medium | Expand around every centre and count each palindrome found on the way out |
| 746 | [Min Cost Climbing Stairs](dp/lc0746_min_cost_climbing_stairs.py) | Easy | Cost to stand past step i = cost[i] + min of the two steps before |
| 1143 | [Longest Common Subsequence](dp/lc1143_longest_common_subsequence.py) | Medium | 2-D DP. Matching characters extend the diagonal |

### Greedy (6)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 122 | [Best Time to Buy and Sell Stock II](greedy/lc0122_best_time_to_buy_and_sell_stock_ii.py) | Medium | Take every upward step: the sum of all positive day-to-day differences |
| 134 | [Gas Station](greedy/lc0134_gas_station.py) | Medium | If total gas >= total cost a start exists; restart after any point where the tank goes negative |
| 678 | [Valid Parenthesis String](greedy/lc0678_valid_parenthesis_string.py) | Medium | Track the lowest and highest possible number of open brackets; '*' widens the range |
| 763 | [Partition Labels](greedy/lc0763_partition_labels.py) | Medium | Know each letter's last index; close a part when the scan reaches the furthest last index seen |
| 846 | [Hand of Straights](greedy/lc0846_hand_of_straights.py) | Medium | Always start a group at the smallest card left and take the next groupSize consecutive cards |
| 860 | [Lemonade Change](greedy/lc0860_lemonade_change.py) | Easy | Keep counts of 5s and 10s; give change with a 10 first when possible |

### Math & Bit Manipulation (9)

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 7 | [Reverse Integer](math_bits/lc0007_reverse_integer.py) | Medium | Reverse the digits of |x|, restore the sign, and return 0 if it leaves the 32-bit range |
| 9 | [Palindrome Number](math_bits/lc0009_palindrome_number.py) | Easy | Reverse only the second half of the digits and compare with the first half (no strings) |
| 13 | [Roman to Integer](math_bits/lc0013_roman_to_integer.py) | Easy | Add each symbol, but subtract it when a bigger symbol follows (like IV or XC) |
| 50 | [Pow(x, n)](math_bits/lc0050_pow_x_n.py) | Medium | Fast exponentiation by squaring; a negative n means 1 / x^-n |
| 66 | [Plus One](math_bits/lc0066_plus_one.py) | Easy | Add one from the right; 9 becomes 0 and carries, otherwise stop |
| 191 | [Number of 1 Bits](math_bits/lc0191_number_of_1_bits.py) | Easy | n & (n - 1) clears the lowest set bit; count how many times until zero |
| 202 | [Happy Number](math_bits/lc0202_happy_number.py) | Easy | Repeat 'sum of squared digits'; Floyd's cycle check stops at 1 or at a loop |
| 268 | [Missing Number](math_bits/lc0268_missing_number.py) | Easy | The sum 0..n minus the sum of the array is the missing number |
| 338 | [Counting Bits](math_bits/lc0338_counting_bits.py) | Easy | bits[i] = bits[i >> 1] + (i & 1): drop the last bit, then add it back |

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
