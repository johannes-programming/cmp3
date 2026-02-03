import unittest
from typing import *

from cmp3 import core

__all__ = ["TestCmpDecoOnPlainClass"]


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
