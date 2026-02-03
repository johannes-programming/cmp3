import math
import unittest
from typing import *

from cmp3 import core

__all__ = ["TestCmpModePoset"]


class TestCmpModePoset(unittest.TestCase):
    def test_cmp_uses_poset_mode(self: Self) -> None:
        self.assertEqual(core.cmp({1}, {1, 2}, mode="poset"), -1)
        self.assertEqual(core.cmp({1, 2}, {1}, mode="poset"), 1)
        self.assertTrue(math.isnan(core.cmp({1}, {2}, mode="poset")))


if __name__ == "__main__":
    unittest.main()
