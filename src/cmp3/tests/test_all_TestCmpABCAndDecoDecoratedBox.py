"""This module provides cmp3 functionality."""

import unittest
from typing import Any, Self

import setdoc

from cmp3.core.CmpABC import CmpABC
from cmp3.core.cmpDeco import cmpDeco

__all__ = ["TestCmpABCAndDecoDecoratedBox"]


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


class TestCmpABCAndDecoDecoratedBox(unittest.TestCase):
    def test_cmpabc_is_abstract(self: Self) -> None:
        with self.assertRaises(TypeError):
            CmpABC()  # type: ignore[abstract]  # must not be instantiable

    def test_cmpdeco_on_regular_class(self: Self) -> None:
        x: DecoratedBox
        y: DecoratedBox
        z: DecoratedBox
        x = DecoratedBox(10)
        y = DecoratedBox(20)
        z = DecoratedBox(10)

        self.assertTrue(x < y)  # type: ignore[operator]
        self.assertTrue(x <= y)  # type: ignore[operator]
        self.assertTrue(y > x)  # type: ignore[operator]
        self.assertTrue(y >= x)  # type: ignore[operator]
        self.assertTrue(x == z)
        self.assertTrue(x != y)


if __name__ == "__main__":
    unittest.main()
