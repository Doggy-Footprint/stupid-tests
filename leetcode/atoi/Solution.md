# Strategy

No outstanding strategy. I can't understand it's acceptance rate (17.4%).
A small trick is to determine if max is reached.

```java
class Solution {
    private static final int STEP1 = 1;
    private static final int STEP2 = 2;
    private static final int STEP3 = 3;
    private static final int STEP4 = 4;
    private ArrayList<Character> posMax = new ArrayList<>(Arrays.asList(new Character[]{'2', '1', '4', '7', '4', '8', '3', '6', '4', '7'}));
    private ArrayList<Character> negMin = new ArrayList<>(Arrays.asList(new Character[]{'2', '1', '4', '7', '4', '8', '3', '6', '4', '8'}));
    private static final int offset = 48; //  (int)'0' = 48

    public int myAtoi(String s) {
        int length = s.length();
        int state = Solution.STEP1;
        boolean isPositive = true;
        boolean minMaxReached = false;

        ArrayList<Character> output = new ArrayList<>();

        for (int i = 0; i < length; i++) {
            Character c = s.charAt(i);
            if (state == Solution.STEP1) {
                if (c == ' ') continue;
                else state = Solution.STEP2;
            } 
            if (state == Solution.STEP2) {
                if (c == '+') {
                    state = Solution.STEP3;
                    continue;
                } else if (c == '-') {
                    isPositive = false;
                    state = Solution.STEP3;
                    continue;
                } else {
                    state = Solution.STEP3;
                }
            }
            if (state == Solution.STEP3) {
                if (c == '0') continue;
                if (c > '0' && c <= '9') {
                    output.add(c);
                    state = Solution.STEP4;
                    continue;
                } else {
                    return 0;
                }
            }
            if (state == Solution.STEP4) {
                if (c >= '0' && c <= '9') {
                    output.add(c);
                    if (output.size() == 10) {
                        minMaxReached = this.checkMinMax(output, isPositive);
                        if (minMaxReached) break;
                    } else if (output.size() >= 11) {
                        minMaxReached = true;
                        break;
                    }
                } else {
                    break;
                }
            }
        }

        if (minMaxReached) {
            return  isPositive ? 2147483647 : -2147483648;
        } else {
            if (output.size() == 0) return 0;
            int sign = isPositive ? 1 : -1;
            int out = 0;
            out = sign * ((int)output.get(0) - Solution.offset);
            for (int i = 1; i < output.size(); i++) {
                out *= 10;
                out += sign * ((int)output.get(i) - Solution.offset);
            }
            return out;
        }
    }

    public boolean checkMinMax(ArrayList<Character> output, boolean isPositive) {
        ArrayList<Character> limit = isPositive ? this.posMax : this.negMin;
        for (int i = 0; i < 10; i++) {
            if (output.get(i) > limit.get(i)) return true;
            else if (output.get(i) < limit.get(i)) return false;
        }
        return true;
    }
}
```