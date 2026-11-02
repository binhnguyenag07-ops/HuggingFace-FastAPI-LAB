
import requests

BASE_URL = "http://127.0.0.1:8000"


def test_home():
    response = requests.get(
        f"{BASE_URL}/",
        timeout=10
    )

    assert response.status_code == 200
    print("[PASS] GET /")
    print(response.json())


def test_health():
    response = requests.get(
        f"{BASE_URL}/health",
        timeout=10
    )

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["model_loaded"] is True

    print("[PASS] GET /health")
    print(response.json())


def test_positive():
    response = requests.post(
        f"{BASE_URL}/predict",
        json={"text": "I love this movie!"},
        timeout=60
    )

    assert response.status_code == 200
    result = response.json()
    assert result["label"] == "POSITIVE"

    print("[PASS] Positive prediction")
    print(result)


def test_negative():
    response = requests.post(
        f"{BASE_URL}/predict",
        json={"text": "This movie is terrible!"},
        timeout=60
    )

    assert response.status_code == 200
    result = response.json()
    assert result["label"] == "NEGATIVE"

    print("[PASS] Negative prediction")
    print(result)


def test_empty_input():
    response = requests.post(
        f"{BASE_URL}/predict",
        json={"text": ""},
        timeout=10
    )

    assert response.status_code == 422

    print("[PASS] Empty input validation")
    print(response.json())


def test_missing_input():
    response = requests.post(
        f"{BASE_URL}/predict",
        json={},
        timeout=10
    )

    assert response.status_code == 422

    print("[PASS] Missing input validation")
    print(response.json())


if __name__ == "__main__":
    test_home()
    test_health()
    test_positive()
    test_negative()
    test_empty_input()
    test_missing_input()

    print("\nALL TESTS PASSED!")
