package dev.devs;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.printf("Hello and welcome!");
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /**
         analysis:
         left array: first element is smaller than the other
         right array: not left array
         note: left array's last element might be bigger than right one's last.
         but, It can be proved that the medium is included in
         right m+n/4 part of left array and left m+n/4 part of right array
         conclusive case:
         left array's last element is smaller than right array's first element.
         tatic:
         In each step, partition each arrays by one-fourth of remaining size.
         As above, we can prove that medium is in the right partition of left array
         and left partition of right array
         */
        int start1 = 0;
        int end1 = nums1.length - 1;
        int start2 = 0;
        int end2 = nums2.length - 1;
        boolean isOdd = (nums1.length + nums2.length) % 2 == 1;

        if (nums1.length == 0) {
            return isOdd ? (double)nums2[nums2.length/2]: ((double)nums2[nums2.length/2 - 1] + (double)nums2[nums2.length/2])/2.0;
        } else if (nums2.length == 0) {
            return isOdd ? (double)nums1[nums1.length/2]: ((double)nums1[nums1.length/2 - 1] + (double)nums1[nums1.length/2])/2.0;
        }


        while (end1 - start1 + end2 - start2 + 2 > 5) {
            if (nums1[end1] < nums2[start2]) {
                // two partitions have no overlap, a partition of nums1 comes first
                return this.getMedianFromOrderedPartitions(isOdd, nums1, nums2, start1, end1, start2, end2);
            } else if (nums1[start1] > nums2[end2]) {
                // two partitions have no overlap, a partition of nums2 comes first
                return this.getMedianFromOrderedPartitions(isOdd, nums2, nums1, start2, end2, start1, end1);
            }


            // fraction problem - as long as keep removing same size, the oddity remains. and median remains median.
            int sizeOfPartitionToRemove = (end1 - start1 + end2 - start2 + 2) / 4;

            // core consideration: case [2], and [1,3,4,5,6] -> m+n/4 is not guarnteed to be smaller than m or n
            /**
             * there are two cases,
             * a smaller one might include median (can't be ignored)
             * a smaller one can't include median (can be ignored)
             * either ends of smaller one is included in large one's both sides partitioned state.
             */
            // TODO from here

            if (nums1[start1] <= nums2[start2]) {
                // partition of nums1 is aheading or equal
                start1 = start1 + sizeOfPartitionToRemove;
                end2 = end2 - sizeOfPartitionToRemove;
            } else {
                // partition of nums2 is aheading
                start2 = start2 + sizeOfPartitionToRemove;
                end1 = end1 - sizeOfPartitionToRemove;
            }
        }

        return this.getMedianBrutally(isOdd, nums1, nums2, start1, end1, start2, end2);
    }

    double getMedianFromOrderedPartitions(boolean isOdd, int[] aheading, int[] following, int sa, int ea, int sf, int ef) {
        int size = ea + ef -sa -sf + 2;
        if (isOdd) {
            int index = size / 2;
            if (ea - sa >= index) return aheading[sa + index];
            else return following[sf + index - (ea - sa + 1)];
        } else {
            int index1 = size / 2;
            int index2 = index1 - 1;
            if (ea - sa >= index1) {
                // aheading partitino includes both
                return ((double)aheading[sa + index1] + (double)aheading[sa + index2]) / 2.0;
            } else if (ea - sa < index1 && ea - sa >= index2) {
                // each partition has each index
                return ((double)aheading[ea] + (double)following[sf])/2.0;
            } else {
                // following partition includes both
                return ((double)following[sf + index1 - (ea - sa + 1)] + (double)following[sf + index2 - (ea - sa + 1)])/2.0;
            }
        }
    }

    double getMedianBrutally(boolean isOdd, int[] nums1, int[] nums2, int start1, int end1, int start2, int end2) {
        int size = end1 - start1 + end2 - start2 + 2;
        int[] merged = new int[size];

        int i = 0;
        int j = 0;
        for (int m = 0; m < size; m++) {
            if (start1 + i > end1) {
                merged[m] = nums2[start2 + j++];
                continue;
            }
            if (start2 + j > end2) {
                merged[m] = nums1[start1 + i++];
                continue;
            }
            if (nums1[start1 + i] <= nums2[start2 + j]) {
                merged[m] = nums1[start1 + i++];
            } else {
                merged[m] = nums2[start2 + j++];
            }
        }

        return isOdd ? (double)merged[size/2] : ((double)merged[size/2 - 1] + (double)merged[size/2])/2.0;
    }
}