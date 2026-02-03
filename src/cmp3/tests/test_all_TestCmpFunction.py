import unittest
from typing import *

from cmp3.core import cmp

__all__ = ["TestCmpFunction"]


class TestCmpFunction(unittest.TestCase):
    def test_portingguide_less(self: Self) -> None:
        self.assertEqual(cmp(1, 2), -1)
        self.assertEqual(cmp(-5, -1), -1)

    def test_portingguide_equal(self: Self) -> None:
        self.assertEqual(cmp(3, 3), 0)
        self.assertEqual(cmp("a", "a"), 0)

    def test_portingguide_greater(self: Self) -> None:
        self.assertEqual(cmp(2, 1), 1)
        self.assertEqual(cmp("b", "a"), 1)

    def test_poset_mode_uses_poset_semantics(self: Self) -> None:
        # For totally ordered ints, this should behave like normal cmp
        self.assertEqual(cmp(1, 2, mode="le"), -1)
        self.assertEqual(cmp(2, 1, mode="le"), 1)
        self.assertEqual(cmp(5, 5, mode="le"), 0)

    def test_invalid_mode_raises(self: Self) -> None:
        with self.assertRaises(ValueError):
            cmp(1, 2, mode="something-else")


if __name__ == "__main__":
    unittest.main()
