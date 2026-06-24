"""This module provides cmp3 functionality."""

from typing import Any

__all__ = ["cmp"]


def cmp(x: Any, y: Any, /, *, mode: str = "portingguide") -> Any:
    "This function returns a value that compares to 0 as x compares to y."
    errors: list[Exception]
    part: str
    if not any(map(str.isspace, mode)):
        return cmp_mode(x, y, mode=mode)
    errors = list()
    for part in mode.split():
        try:
            return cmp_mode(x, y, mode=part)
        except Exception as exc:
            errors.append(exc)
    if len(errors):
        raise ExceptionGroup("No submode worked.", errors)
    else:
        raise ValueError("No submodes provided.")


def cmp_mode(x: Any, y: Any, /, *, mode: str) -> Any:
    "This function implements submodes."
    if mode == "eq":
        return 0 if x == y else float("nan")
    if mode == "eq_strict":
        return 0 if x == y else None
    if mode == "le":
        return cmp_le(x, y)
    if mode == "magic":
        return x.__cmp__(y)
    if mode == "portingguide":
        return (x > y) - (x < y)
    raise ValueError("%r is not a recognized mode." % mode)


def cmp_le(x: Any, y: Any, /) -> float | int:
    "This function returns a value that compares to 0 as x compares to y assuming a partial order."
    if x <= y:
        if y <= x:
            return 0
        else:
            return -1
    else:
        if y <= x:
            return 1
        else:
            return float("nan")
