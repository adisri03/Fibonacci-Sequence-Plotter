from __future__ import annotations

import time

from .algorithms import (
    fibonacci_fast_doubling,
    fibonacci_iterative,
    fibonacci_matrix,
    generate_positive_range_optimized,
    generate_range,
)
from .schemas import BenchmarkItem


def get_fibonacci_value(n: int, algorithm: str) -> int:
    if algorithm == "iterative":
        return fibonacci_iterative(n)
    if algorithm == "fast_doubling":
        return fibonacci_fast_doubling(n)
    if algorithm == "matrix":
        return fibonacci_matrix(n)
    raise ValueError(f"Unsupported algorithm: {algorithm}")


def get_range(start: int, end: int, algorithm: str, optimized_positive_range: bool = False) -> list[int]:
    if optimized_positive_range:
        return generate_positive_range_optimized(start, end)
    return generate_range(start, end, algorithm)


def benchmark(n: int) -> list[BenchmarkItem]:
    algorithms = {
        "iterative": fibonacci_iterative,
        "fast_doubling": fibonacci_fast_doubling,
        "matrix": fibonacci_matrix,
    }

    results: list[BenchmarkItem] = []
    for name, fn in algorithms.items():
        started = time.perf_counter()
        value = fn(n)
        elapsed = time.perf_counter() - started
        results.append(
            BenchmarkItem(
                algorithm=name,
                elapsed_seconds=elapsed,
                digits=len(str(value)),
            )
        )

    return sorted(results, key=lambda item: item.elapsed_seconds)
