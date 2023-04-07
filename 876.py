# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# Solution: Angel Piña

import pytest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one_step = head
        two_steps = head

        while two_steps and two_steps.next:
            one_step = one_step.next
            two_steps = two_steps.next.next

        return one_step


# Tests for the given solution
class Tests:
    # First test case
    def test_middleNode_case01(self):
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        solution = Solution()
        middle = solution.middleNode(input)
        assert middle.val == 3
        assert middle.next.val == 4
        assert middle.next.next.val == 5
        assert middle.next.next.next is None
        return

    # Second test case
    def test_middleNode_case02(self):
        input = ListNode(
            1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))
        )
        solution = Solution()
        middle = solution.middleNode(input)
        assert middle.val == 4
        assert middle.next.val == 5
        assert middle.next.next.val == 6
        assert middle.next.next.next is None
        return


if __name__ == "__main__":
    pytest.main(["-v", __file__])
