# Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

## Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

## Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
```
P     I    N
A   L S  I G
Y A   H R
P     I
```
## Example 3:

Input: s = "A", numRows = 1
Output: "A"

# Strategy

**Simple mathematical induction problem**

# Solution
```java
class Solution {
    // size of triangle: 2n - 2: except first and last, remaining size , and complementary. for example of n = 4, 
    // second row (2n - 2 - 2 * '1')
    // 4,2,4,2
    // third row (2n - 2 - 2 * '2')
    // 2,4,2,4
    public String convert(String s, int numRows) {
        int length = s.length();
        char[] output = new char[length];
        int cursor = 0;
        if (numRows == 1) {
            return s;
        } else if (numRows == 2) {
            int i = 0; 
            while (i < length) {
                output[cursor] = s.charAt(i);
                i += 2;
                cursor ++;
            }
            int j = 1;
            while (j < length) {
                output[cursor] = s.charAt(j);
                j += 2;
                cursor++;
            }
            return new String(output);
        } else { 
            int sizeOfTriangle = 2 * numRows - 2;
            //first
            int pos = 0;
            while (pos < length) {
                output[cursor] = s.charAt(pos);
                pos += sizeOfTriangle;
                cursor++;
            }
            //middle
            for (int i = 1; i < numRows - 1; i++) {
                // 
                // 2 * i 
                // repeate two
                int step = sizeOfTriangle - 2 * i;
                int j = i;
                while (j < length) {
                    output[cursor] = s.charAt(j);
                    j += step;
                    step = sizeOfTriangle - step; 
                    cursor++;
                }
            }
            //last
            pos = numRows - 1;
            while (pos < length) {
                output[cursor] = s.charAt(pos);
                pos += sizeOfTriangle;
                cursor++;
            }
            return new String(output);
        }
    }
}
```