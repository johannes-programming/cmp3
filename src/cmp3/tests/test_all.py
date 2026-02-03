import math
import unittest
from typing import *

from cmp3.core import CmpABC, cmp, cmp_poset, cmpDeco


class TestCmpFunction(unittest.TestCase):
    def test_portingguide_less(self: Self) -> None:
        self.assertEqual(cmp(1, 2), -1)
        self.assertEqual(cmp(-5, -1), -1)

    def test_portingguide_equal(self: Self) -> None:
        self.assertEqual(cmp(3, 3), 0)
        self.assertEqual(cmp("a", "a"), 0)

    def test_portingguide_greater(self: Self) -> None:
        self.assertEqual(cmp(2, 1), 1)
        self.assertEqual(cmp("b", "a"), 1)

    def test_poset_mode_uses_poset_semantics(self: Self) -> None:
        # For totally ordered ints, this should behave like normal cmp
        self.assertEqual(cmp(1, 2, mode="poset"), -1)
        self.assertEqual(cmp(2, 1, mode="poset"), 1)
        self.assertEqual(cmp(5, 5, mode="poset"), 0)

    def test_invalid_mode_raises(self: Self) -> None:
        with self.assertRaises(ValueError):
            cmp(1, 2, mode="something-else")


class TestCmpPoset(unittest.TestCase):
    def test_total_order_ints(self: Self) -> None:
        self.assertEqual(cmp_poset(1, 2), -1)
        self.assertEqual(cmp_poset(2, 1), 1)
        self.assertEqual(cmp_poset(3, 3), 0)

    def test_incomparable_returns_nan(self: Self) -> None:
        class Incomparable:
            def __le__(self: Self, other: Any) -> bool:
                # Always False, so no order relation is established
                return False

        result: Any
        x: Incomparable
        y: Incomparable

        x = Incomparable()
        y = Incomparable()
        result = cmp_poset(x, y)
        self.assertTrue(math.isnan(result))


# A concrete implementation of CmpABC for testing
class Box(CmpABC):
    def __init__(self: Self, value: Any) -> None:
        self.value = value

    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, Box):
            return NotImplemented
        return (self.value > other.value) - (self.value < other.value)


@cmpDeco
class DecoratedBox:
    def __init__(self: Self, value: Any) -> None:
        self.value = value

    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, DecoratedBox):
            return NotImplemented
        return (self.value > other.value) - (self.value < other.value)


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
