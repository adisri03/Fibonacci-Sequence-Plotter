const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || "").replace(/\/$/, "");

export type AlgorithmName = "iterative" | "fast_doubling" | "matrix";

export interface FibonacciResponse {
  n: number;
  algorithm: AlgorithmName;
  value: string;
  digits: number;
}

export interface RangeResponse {
  start: number;
  end: number;
  algorithm: string;
  indices: number[];
  values: string[];
}

export interface BenchmarkItem {
  algorithm: string;
  elapsed_seconds: number;
  digits: number;
}

export interface BenchmarkResponse {
  n: number;
  results: BenchmarkItem[];
}

async function getJson<T>(path: string): Promise<T> {
  if (!API_BASE_URL) {
    throw new Error("VITE_API_BASE_URL is missing");
  }

  const response = await fetch(`${API_BASE_URL}${path}`);
  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || "Request failed");
  }
  return response.json() as Promise<T>;
}

export function fetchFibonacci(n: number, algorithm: AlgorithmName): Promise<FibonacciResponse> {
  return getJson(`/api/v1/fibonacci?n=${n}&algorithm=${algorithm}`);
}

export function fetchRange(
  start: number,
  end: number,
  algorithm: AlgorithmName,
  optimizedPositiveRange: boolean
): Promise<RangeResponse> {
  return getJson(
    `/api/v1/range?start=${start}&end=${end}&algorithm=${algorithm}&optimized_positive_range=${optimizedPositiveRange}`
  );
}

export function fetchBenchmark(n: number): Promise<BenchmarkResponse> {
  return getJson(`/api/v1/benchmark?n=${n}`);
}
