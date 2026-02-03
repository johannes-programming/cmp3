import math
import unittest
from typing import *

from cmp3 import core


class TestCmpPortingGuide(unittest.TestCase):
    def test_equal(self: Self) -> None:
        self.assertEqual(core.cmp(1, 1), 0)
        self.assertEqual(core.cmp("a", "a"), 0)

    def test_less(self: Self) -> None:
        self.assertEqual(core.cmp(1, 2), -1)
        self.assertEqual(core.cmp("a", "b"), -1)

    def test_greater(self: Self) -> None:
        self.assertEqual(core.cmp(2, 1), 1)
        self.assertEqual(core.cmp("b", "a"), 1)

    def test_invalid_mode_raises(self: Self) -> None:
        with self.assertRaises(ValueError):
            core.cmp(1, 2, mode="invalid-mode")


class TestCmpPoset(unittest.TestCase):
    def test_poset_equal(self: Self) -> None:
        # subset ordering: same set
        self.assertEqual(core.cmp_poset({1, 2}, {1, 2}), 0)

    def test_poset_less(self: Self) -> None:
        # subset ordering: strict subset
        self.assertEqual(core.cmp_poset({1}, {1, 2}), -1)

    def test_poset_greater(self: Self) -> None:
        # subset ordering: strict superset
        self.assertEqual(core.cmp_poset({1, 2}, {1}), 1)

    def test_poset_incomparable(self: Self) -> None:
        # incomparable in subset ordering
        res = core.cmp_poset({1}, {2})
        self.assertTrue(math.isnan(res))


class TestCmpModePoset(unittest.TestCase):
    def test_cmp_uses_poset_mode(self: Self) -> None:
        self.assertEqual(core.cmp({1}, {1, 2}, mode="poset"), -1)
        self.assertEqual(core.cmp({1, 2}, {1}, mode="poset"), 1)
        self.assertTrue(math.isnan(core.cmp({1}, {2}, mode="poset")))


class Number(core.CmpABC):
    def __init__(self: Self, value: int) -> None:
        self.value = value

    def __cmp__(self: Self, other: Any) -> Any:
        if not isinstance(other, Number):
            return NotImplemented
        # classic 3-way comparison
        return (self.value > other.value) - (self.value < other.value)


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


class TestCmpDecoOnPlainClass(unittest.TestCase):
    def test_decorator_on_non_abc_class(self: Self) -> None:
        @core.cmpDeco
        class Plain:
            def __init__(self: Self, x: int) -> None:
                self.x = x

            def __cmp__(self: Self, other: Any) -> Any:
                if not isinstance(other, Plain):
                    return NotImplemented
                return (self.x > other.x) - (self.x < other.x)

        p1: Plain
        p2: Plain
        p3: Plain
        p1 = Plain(1)
        p2 = Plain(2)
        p3 = Plain(1)

        self.assertTrue(p1 < p2)
        self.assertTrue(p2 > p1)
        self.assertTrue(p1 == p3)
        self.assertTrue(p1 != p2)


if __name__ == "__main__":
    unittest.main()
