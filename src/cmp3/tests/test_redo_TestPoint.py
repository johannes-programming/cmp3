"""This module provides cmp3 functionality."""

import unittest
from types import NotImplementedType
from typing import Any, Self, cast

import setdoc

from cmp3.core.cmp import cmp_mode
from cmp3.core.CmpABC import CmpABC

__all__ = ["TestPoint"]


class Point(CmpABC):
    "This class is a simple comparable type based on an integer value."

    __slots__ = ("value",)

    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any:
        if isinstance(other, Point):
            return (self.value > other.value) - (self.value < other.value)
        else:
            return NotImplemented

    @setdoc.basic
    def __init__(self: Self, value: int) -> None:
        self.value = value


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
