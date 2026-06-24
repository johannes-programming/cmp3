"""This module provides cmp3 functionality."""

import math
import unittest
from typing import Any, Self

from cmp3.core.cmp import cmp

__all__ = ["TestCmpPoset"]


class TestCmpPoset(unittest.TestCase):
    def test_poset_equal(self: Self) -> None:
        # subset ordering: same set
        self.assertEqual(cmp({1, 2}, {1, 2}, mode="le"), 0)

    def test_poset_less(self: Self) -> None:
        # subset ordering: strict subset
        self.assertEqual(cmp({1}, {1, 2}, mode="le"), -1)

    def test_poset_greater(self: Self) -> None:
        # subset ordering: strict superset
        self.assertEqual(cmp({1, 2}, {1}, mode="le"), 1)

    def test_poset_incomparable(self: Self) -> None:
        # incomparable in subset ordering
        res: Any
        res = cmp({1}, {2}, mode="le")
        self.assertTrue(math.isnan(res))


if __name__ == "__main__":
    unittest.main()
