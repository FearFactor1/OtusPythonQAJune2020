from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class custom_wait:

    def __init__(self, locator, count):
        self.count = count
        self.locator = locator

    def __call__(self, driver):
        elements = driver.find_elements_by_xpath(self.locator)
        if len(elements) == self.count:
            return elements
        else:
            return False


driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.maximize_window()
# wait = WebDriverWait(driver, 1)

driver.get('https://beru.ru')
el = driver.find_element_by_xpath("//input[@class='mvd1wAJzjc']")
el.click()

el.send_keys('часы')
el.send_keys(Keys.ENTER)

elements = WebDriverWait(driver, 3).until(custom_wait("//div[@class='_1Ybu1aynfr']", 5))
driver.quit()
