"""This module provides cmp3 functionality."""

from abc import ABC, abstractmethod
from typing import Any, Self

import setdoc

__all__ = ["CmpABC", "cmp", "cmpDeco"]


class CmpABC(ABC):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any: ...

    @setdoc.basic
    def __eq__(self: Self, other: object) -> Any:
        return self.__cmp__(other).__eq__(0)

    @setdoc.basic
    def __ge__(self: Self, other: Any) -> Any:
        return self.__cmp__(other).__ge__(0)

    @setdoc.basic
    def __gt__(self: Self, other: Any) -> Any:
        return self.__cmp__(other).__gt__(0)

    @setdoc.basic
    def __le__(self: Self, other: Any) -> Any:
        return self.__cmp__(other).__le__(0)

    @setdoc.basic
    def __lt__(self: Self, other: Any) -> Any:
        return self.__cmp__(other).__lt__(0)

    @setdoc.basic
    def __ne__(self: Self, other: object) -> Any:
        return self.__cmp__(other).__ne__(0)
