
import requests

URL = "http://127.0.0.1:8000/predict"


def check_case(name, response, expected_status=422):
    assert response.status_code == expected_status, (
        f"{name}: Expected {expected_status}, "
        f"got {response.status_code}: {response.text}"
    )

    print(f"[PASS] {name} - HTTP {response.status_code}")


# Test 1: Input chỉ chứa khoảng trắng
response = requests.post(
    URL,
    json={"text": "   "},
    timeout=10
)
check_case("Whitespace input", response)


# Test 2: Input sai kiểu dữ liệu
response = requests.post(
    URL,
    json={"text": 12345},
    timeout=10
)
check_case("Invalid data type", response)


# Test 3: Input vượt giới hạn 2000 ký tự
response = requests.post(
    URL,
    json={"text": "A" * 2001},
    timeout=10
)
check_case("Text too long", response)


# Test 4: JSON không hợp lệ
response = requests.post(
    URL,
    data='{"text":',
    headers={"Content-Type": "application/json"},
    timeout=10
)
check_case("Malformed JSON", response)


print("\nALL VALIDATION TESTS PASSED!")
