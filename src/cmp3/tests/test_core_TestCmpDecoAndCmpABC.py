import unittest
from typing import Any, Self

import setdoc

from cmp3.core.CmpABC import CmpABC

__all__ = ["TestCmpDecoAndCmpABC"]


class Number(CmpABC):
    value: int

    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, Number):
            return NotImplemented
        # classic 3-way comparison
        return (self.value > other.value) - (self.value < other.value)

    @setdoc.basic
    def __init__(self: Self, value: int) -> None:
        self.value = value


class TestCmpDecoAndCmpABC(unittest.TestCase):

    def test_eq_ne(self: Self) -> None:
        a: Number
        b: Number
        c: Number
        a = Number(1)
        b = Number(2)
        c = Number(1)
        self.assertTrue(a == c)
        self.assertFalse(a == b)
        self.assertTrue(a != b)
        self.assertFalse(a != c)

    def test_lt_le(self: Self) -> None:
        a: Number
        b: Number
        c: Number
        a = Number(1)
        b = Number(2)
        c = Number(1)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)
        self.assertTrue(a <= c)
        self.assertFalse(b < a)

    def test_gt_ge(self: Self) -> None:
        a: Number
        b: Number
        c: Number
        a = Number(1)
        b = Number(2)
        c = Number(1)
        self.assertTrue(b > a)
        self.assertTrue(b >= a)
        self.assertTrue(b >= c)
        self.assertFalse(a > b)

    def test_cmpabc_is_abstract(self: Self) -> None:
        with self.assertRaises(TypeError):
            CmpABC()  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
