import dev.devs.Main;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import static org.assertj.core.api.Assertions.*;


import java.util.stream.Stream;

public class TestMedianOfTwoSortedArrays {
    @ParameterizedTest
    @MethodSource("getTestCases")
    void testSolution(int[] nums1, int[] nums2, Double expected) {
        Main solution = new Main();
        assertThat(solution.findMedianSortedArrays(nums1, nums2)).isEqualTo(expected);
    }

    static Stream<Arguments> getTestCases() {
        return Stream.of(
                Arguments.arguments(new int[]{1, 2, 3, 4, 5}, new int[]{8, 9, 10}, 4.5),
                Arguments.arguments(new int[]{8,9,10}, new int[]{1, 2, 3, 4, 5}, 4.5),
                Arguments.arguments(new int[]{1,3}, new int[]{2}, 2.0),
                Arguments.arguments(new int[]{1,2,5,6}, new int[]{2}, 2.0),
                Arguments.arguments(new int[]{1,2,5}, new int[]{3}, 2.5),
                Arguments.arguments(new int[]{}, new int[]{1,2,3,4,5,6}, 3.5)
//                Arguments.arguments(new int[]{}, new int[]{1,2,3,4,5,6}, 3.5),
        );
    }
}
