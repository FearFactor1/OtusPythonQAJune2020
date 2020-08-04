from pytest import fixture
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@fixture(scope='session', name='driver')
def get_driver():
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver.maximize_window()
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()


@fixture
def wait(driver):
    wait = WebDriverWait(driver, 5)
    yield wait
