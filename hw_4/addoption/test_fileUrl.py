import pytest
import requests

def test_check_status(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}"