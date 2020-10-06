import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--app_host", default="http://10.20.30.57")
    parser.addoption("--executor", default="10.20.30.57")


@pytest.fixture
def browserm(request):

    bro = request.config.getoption("--browser")
    app_host = request.config.getoption("--app_host")
    executor = request.config.getoption("--executor")

    caps = {"browserName": bro}

    wd = webdriver.Remote(command_executor=f"http://{executor}:4445/wd/hub", desired_capabilities=caps)
    request.addfinalizer(wd.quit)
    wd.get(app_host)
    return wd

