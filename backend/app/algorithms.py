from __future__ import annotations

from typing import Callable, Tuple


def _negafib_sign(n: int) -> int:
    abs_n = abs(n)
    return 1 if abs_n % 2 == 1 else -1


def fibonacci_iterative(n: int) -> int:
    if n == 0:
        return 0

    abs_n = abs(n)
    a, b = 0, 1
    for _ in range(abs_n):
        a, b = b, a + b

    if n > 0:
        return a
    return _negafib_sign(n) * a


def _fast_doubling_core(n: int) -> Tuple[int, int]:
    if n == 0:
        return 0, 1

    a, b = _fast_doubling_core(n // 2)
    c = a * ((2 * b) - a)
    d = a * a + b * b

    if n % 2 == 0:
        return c, d
    return d, c + d


def fibonacci_fast_doubling(n: int) -> int:
    if n == 0:
        return 0

    abs_n = abs(n)
    value, _ = _fast_doubling_core(abs_n)

    if n > 0:
        return value
    return _negafib_sign(n) * value


def _matrix_multiply(
    a: tuple[tuple[int, int], tuple[int, int]],
    b: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def _matrix_power(
    matrix: tuple[tuple[int, int], tuple[int, int]],
    exponent: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    result = ((1, 0), (0, 1))
    base = matrix
    exp = exponent

    while exp > 0:
        if exp % 2 == 1:
            result = _matrix_multiply(result, base)
        base = _matrix_multiply(base, base)
        exp //= 2

    return result


def fibonacci_matrix(n: int) -> int:
    if n == 0:
        return 0

    abs_n = abs(n)
    q_matrix = ((1, 1), (1, 0))
    powered = _matrix_power(q_matrix, abs_n - 1)
    value = powered[0][0]

    if n > 0:
        return value
    return _negafib_sign(n) * value


def get_algorithm(name: str) -> Callable[[int], int]:
    algorithms: dict[str, Callable[[int], int]] = {
        "iterative": fibonacci_iterative,
        "fast_doubling": fibonacci_fast_doubling,
        "matrix": fibonacci_matrix,
    }
    if name not in algorithms:
        raise ValueError(f"Unsupported algorithm: {name}")
    return algorithms[name]


def generate_range(start: int, end: int, algorithm: str) -> list[int]:
    if start >= end:
        raise ValueError("start must be less than end")
    fib = get_algorithm(algorithm)
    return [fib(i) for i in range(start, end)]


def generate_positive_range_optimized(start: int, end: int) -> list[int]:
    if start < 0 or end < 0:
        raise ValueError("optimized range requires non negative indices")
    if start >= end:
        raise ValueError("start must be less than end")

    if end == 1:
        return [0] if start == 0 else []

    values = [0, 1]
    while len(values) < end:
        values.append(values[-1] + values[-2])
    return values[start:end]
