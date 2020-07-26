import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get"],
        help="method to execute"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="status code"
    )


@pytest.fixture
def url_status(request):
    return request.config.getoption("--url")


@pytest.fixture
def method_get(request):
    m = request.config.getoption("--method")
    if m == "get":
        return requests.get


@pytest.fixture
def method_status_code(request):
    return request.config.getoption("--status_code")