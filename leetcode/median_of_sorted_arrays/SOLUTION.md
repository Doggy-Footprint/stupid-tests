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

**half each arrays**

position of median is changed upon steps. - can't track median

## Strategy 2 - developing

**remove the quarter of remaining elements from both side: `(m+n)/4`**

### SubStrategy 1

**find aheading array and following array and remove first `(m+n)/4` in aheading array and remove trailing `(m+n)/4` in following array**

#### edge cases 

**one array is three or more times bigger than the other**: trim the big one on both side
**`[2, 3], [1, 4, 5, 6]` edge case**: `3` is median but *trimmed*
**one array is entirely overlapped by the other**

### SubStrategy 2

**find mathematically guarnteed not-median elements and trim it**
**Ground rule is it should be trimed `(m+n)/4` on both side, not the same size on each array**