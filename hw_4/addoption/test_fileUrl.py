import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="Expected status code"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

def test_check_status(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}"