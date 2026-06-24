"""This module provides cmp3 functionality."""

import unittest
from typing import Self

from cmp3.core.cmp import cmp

__all__ = ["TestCmpPortingGuide"]


class TestCmpPortingGuide(unittest.TestCase):
    def test_equal(self: Self) -> None:
        self.assertEqual(cmp(1, 1), 0)
        self.assertEqual(cmp("a", "a"), 0)

    def test_less(self: Self) -> None:
        self.assertEqual(cmp(1, 2), -1)
        self.assertEqual(cmp("a", "b"), -1)

    def test_greater(self: Self) -> None:
        self.assertEqual(cmp(2, 1), 1)
        self.assertEqual(cmp("b", "a"), 1)

    def test_invalid_mode_raises(self: Self) -> None:
        with self.assertRaises(ValueError):
            cmp(1, 2, mode="invalid-mode")


if __name__ == "__main__":
    unittest.main()
