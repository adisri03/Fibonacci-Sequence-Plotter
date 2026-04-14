from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


AlgorithmName = Literal["iterative", "fast_doubling", "matrix"]


class FibonacciResponse(BaseModel):
    n: int
    algorithm: AlgorithmName
    value: str
    digits: int


class RangeResponse(BaseModel):
    start: int
    end: int
    algorithm: str
    indices: list[int]
    values: list[str]


class BenchmarkItem(BaseModel):
    algorithm: str
    elapsed_seconds: float = Field(..., ge=0)
    digits: int


class BenchmarkResponse(BaseModel):
    n: int
    results: list[BenchmarkItem]


class HealthResponse(BaseModel):
    status: str
