# Description
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

# Strategy
1. determine if input overflow when reversed.
2. reverse.

# Solution
```java
class Solution {
    public int reverse(int x) {
        // 2^31 - 1 = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]

        /**
         * 1. would reverse overflow? - clear
         * 2. parse digit by modular - clear
         */

        if (this.wouldReverseOverflow(x)) return 0;

        int reverse = 0;
        int origin = x;

        while (origin != 0) {
            int digit = origin % 10;
            reverse *= 10;
            reverse += digit;
            origin /= 10;
        }

        return reverse;
    }

    boolean wouldReverseOverflow(int x) {
        if (x / 1000000000 == 0) return false;

        int[] maximum = {2, 1, 4, 7, 4, 8, 3, 6, 4, 7};
        if (x < 0) {
            // get rid of edge case.
            if (x == -2147483648) return true;

            x *= -1;
            maximum[9] = 8;
        }

        int modularDivisor = 10;
        int trimmer = 1;
        for (int i = 0; i < 10; i++, modularDivisor *= 10, trimmer*= 10) {
            int digit = (x % modularDivisor) / trimmer;
            if (digit == maximum[i]) continue;
            return digit > maximum[i];
        }
        return false;
    }
}
```