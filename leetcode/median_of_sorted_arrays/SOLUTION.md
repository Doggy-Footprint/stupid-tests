# Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Strategy

To achieve `O(log (m+n))`, half of remaining elements need to be trimed for each step (**Binary Search**)

## Strategy 1 - wrong

half each arrays

position of median is changed upon steps. - can't track median

## Strategy 2 - correct

remove the quarter of remaining elements from both side: `(m+n)/4`

### Substrategy 1 - wrong

find aheading array and following array and remove first `(m+n)/4` in aheading array and remove trailing `(m+n)/4` in following array

### Substrategy 2 - correct

Check both arrays (m+n)/4 partitions. That is, check the biggest elements of each array's front `(m+n)/4` partition. The partition with smaller biggest element will be removed.
Same logic allied to the back `(m+n)/4` partition.

#### key idea

remove half of elements while reserving median as median

### Core Cases (including edge cases)

#### Case 1

A array becomes empty while loop.

#### Case 2

Arrays are ordered (i.e. end of one array is smaller than the start of the other)

#### Case 3

A array is 3+ times bigger than the other. In this case, the larger one's both side can be partitioned reserving median

#### Case 4

A array is exactly 3 times bigger than the other. In this case, we can't be sure if median is reserved if we remove both side of the larger one.