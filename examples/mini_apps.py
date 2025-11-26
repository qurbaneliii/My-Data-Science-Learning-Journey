"""Reusable mini applications extracted from notebooks.

Each function encapsulates logic originally shown in interactive cells so they can be
imported, tested, and reused. The implementations avoid side effects (I/O) unless
explicitly needed. For learning purposes only.
"""
from typing import Iterable, List, Sequence


def calculate(a: float, b: float, operator: str) -> float:
    """Perform a basic arithmetic operation.

    Supported operators: +, -, *, /.
    Raises ValueError for invalid operator or division by zero.
    """
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    raise ValueError(f"Unsupported operator: {operator}")


def grade_converter(score: int) -> str:
    """Convert numeric score (0–100) to letter grade."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def filter_even(numbers: Iterable[int]) -> List[int]:
    """Return even numbers from the iterable."""
    return [n for n in numbers if n % 2 == 0]


def classify_sign(numbers: Iterable[int]) -> List[str]:
    """Classify integers as 'positive', 'negative', or 'zero'."""
    result: List[str] = []
    for n in numbers:
        if n > 0:
            result.append("positive")
        elif n < 0:
            result.append("negative")
        else:
            result.append("zero")
    return result


def filter_by_word_length(words: Sequence[str], min_len: int) -> List[str]:
    """Return words with length >= min_len."""
    return [w for w in words if len(w) >= min_len]


def swap_values(a, b):
    """Return values swapped. Demonstrates tuple unpacking."""
    return b, a

__all__ = [
    "calculate",
    "grade_converter",
    "filter_even",
    "classify_sign",
    "filter_by_word_length",
    "swap_values",
]
