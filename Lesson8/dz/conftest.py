import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import Ie


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="This is request browser"
    )

    parser.addoption(
            "--url_browser",
            default="https://www.opencart.com/",
            help="url"
        )


@pytest.fixture
def browser(request):
    if request.config.getoption("--browser") == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.headless = False
        chrome_options.add_argument('start-fullscreen')
        wd = webdriver.Chrome(options=chrome_options)
        return wd
    elif request.config.getoption("--browser") == "firefox":
        firefox_option = FirefoxOptions()
        wd = webdriver.Firefox(options=firefox_option)
        wd.maximize_window()
        return wd
    elif request.config.getoption("--browser") == "ie":
        ie_option = Ie()
        wd = webdriver.Ie(options=ie_option)
        return wd


@pytest.fixture
def url_browser(request):
    return request.config.getoption("--url_browser")