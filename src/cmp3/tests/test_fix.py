import unittest
from typing import Self

from cmp3.core.cmp import cmp

__all__ = ["TestFix"]


class TestFix(unittest.TestCase):

    def test_fix(self: Self) -> None:
        with self.assertRaises(ValueError):
            cmp(4, 2, mode="")
        with self.assertRaises(ValueError):
            cmp(4, 2, mode=" ")


if __name__ == "__main__":
    unittest.main()
