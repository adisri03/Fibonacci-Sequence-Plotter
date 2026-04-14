from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_fibonacci_endpoint() -> None:
    response = client.get("/api/v1/fibonacci", params={"n": 10, "algorithm": "fast_doubling"})
    assert response.status_code == 200
    data = response.json()
    assert data["value"] == "55"
    assert data["digits"] == 2


def test_range_endpoint() -> None:
    response = client.get("/api/v1/range", params={"start": 0, "end": 6, "algorithm": "matrix"})
    assert response.status_code == 200
    data = response.json()
    assert data["values"] == ["0", "1", "1", "2", "3", "5"]


def test_benchmark_endpoint() -> None:
    response = client.get("/api/v1/benchmark", params={"n": 100})
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) == 3
