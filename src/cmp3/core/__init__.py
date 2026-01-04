from abc import ABC, abstractmethod
from functools import partial
from typing import *

import setdoc

__all__ = ["Comparable", "comparable", "update_rich_cmp"]


def comparable(*, overwrites: Any = False) -> partial:
    "This function returns a decorator."
    return partial(update_rich_cmp, overwrites=overwrites)


def update_rich_cmp(cls: type, /, *, overwrites: Any = False) -> type:
    @setdoc.basic
    def __eq__(self: Self, other: Any) -> Any:
        return self.__cmp__(other) == 0

    @setdoc.basic
    def __ge__(self: Self, other: Any) -> Any:
        return self.__cmp__(other) >= 0

    @setdoc.basic
    def __gt__(self: Self, other: Any) -> Any:
        return self.__cmp__(other) > 0

    @setdoc.basic
    def __le__(self: Self, other: Any) -> Any:
        return self.__cmp__(other) <= 0

    @setdoc.basic
    def __lt__(self: Self, other: Any) -> Any:
        return self.__cmp__(other) < 0

    @setdoc.basic
    def __ne__(self: Self, other: Any) -> Any:
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
        if hasattr(cls, func.__name__) and not overwrites:
            continue
        setattr(cls, func.__name__, func)
        try:
            func.__module__ = cls.__module__
        except AttributeError:
            pass
        try:
            func.__qualname__ = cls.__qualname__
        except AttributeError:
            pass
    return cls


@comparable()
class Comparable(ABC):
    __slots__ = ()

    @abstractmethod
    def __cmp__(self: Self, other: Any) -> Any: ...
