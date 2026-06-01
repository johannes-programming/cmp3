import math
import unittest
from typing import Any, Self

import setdoc

from cmp3.core.cmp import cmp_le, cmp_mode

__all__ = ["TestIncomparable"]


class Incomparable:
    "This class is a type whose instances are never <= each other."

    @setdoc.basic
    def __le__(self: Self, other: Any) -> bool:
        return False


class TestIncomparable(unittest.TestCase):
    def test_portingguide_ints(self: Self) -> None:
        self.assertEqual(cmp_mode(1, 1, mode="portingguide"), 0)
        self.assertEqual(cmp_mode(2, 1, mode="portingguide"), 1)
        self.assertEqual(cmp_mode(1, 2, mode="portingguide"), -1)

    def test_equality_mode(self: Self) -> None:
        self.assertEqual(cmp_mode(10, 10, mode="eq_strict"), 0)
        self.assertIsNone(cmp_mode(10, 11, mode="eq_strict"))

    def test_poset_total_order_ints(self: Self) -> None:
        self.assertEqual(cmp_le(1, 1), 0)
        self.assertEqual(cmp_le(1, 2), -1)
        self.assertEqual(cmp_le(2, 1), 1)

    def test_poset_incomparable(self: Self) -> None:
        result: object
        x: Incomparable
        y: Incomparable
        x = Incomparable()
        y = Incomparable()
        result = cmp_le(x, y)
        self.assertTrue(math.isnan(result))

    def test_cmp_mode_invalid_raises(self: Self) -> None:
        with self.assertRaises(ValueError):
            cmp_mode(1, 2, mode="not-a-mode")


if __name__ == "__main__":
    unittest.main()
