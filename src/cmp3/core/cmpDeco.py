from collections.abc import Callable
from functools import wraps
from typing import Any, Final, TypeVar

from tofunc import tofunc

from ..core.CmpABC import CmpABC

__all__ = ["cmpDeco"]


Target = TypeVar("Target")

NAMES: Final[tuple[str, ...]] = (
    "__eq__",
    "__ge__",
    "__gt__",
    "__le__",
    "__lt__",
    "__ne__",
)


def cmpDeco(cls: type[Target], /) -> type[Target]:
    "This decorator enforces the use of __cmp__ upon a class."
    name: str
    new: Callable[[Any, Any], Any]
    old: Callable[[Any, Any], Any]
    for name in NAMES:
        old = getattr(CmpABC, name)
        new = wraps(old)(tofunc(old))
        try:
            new.__module__ = cls.__module__
        except AttributeError:
            pass
        try:
            new.__qualname__ = f"{cls.__qualname__}.{name}"
        except AttributeError:
            pass
        setattr(cls, name, new)
    return cls
