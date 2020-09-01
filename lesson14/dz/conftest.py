import pytest
import logging
import allure
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(level=logging.INFO, filename="C:\\PycharmProjects\\OtusPythonQAJune2020\\lesson14\\dz\\results\\selenium.log")


@allure.step("Жду доступности видео")
def url_data_exists(url):
    # Ждем доступности url
    wait = 15
    while wait > 0:
        r = requests.get(url)
        if r.ok:
            return True
        else:
            time.sleep(1)
            wait -= 1
    return False


class MyListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        driver.save_screenshot("lesson14/dz/results/error.png")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--selenoid", action="store", default="localhost")
    parser.addoption("--url_browser_se", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browser_se(request):
    browser = request.config.getoption("--browser")
    selenoid = request.config.getoption("--selenoid")
    fixture_logger = logging.getLogger("fixture")

    executor_url = f"http://{selenoid}:4444/wd/hub"

    options = webdriver.ChromeOptions()
    options.add_argument('start-fullscreen')

    caps = {"browserName": browser,
            #"version": "83.0",
            "enableVnc": True,
#            "enableVideo": True,
            "enableLog": True,
            "screenResolution": "1280x720",
            "name": request.node.name}

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps, options=options)

    session_id = driver.session_id

    allure.attach(name=driver.session_id,
                  body=str(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)

    driver = EventFiringWebDriver(driver, MyListener())
    fixture_logger.info(f"Start session {driver.session_id}")
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture
def url_browser_se(request):
    return request.config.getoption("--url_browser_se")