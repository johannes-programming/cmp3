from functools import partial
from typing import *

import setdoc

__all__ = ["Comparable", "comparable"]


def comparable(*, overwrite: Any = False) -> type:
    return partial(update, overwrite=overwrite)


def update(cls: type, /, *, overwrite: Any = False) -> type:
    @setdoc.basic
    def __eq__(self: Self, other: Any) -> bool:
        return self.__cmp__(other) == 0

    @setdoc.basic
    def __ge__(self: Self, other: Any) -> bool:
        return self.__cmp__(other) >= 0

    @setdoc.basic
    def __gt__(self: Self, other: Any) -> bool:
        return self.__cmp__(other) > 0

    @setdoc.basic
    def __le__(self: Self, other: Any) -> bool:
        return self.__cmp__(other) <= 0

    @setdoc.basic
    def __lt__(self: Self, other: Any) -> bool:
        return self.__cmp__(other) < 0

    @setdoc.basic
    def __ne__(self: Self, other: Any) -> bool:
        return self.__cmp__(other) != 0

    func: Callable
    funcs: list[Callable]
    funcs = [
        __eq__,
        __ge__,
        __gt__,
        __le__,
        __lt__,
        __ne__,
    ]
    for func in funcs:
        if overwrite or not hasattr(cls, func.__name__):
            setattr(cls, func.__name__, func)
    return cls


@comparable()
class Comparable:
    __slots__ = ()
