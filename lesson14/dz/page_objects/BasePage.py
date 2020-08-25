import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    def return_home(self):
        self.logger.info("return_home")
        self.driver.find_element_by_link_text("Your Store").click()

    def return_desktop(self):
        self.logger.info("return_desktop")
        self.driver.find_element_by_css_selector("ul.breadcrumb").find_element_by_link_text("Desktops").click()

    def _click(self, selector, index=0):
        self.logger.info("_click: {}".format(selector))
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def __element(self, selector: dict, index: int, link_text: str = None):
        self.logger.info("selector {} index {} link_text {}".format(selector, index, link_text))
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def _input(self, selector, value, index=0):
        self.logger.info("selector {} value {} index {}".format(selector, value, index))
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)