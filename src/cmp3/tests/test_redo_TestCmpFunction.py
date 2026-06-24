"""This module provides cmp3 functionality."""

import unittest
from typing import Self

from cmp3.core.cmp import cmp

__all__ = ["TestCmpFunction"]


class TestCmpFunction(unittest.TestCase):
    def test_default_mode_is_portingguide(self: Self) -> None:
        self.assertEqual(cmp(1, 1), 0)
        self.assertEqual(cmp(2, 1), 1)
        self.assertEqual(cmp(1, 2), -1)

    def test_mode_without_whitespace_goes_directly_to_cmp_mode(
        self: Self,
    ) -> None:
        # Just checks result; behavior should match portingguide
        self.assertEqual(cmp(3, 4, mode="portingguide"), -1)

    def test_whitespace_modes_first_successful_used(self: Self) -> None:
        # "portingguide" works; "equality" would give None instead
        self.assertEqual(cmp(1, 2, mode="portingguide eq_strict"), -1)

    def test_whitespace_modes_falls_back_on_exception(self: Self) -> None:
        # int has no __cmp__, so "dunder" fails, then "portingguide" works
        self.assertEqual(cmp(1, 2, mode="magic portingguide"), -1)

    def test_whitespace_modes_all_fail_raise_exceptiongroup(
        self: Self,
    ) -> None:
        exc: ExceptionGroup
        # For int vs str, "dunder", "poset", and "portingguide" all raise
        with self.assertRaises(ExceptionGroup) as cm:
            cmp(1, "a", mode="magic le portingguide")
        exc = cm.exception
        # There should be one sub-exception per submode
        self.assertEqual(len(exc.exceptions), 3)


if __name__ == "__main__":
    unittest.main()
