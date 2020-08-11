import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost/", help="choose your browser")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome(chrome_options=options)
    elif browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(firefox_profile=profile)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(3)
    driver.maximize_window()

    request.addfinalizer(driver.quit)
    def open(path=""):
        return driver.get(url + path)
    driver.open = open
    driver.open()
    return driver
