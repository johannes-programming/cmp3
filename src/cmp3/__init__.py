"""This module exposes the public API of cmp3."""

__all__: list[str] = [
    "CmpABC",
    "cmp",
    "cmpDeco",
]

from cmp3.core.cmp import cmp
from cmp3.core.CmpABC import CmpABC
from cmp3.core.cmpDeco import cmpDeco
