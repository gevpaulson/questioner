import pytest
from main import Solution

def test_first_missing_positive_bigger_zero():
    sol = Solution()
    assert sol.firstMissingPositive([7,8,9,11,12]) == 1
    assert sol.firstMissingPositive(([-1, -2])) == 1
    assert sol.firstMissingPositive(([-1, -2, 2, 3])) == 1


def test_first_missing_positive_between_positives():
    sol = Solution()
    assert sol.firstMissingPositive([-1, 1, 2, 4]) == 3

def test_first_missing_positive_bigger_max():
    sol = Solution()
    assert  sol.firstMissingPositive([1,2,3]) == 4
    assert  sol.firstMissingPositive([-1, -2 -5, 0, 1, 2]) == 3
    assert  sol.firstMissingPositive([1, 2, -1, -2 -5, 0]) == 3
    assert  sol.firstMissingPositive([-1, -2, 1, 2, -5, 0]) == 3
