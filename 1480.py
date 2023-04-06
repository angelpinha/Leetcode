# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Solution: Angel Piña

import pytest


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                nums[i] += nums[i - 1]
        return nums


# Tests for the given solution
class Tests:
    @pytest.mark.parametrize(
        "input, output",
        [
            ([1, 2, 3, 4], [1, 3, 6, 10]),
            ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ],
    )
    def test_running_sum(self, input, output):
        assert Solution().runningSum(input) == output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
