import { useEffect, useMemo, useState } from "react";
import {
  fetchBenchmark,
  fetchFibonacci,
  fetchRange,
  type AlgorithmName,
  type BenchmarkResponse,
  type FibonacciResponse,
  type RangeResponse,
} from "./api";
import {
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
  Bar,
  BarChart,
} from "recharts";

type LoadState = "idle" | "loading" | "error";

export default function App() {
  const [algorithm, setAlgorithm] = useState<AlgorithmName>("fast_doubling");
  const [n, setN] = useState(100);
  const [start, setStart] = useState(0);
  const [end, setEnd] = useState(20);
  const [optimizedPositiveRange, setOptimizedPositiveRange] = useState(false);

  const [singleValue, setSingleValue] = useState<FibonacciResponse | null>(null);
  const [rangeData, setRangeData] = useState<RangeResponse | null>(null);
  const [benchmarkData, setBenchmarkData] = useState<BenchmarkResponse | null>(null);

  const [singleState, setSingleState] = useState<LoadState>("idle");
  const [rangeState, setRangeState] = useState<LoadState>("idle");
  const [benchmarkState, setBenchmarkState] = useState<LoadState>("idle");
  const [errorMessage, setErrorMessage] = useState("");

  async function loadSingle(): Promise<void> {
    setSingleState("loading");
    setErrorMessage("");
    try {
      const data = await fetchFibonacci(n, algorithm);
      setSingleValue(data);
      setSingleState("idle");
    } catch (error) {
      setSingleState("error");
      setErrorMessage(error instanceof Error ? error.message : "Failed to load single value");
    }
  }

  async function loadRange(): Promise<void> {
    setRangeState("loading");
    setErrorMessage("");
    try {
      const data = await fetchRange(start, end, algorithm, optimizedPositiveRange);
      setRangeData(data);
      setRangeState("idle");
    } catch (error) {
      setRangeState("error");
      setErrorMessage(error instanceof Error ? error.message : "Failed to load range");
    }
  }

  async function loadBenchmark(): Promise<void> {
    setBenchmarkState("loading");
    setErrorMessage("");
    try {
      const data = await fetchBenchmark(Math.max(0, n));
      setBenchmarkData(data);
      setBenchmarkState("idle");
    } catch (error) {
      setBenchmarkState("error");
      setErrorMessage(error instanceof Error ? error.message : "Failed to load benchmark");
    }
  }

  useEffect(() => {
    void loadSingle();
    void loadRange();
    void loadBenchmark();
  }, []);

  const chartData = useMemo(() => {
    if (!rangeData) return [];
    return rangeData.indices.map((index, i) => ({
      index,
      value: Number(rangeData.values[i]),
    }));
  }, [rangeData]);

  const benchmarkChartData = useMemo(() => {
    return (benchmarkData?.results || []).map((item) => ({
      algorithm: item.algorithm,
      elapsed: item.elapsed_seconds,
    }));
  }, [benchmarkData]);

  return (
    <div className="page">
      <header className="hero">
        <div>
          <p className="eyebrow">Production Grade Full Stack Analytics</p>
          <h1>Fibonacci Analytics Platform</h1>
          <p className="subtext">
            Compare algorithms, inspect runtime tradeoffs, and visualize sequence behavior with a clean API and dashboard.
          </p>
        </div>
      </header>

      <section className="grid">
        <div className="card">
          <h2>Controls</h2>

          <label>Algorithm</label>
          <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value as AlgorithmName)}>
            <option value="iterative">iterative</option>
            <option value="fast_doubling">fast_doubling</option>
            <option value="matrix">matrix</option>
          </select>

          <label>Single value n</label>
          <input type="number" value={n} onChange={(e) => setN(Number(e.target.value))} />

          <button onClick={() => void loadSingle()}>Load single value</button>
          <button onClick={() => void loadBenchmark()}>Run benchmark</button>

          <hr />

          <label>Range start</label>
          <input type="number" value={start} onChange={(e) => setStart(Number(e.target.value))} />

          <label>Range end</label>
          <input type="number" value={end} onChange={(e) => setEnd(Number(e.target.value))} />

          <label className="checkbox">
            <input
              type="checkbox"
              checked={optimizedPositiveRange}
              onChange={(e) => setOptimizedPositiveRange(e.target.checked)}
            />
            Use optimized positive range
          </label>

          <button onClick={() => void loadRange()}>Load range</button>
        </div>

        <div className="card">
          <h2>Single value result</h2>
          {singleState === "loading" ? <p>Loading...</p> : null}
          {singleValue ? (
            <div className="statBlock">
              <div className="stat">
                <span className="label">n</span>
                <span className="value">{singleValue.n}</span>
              </div>
              <div className="stat">
                <span className="label">algorithm</span>
                <span className="value">{singleValue.algorithm}</span>
              </div>
              <div className="stat">
                <span className="label">digits</span>
                <span className="value">{singleValue.digits}</span>
              </div>
              <div className="monoBox">{singleValue.value}</div>
            </div>
          ) : null}
        </div>

        <div className="card wide">
          <h2>Sequence chart</h2>
          {rangeState === "loading" ? <p>Loading...</p> : null}
          <div className="chartWrap">
            <ResponsiveContainer width="100%" height={360}>
              <LineChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="index" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="value" name="Fibonacci" dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="card wide">
          <h2>Benchmark chart</h2>
          {benchmarkState === "loading" ? <p>Loading...</p> : null}
          <div className="chartWrap">
            <ResponsiveContainer width="100%" height={320}>
              <BarChart data={benchmarkChartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="algorithm" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="elapsed" name="elapsed seconds" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      {errorMessage ? <div className="errorBox">{errorMessage}</div> : null}
    </div>
  );
}
