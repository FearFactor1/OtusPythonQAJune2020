import pytest
import logging

from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)

DRIVERS = "/Users/mikhail/Downloads/drivers"


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    return driver
