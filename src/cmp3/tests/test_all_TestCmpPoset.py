import math
import unittest
from typing import *

from cmp3.core import cmp_poset

__all__ = ["TestCmpPoset"]


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


if __name__ == "__main__":
    unittest.main()
