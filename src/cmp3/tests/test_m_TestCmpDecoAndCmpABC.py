"""This module provides cmp3 functionality."""

import unittest
from typing import Any, Self

import setdoc

from cmp3.core.CmpABC import CmpABC

__all__ = ["TestCmpDecoAndCmpABC"]


class Number(CmpABC):
    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, Number):
            return NotImplemented
        return (self.value > other.value) - (self.value < other.value)

    @setdoc.basic
    def __init__(self: Self, value: int) -> None:
        self.value = value


class TestCmpDecoAndCmpABC(unittest.TestCase):
    def test_rich_comparisons_lt_gt(self: Self) -> None:
        a: Number
        b: Number
        a = Number(1)
        b = Number(2)
        self.assertTrue(a < b)
        self.assertTrue(b > a)

    def test_rich_comparisons_le_ge_eq(self: Self) -> None:
        a1: Number
        a2: Number
        b: Number
        a1 = Number(5)
        a2 = Number(5)
        b = Number(7)
        self.assertTrue(a1 <= a2)
        self.assertTrue(a1 >= a2)
        self.assertTrue(a1 == a2)
        self.assertTrue(a1 <= b)
        self.assertTrue(b >= a1)

    def test_rich_comparisons_ne(self: Self) -> None:
        a: Number
        b: Number
        a = Number(1)
        b = Number(2)
        self.assertTrue(a != b)
        self.assertFalse(a != Number(1))


if __name__ == "__main__":
    unittest.main()
