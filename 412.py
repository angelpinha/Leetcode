# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# Solution: Angel Piña

import pytest


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        number_list: list = list()
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                number_list.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                number_list.append("Fizz")
                continue
            elif i % 5 == 0:
                number_list.append("Buzz")
                continue
            else:
                number_list.append(str(i))
        return number_list


# Tests for the given solution
class Tests:
    @pytest.mark.parametrize(
        "input, output",
        [
            (3, ["1", "2", "Fizz"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
        ],
    )
    def test_fizzBuzz(self, input, output):
        assert Solution().fizzBuzz(input) == output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
