import math
import unittest
from typing import *

import setdoc

from cmp3.core import cmp

__all__ = ["TestCmpPoset"]


class TestCmpPoset(unittest.TestCase):
    def test_total_order_ints(self: Self) -> None:
        self.assertEqual(cmp(1, 2, mode="le"), -1)
        self.assertEqual(cmp(2, 1, mode="le"), 1)
        self.assertEqual(cmp(3, 3, mode="le"), 0)

    def test_incomparable_returns_nan(self: Self) -> None:
        class Incomparable:
            @setdoc.basic
            def __le__(self: Self, other: Any) -> bool:
                # Always False, so no order relation is established
                return False

        result: Any
        x: Incomparable
        y: Incomparable

        x = Incomparable()
        y = Incomparable()
        result = cmp(x, y, mode="le")
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()
