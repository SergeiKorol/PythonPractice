import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Choose browser: firefox, chrome, edge, yandex (default: chrome)")

@pytest.fixture()
def browser(request):

    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser name must be chrome, firefox, edge ")

    yield driver
    driver.quit()
