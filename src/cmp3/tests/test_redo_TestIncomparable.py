import math
import unittest
from typing import *

from cmp3.core import CmpABC, cmp_le, cmp_mode

__all__ = ["TestIncomparable"]


class Incomparable:
    """Type whose instances are never <= each other."""

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


class Point(CmpABC):
    """Simple comparable type based on an integer value."""

    __slots__ = ("value",)

    def __init__(self: Self, value: int) -> None:
        self.value = value

    def __cmp__(self: Self, other: Any) -> int:
        if isinstance(other, Point):
            return (self.value > other.value) - (self.value < other.value)
        return NotImplemented


class TestPoint(unittest.TestCase):

    def test_dunder_mode_uses___cmp__(self: Self) -> None:
        a: Point
        b: Point

        a = Point(1)
        b = Point(2)
        self.assertEqual(cmp_mode(a, b, mode="magic"), -1)
        self.assertEqual(cmp_mode(b, a, mode="magic"), 1)
        self.assertEqual(cmp_mode(a, a, mode="magic"), 0)

    def test_cmpabc_is_abstract(self: Self) -> None:
        with self.assertRaises(TypeError):
            CmpABC()  # type: ignore[abstract]

    def test_cmpabc_slots(self: Self) -> None:
        self.assertEqual(CmpABC.__slots__, ())

    def test_subclass_comparisons_use___cmp__(self: Self) -> None:
        a: Point
        b: Point
        c: Point
        a = Point(1)
        b = Point(2)
        c = Point(1)

        self.assertTrue(a < b)
        self.assertTrue(a <= b)
        self.assertTrue(b > a)
        self.assertTrue(b >= a)
        self.assertTrue(a == c)
        self.assertTrue(a != b)

        self.assertFalse(a > b)
        self.assertFalse(a >= b)
        self.assertFalse(b < a)
        self.assertFalse(b <= a)
        self.assertFalse(a != c)
        self.assertFalse(a == b)

    def test_cmpdeco_adds_comparison_methods(self: Self) -> None:
        self.assertTrue(hasattr(Point, "__eq__"))
        self.assertTrue(hasattr(Point, "__lt__"))
        self.assertTrue(hasattr(Point, "__le__"))
        self.assertTrue(hasattr(Point, "__gt__"))
        self.assertTrue(hasattr(Point, "__ge__"))
        self.assertTrue(hasattr(Point, "__ne__"))


if __name__ == "__main__":
    unittest.main()
