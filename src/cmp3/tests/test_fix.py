"""This module provides cmp3 functionality."""

__all__: list[str] = ["TestFix"]

import unittest
from typing import Self

from cmp3.core.cmp import cmp


class TestFix(unittest.TestCase):

    def test_fix(self: Self) -> None:
        with self.assertRaises(ValueError):
            cmp(4, 2, mode="")
        with self.assertRaises(ValueError):
            cmp(4, 2, mode=" ")


if __name__ == "__main__":
    unittest.main()
