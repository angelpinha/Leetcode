# 2235. Add Two Integers
# https://leetcode.com/problems/add-two-integers/
# Solution: Angel Piña

import pytest


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# Tests for the given solution
class Tests:
    @pytest.mark.parametrize(
        "i1, i2, output",
        [
            (12, 5, 17),
            (-10, 4, -6),
        ],
    )
    def test_sum(self, i1, i2, output):
        assert Solution().sum(i1, i2) == output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
