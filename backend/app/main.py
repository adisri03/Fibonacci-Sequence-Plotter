from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from .schemas import BenchmarkResponse, FibonacciResponse, HealthResponse, RangeResponse
from .service import benchmark, get_fibonacci_value, get_range

app = FastAPI(
    title="Fibonacci Analytics API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/api/v1/fibonacci", response_model=FibonacciResponse)
def fibonacci(
    n: int = Query(..., description="Index of Fibonacci number"),
    algorithm: str = Query("fast_doubling", pattern="^(iterative|fast_doubling|matrix)$"),
) -> FibonacciResponse:
    try:
        value = get_fibonacci_value(n, algorithm)
        return FibonacciResponse(
            n=n,
            algorithm=algorithm,
            value=str(value),
            digits=len(str(value)),
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/api/v1/range", response_model=RangeResponse)
def fibonacci_range(
    start: int = Query(0),
    end: int = Query(20),
    algorithm: str = Query("fast_doubling", pattern="^(iterative|fast_doubling|matrix)$"),
    optimized_positive_range: bool = Query(False),
) -> RangeResponse:
    try:
        values = get_range(start, end, algorithm, optimized_positive_range=optimized_positive_range)
        return RangeResponse(
            start=start,
            end=end,
            algorithm="optimized_positive_range" if optimized_positive_range else algorithm,
            indices=list(range(start, end)),
            values=[str(v) for v in values],
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/api/v1/benchmark", response_model=BenchmarkResponse)
def run_benchmark(
    n: int = Query(..., ge=0),
) -> BenchmarkResponse:
    results = benchmark(n)
    return BenchmarkResponse(n=n, results=results)
