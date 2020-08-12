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
            default="https://demo.opencart.com/",
            help="url"
        )


@pytest.fixture
def browsers(request):
    if request.config.getoption("--browser") == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.headless = False
        chrome_options.add_argument('start-fullscreen')
        wd = webdriver.Chrome(options=chrome_options)
        wd.implicitly_wait(4)
        return wd
    elif request.config.getoption("--browser") == "firefox":
        firefox_option = FirefoxOptions()
        wd = webdriver.Firefox(options=firefox_option)
        wd.maximize_window()
        wd.implicitly_wait(3)
        return wd
    elif request.config.getoption("--browser") == "ie":
        ie_option = Ie()
        wd = webdriver.Ie(options=ie_option)
        wd.implicitly_wait(3)
        return wd
    else:
        raise Exception(f"{request.param} is not supported!")


@pytest.fixture
def url_browsers(request):
    return request.config.getoption("--url_browser")