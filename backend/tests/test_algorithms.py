from app.algorithms import (
    fibonacci_fast_doubling,
    fibonacci_iterative,
    fibonacci_matrix,
    generate_positive_range_optimized,
    generate_range,
)


def test_known_positive_values() -> None:
    expected = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        10: 55,
    }
    for n, value in expected.items():
        assert fibonacci_iterative(n) == value
        assert fibonacci_fast_doubling(n) == value
        assert fibonacci_matrix(n) == value


def test_negative_values() -> None:
    expected = {
        -1: 1,
        -2: -1,
        -3: 2,
        -4: -3,
        -5: 5,
        -6: -8,
    }
    for n, value in expected.items():
        assert fibonacci_iterative(n) == value
        assert fibonacci_fast_doubling(n) == value
        assert fibonacci_matrix(n) == value


def test_range_generation() -> None:
    assert generate_range(0, 7, "fast_doubling") == [0, 1, 1, 2, 3, 5, 8]


def test_optimized_range() -> None:
    assert generate_positive_range_optimized(2, 7) == [1, 2, 3, 5, 8]
