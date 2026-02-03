import unittest
from typing import *

import setdoc

from cmp3 import core

__all__ = ["TestCmpDecoAndCmpABC"]


class Number(core.CmpABC):
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
    def setUp(self: Self) -> None:
        self.a = Number(1)
        self.b = Number(2)
        self.c = Number(1)

    def test_eq_ne(self: Self) -> None:
        self.assertTrue(self.a == self.c)
        self.assertFalse(self.a == self.b)
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.a != self.c)

    def test_lt_le(self: Self) -> None:
        self.assertTrue(self.a < self.b)
        self.assertTrue(self.a <= self.b)
        self.assertTrue(self.a <= self.c)
        self.assertFalse(self.b < self.a)

    def test_gt_ge(self: Self) -> None:
        self.assertTrue(self.b > self.a)
        self.assertTrue(self.b >= self.a)
        self.assertTrue(self.b >= self.c)
        self.assertFalse(self.a > self.b)

    def test_cmpabc_is_abstract(self: Self) -> None:
        with self.assertRaises(TypeError):
            core.CmpABC()  # abstract, cannot be instantiated


if __name__ == "__main__":
    unittest.main()
