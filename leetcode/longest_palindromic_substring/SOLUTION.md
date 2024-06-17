# Description
Given a string s, return the longest palindromic substring in `s`.

## Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

## Example 2:

Input: s = "cbbd"
Output: "bb"

# Strategy

Parsing from one side to the other end, no information guarntees that following string will form palindromic or not. that is, we need to check all n elements to be sure if we checked for every substrings. For example, even substring larger than the half of original string can't assure that's the biggest one. The whole string might be a palindromc string.

Thus my strategy is **rollback to folding spot after finding palindromic**. And this means discarding all informations after folding spot even if we checked it for a palindromic substring we just found.

# Solution
```java
class Solution {
    public String longestPalindrome(String s) {
        int cursor = 0;
        int current_fold = 0;
        // cursor return to this after finding a palindromic substring
        int cursor_return = 0;
        int[] longestPalindromic = new int[2];

        if (s.length() == 1) return s;

        cursor = 2; // skiping first two elements
        if (s.charAt(0) == s.charAt(1)) {
            longestPalindromic[0] = 0;
            longestPalindromic[1] = 1;
        }

        while (cursor < s.length()) {
            if (s.charAt(cursor) == s.charAt(cursor - 1)) {
            //even case folding
            int [] newPalindromic = this.rollbackOverEvenPalindromic(s, cursor);
                if (this.isNewSubstringLonger(newPalindromic, longestPalindromic)) {
                    longestPalindromic[0] = newPalindromic[0];
                    longestPalindromic[1] = newPalindromic[1];
                }
            }
            /// ccc case 
            if (s.charAt(cursor) == s.charAt(cursor -2)) {
            //odd case folding
            int [] newPalindromic = this.rollbackOverOddPalindromic(s, cursor);
                if (this.isNewSubstringLonger(newPalindromic, longestPalindromic)) {
                    longestPalindromic[0] = newPalindromic[0];
                    longestPalindromic[1] = newPalindromic[1];
                }
            }
            cursor++;
        }

        return s.substring(longestPalindromic[0], longestPalindromic[1] + 1);
    }

    public int[] rollbackOverEvenPalindromic(String s, int cursor) {
        int i = 0;
        while (cursor - 1 - i >= 0 
            && cursor + i < s.length() 
            && s.charAt(cursor + i) == s.charAt(cursor - 1 - i)) {
            i++;
        } 
        i--;
        int[] output = {cursor - 1 - i, cursor + i};
        return output;
    }

    public int[] rollbackOverOddPalindromic(String s, int cursor) {
        int i = 0;
        while (cursor - 2 - i >= 0 
            && cursor + i < s.length() 
            && s.charAt(cursor + i) == s.charAt(cursor - 2 - i)) {
            i++;
        }
        i--;
        int[] output = {cursor - 2 - i, cursor + i};
        return output;
    }

    public boolean isNewSubstringLonger(int[] newOne, int[] oldOne) {
        return newOne[1] - newOne[0] > oldOne[1] - oldOne[0];
    }
}
```