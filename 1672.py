# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/
# Solution: Angel Piña

import pytest


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        individual_wealth: int
        wealth_list: list = []

        for i in range(len(accounts)):
            individual_wealth = 0
            for j in range(len(accounts[i])):
                individual_wealth += accounts[i][j]
            wealth_list.append(individual_wealth)
            continue

        max_wealth: int = max(wealth_list)
        return max_wealth


# Tests for the given solution
class Tests:
    @pytest.mark.parametrize(
        "input, output",
        [
            ([[1, 2, 3], [3, 2, 1]], 6),
            ([[1, 5], [7, 3], [3, 5]], 10),
            ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ],
    )
    def test_maximumWealth(self, input, output):
        assert Solution().maximumWealth(input) == output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
