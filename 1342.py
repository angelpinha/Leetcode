# 1324. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Solution: Angel Piña

import pytest


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps: int = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            steps += 1
        return steps


# Tests for the given solution
class Tests:
    @pytest.mark.parametrize(
        "input, output",
        [
            (14, 6),
            (8, 4),
            (123, 12),
        ],
    )
    def test_numberOfSteps(self, input, output):
        assert Solution().numberOfSteps(input) == output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
