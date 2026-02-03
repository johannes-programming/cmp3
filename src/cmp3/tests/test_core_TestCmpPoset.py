import math
import unittest
from typing import *

from cmp3 import core

__all__ = ["TestCmpPoset"]


class TestCmpPoset(unittest.TestCase):
    def test_poset_equal(self: Self) -> None:
        # subset ordering: same set
        self.assertEqual(core.cmp_poset({1, 2}, {1, 2}), 0)

    def test_poset_less(self: Self) -> None:
        # subset ordering: strict subset
        self.assertEqual(core.cmp_poset({1}, {1, 2}), -1)

    def test_poset_greater(self: Self) -> None:
        # subset ordering: strict superset
        self.assertEqual(core.cmp_poset({1, 2}, {1}), 1)

    def test_poset_incomparable(self: Self) -> None:
        # incomparable in subset ordering
        res: Any
        res = core.cmp_poset({1}, {2})
        self.assertTrue(math.isnan(res))


if __name__ == "__main__":
    unittest.main()
