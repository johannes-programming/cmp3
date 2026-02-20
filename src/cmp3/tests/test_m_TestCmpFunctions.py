import math
import unittest
from typing import *

import setdoc

from cmp3 import core

__all__ = ["TestCmpFunctions"]


class Number(core.CmpABC):
    @setdoc.basic
    def __cmp__(self: Self, other) -> Any:
        if not isinstance(other, Number):
            return NotImplemented
        return (self.value > other.value) - (self.value < other.value)

    @setdoc.basic
    def __init__(self: Self, value: int) -> None:
        self.value = value


class TestCmpFunctions(unittest.TestCase):
    def test_eq_mode_equal(self: Self) -> None:
        self.assertEqual(core.cmp(1, 1, mode="eq"), 0)

    def test_eq_mode_not_equal(self: Self) -> None:
        result: Any
        result = core.cmp(1, 2, mode="eq")
        self.assertTrue(math.isnan(result))

    def test_eq_strict_mode_equal(self: Self) -> None:
        self.assertEqual(core.cmp(1, 1, mode="eq_strict"), 0)

    def test_eq_strict_mode_not_equal(self: Self) -> None:
        self.assertIsNone(core.cmp(1, 2, mode="eq_strict"))

    def test_portingguide_less(self: Self) -> None:
        self.assertEqual(core.cmp(1, 2, mode="portingguide"), -1)

    def test_portingguide_equal(self: Self) -> None:
        self.assertEqual(core.cmp(3, 3, mode="portingguide"), 0)

    def test_portingguide_greater(self: Self) -> None:
        self.assertEqual(core.cmp(5, 2, mode="portingguide"), 1)

    def test_le_mode(self: Self) -> None:
        # Using total-order ints to also test cmp_le
        self.assertEqual(core.cmp(1, 2, mode="le"), -1)
        self.assertEqual(core.cmp(2, 1, mode="le"), 1)
        self.assertEqual(core.cmp(3, 3, mode="le"), 0)

    def test_le_mode_nan_for_incomparable(self: Self) -> None:
        # Simulate incomparable with a custom class
        class P:
            def __init__(self, v):
                self.v = v

        x: P
        y: P
        x = P(1)
        y = P(2)
        # They don't define <=, so this should raise TypeError in cmp_le
        with self.assertRaises(TypeError):
            core.cmp_le(x, y)

    def test_magic_mode_with_cmpabc(self: Self) -> None:
        a: Number
        b: Number
        a = Number(1)
        b = Number(3)
        self.assertEqual(core.cmp(a, b, mode="magic"), -1)
        self.assertEqual(core.cmp(b, a, mode="magic"), 1)
        self.assertEqual(core.cmp(a, Number(1), mode="magic"), 0)

    def test_multi_mode_first_fails_second_succeeds(self: Self) -> None:
        # "magic" will work for Number, but let's create an object without __cmp__
        class NoCmp:
            pass

        x: NoCmp
        y: NoCmp

        x = NoCmp()
        y = NoCmp()
        with self.assertRaises(Exception):
            core.cmp(x, y, mode="magic portingguide")

    def test_unknown_modes_raise_exceptiongroup(self: Self) -> None:
        exc: Any
        with self.assertRaises(ExceptionGroup) as cm:
            core.cmp(1, 2, mode="foo bar")
        exc = cm.exception
        self.assertEqual(len(exc.exceptions), 2)
        self.assertTrue(all(isinstance(e, ValueError) for e in exc.exceptions))

    def test_only_whitespace_mode_raises_valueerror(self: Self) -> None:
        with self.assertRaises(ValueError):
            core.cmp(1, 2, mode="   ")


if __name__ == "__main__":
    unittest.main()
