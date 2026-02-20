import unittest
from typing import *

import setdoc

from cmp3.core import CmpABC, cmpDeco

__all__ = ["TestCmpABCAndDeco"]


# A concrete implementation of CmpABC for testing
class Box(CmpABC):
    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, Box):
            return NotImplemented
        return (self.value > other.value) - (self.value < other.value)

    @setdoc.basic
    def __init__(self: Self, value: Any) -> None:
        self.value = value


@cmpDeco
class DecoratedBox:
    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, DecoratedBox):
            return NotImplemented
        return (self.value > other.value) - (self.value < other.value)

    @setdoc.basic
    def __init__(self: Self, value: Any) -> None:
        self.value = value


class TestCmpABCAndDeco(unittest.TestCase):
    def test_cmpabc_is_abstract(self: Self) -> None:
        with self.assertRaises(TypeError):
            CmpABC()  # type: ignore[abstract]  # must not be instantiable

    def test_cmpabc_comparisons(self: Self) -> None:
        a: Box
        b: Box
        c: Box
        a = Box(1)
        b = Box(2)
        c = Box(1)

        self.assertTrue(a < b)
        self.assertTrue(a <= b)
        self.assertTrue(b > a)
        self.assertTrue(b >= a)
        self.assertTrue(a == c)
        self.assertTrue(a != b)

    def test_cmpdeco_on_regular_class(self: Self) -> None:
        x: DecoratedBox
        y: DecoratedBox
        z: DecoratedBox
        x = DecoratedBox(10)
        y = DecoratedBox(20)
        z = DecoratedBox(10)

        self.assertTrue(x < y)
        self.assertTrue(x <= y)
        self.assertTrue(y > x)
        self.assertTrue(y >= x)
        self.assertTrue(x == z)
        self.assertTrue(x != y)


if __name__ == "__main__":
    unittest.main()
