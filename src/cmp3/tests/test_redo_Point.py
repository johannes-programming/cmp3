import unittest
from typing import *

from cmp3.core import CmpABC, cmp_mode

__all__ = ["TestPoint"]


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
        self.assertEqual(cmp_mode(a, b, mode="dunder"), -1)
        self.assertEqual(cmp_mode(b, a, mode="dunder"), 1)
        self.assertEqual(cmp_mode(a, a, mode="dunder"), 0)

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
