import unittest
from typing import *

from cmp3.core import cmp as cmp_fn

__all__ = ["TestCmpFunction"]


class TestCmpFunction(unittest.TestCase):
    def test_default_mode_is_portingguide(self: Self) -> None:
        self.assertEqual(cmp_fn(1, 1), 0)
        self.assertEqual(cmp_fn(2, 1), 1)
        self.assertEqual(cmp_fn(1, 2), -1)

    def test_mode_without_whitespace_goes_directly_to_cmp_mode(self: Self) -> None:
        # Just checks result; behavior should match portingguide
        self.assertEqual(cmp_fn(3, 4, mode="portingguide"), -1)

    def test_whitespace_modes_first_successful_used(self: Self) -> None:
        # "portingguide" works; "equality" would give None instead
        self.assertEqual(cmp_fn(1, 2, mode="portingguide equality"), -1)

    def test_whitespace_modes_falls_back_on_exception(self: Self) -> None:
        # int has no __cmp__, so "dunder" fails, then "portingguide" works
        self.assertEqual(cmp_fn(1, 2, mode="dunder portingguide"), -1)

    def test_whitespace_modes_all_fail_raise_exceptiongroup(self: Self) -> None:
        exc: ExceptionGroup
        # For int vs str, "dunder", "poset", and "portingguide" all raise
        with self.assertRaises(ExceptionGroup) as cm:
            cmp_fn(1, "a", mode="dunder poset portingguide")

        exc = cm.exception
        # First argument is the message given to ExceptionGroup
        self.assertEqual(exc.args[0], "No submode worked.")
        # There should be one sub-exception per submode
        self.assertEqual(len(exc.exceptions), 3)


if __name__ == "__main__":
    unittest.main()
